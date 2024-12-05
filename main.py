from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import numpy as np
import json
import os
import faiss

app = FastAPI(
    title="API de Recherche Optimisée avec FAISS",
    description="Une API pour encoder des documents et rechercher les plus pertinents en utilisant FAISS.",
    version="1.1"
)

# Initialisation du modèle et des variables globales
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
embeddings_file = "embeddings.json"
index = None

class Document(BaseModel):
    documents: list[str]

class Query(BaseModel):
    query: str

class FilePath(BaseModel):
    file_path: str

# Sauvegarder les embeddings dans un fichier JSON
def save_embeddings(data):
    try:
        with open(embeddings_file, "w", encoding="utf-8") as f:
            json.dump(data, f)
    except IOError:
        raise HTTPException(status_code=500, detail="Erreur lors de la sauvegarde des embeddings.")

# Charger les embeddings depuis un fichier JSON
def load_embeddings():
    if not os.path.exists(embeddings_file):
        raise HTTPException(status_code=404, detail="Fichier d'embeddings introuvable.")
    try:
        with open(embeddings_file, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Erreur lors du chargement des embeddings.")

# Créer l'index FAISS
def create_faiss_index(embeddings):
    dimension = len(embeddings[0])
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))
    return index

# Charger les embeddings et créer l'index FAISS
def load_embeddings_with_faiss():
    global index
    embeddings_data = load_embeddings()
    embeddings = [np.array(item["embedding"]) for item in embeddings_data]
    if embeddings:
        index = create_faiss_index(embeddings)
        return embeddings_data
    else:
        raise HTTPException(status_code=500, detail="Aucun embedding trouvé pour créer l'index FAISS.")

# Charger des documents depuis un fichier texte
def load_documents_from_file(file_path):
    documents = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            documents = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Fichier de documents introuvable.")
    return documents

# Endpoint pour encoder les documents
@app.post(
    "/encode_documents",
    summary="Encodage des documents",
    description="Encode une liste de documents et les sauvegarde dans l'index FAISS.",
    response_description="Retourne un message de succès si les documents ont été encodés et sauvegardés.",
    responses={
        200: {
            "description": "Succès",
            "content": {
                "application/json": {
                    "example": {
                        "status": "success",
                        "message": "Documents encodés et sauvegardés."
                    }
                }
            }
        },
        400: {"description": "Liste de documents vide."}
    }
)
async def encode_documents(documents: Document):
    if not documents.documents:
        raise HTTPException(status_code=400, detail="Liste de documents vide.")
    
    embeddings_data = []
    for doc_id, text in enumerate(documents.documents):
        embedding = model.encode(text).tolist()
        embeddings_data.append({"id": doc_id, "text": text, "embedding": embedding})
    
    save_embeddings(embeddings_data)
    load_embeddings_with_faiss()
    return {"status": "success", "message": "Documents encodés et sauvegardés."}


# Endpoint pour charger des documents depuis un fichier texte
@app.post("/load_from_file", summary="Charger des documents depuis un fichier", description="Charge des documents depuis un fichier texte et les encode.")
async def load_from_file(file_path: FilePath):
    documents = load_documents_from_file(file_path.file_path)
    return await encode_documents(Document(documents=documents))

# Endpoint pour rechercher des documents pertinents
@app.post(
    "/search_documents",
    summary="Recherche de documents",
    description="Recherche les documents les plus pertinents pour une requête donnée en utilisant l'index FAISS.",
    response_description="Retourne les documents les plus pertinents avec leurs scores de similarité.",
    responses={
        200: {
            "description": "Liste des documents pertinents",
            "content": {
                "application/json": {
                    "example": {
                        "relevant_documents": [
                            {
                                "id": 1,
                                "text": "Document exemple",
                                "similarity_score": 0.95
                            }
                        ]
                    }
                }
            }
        },
        400: {"description": "Requête vide."},
        500: {"description": "Index FAISS non initialisé."}
    }
)
async def search_documents(query: Query):
    if not query.query.strip():
        raise HTTPException(status_code=400, detail="Requête vide.")
    
    if index is None or index.ntotal == 0:
        raise HTTPException(status_code=500, detail="Index FAISS non initialisé ou vide.")
    
    embeddings_data = load_embeddings()
    query_embedding = model.encode(query.query).reshape(1, -1)
    distances, indices = index.search(query_embedding, k=5)

    relevant_documents = []
    for i, idx in enumerate(indices[0]):
        relevant_documents.append({
            "id": embeddings_data[idx]["id"],
            "text": embeddings_data[idx]["text"],
            "similarity_score": float(1 - distances[0][i])
        })
    
    return {"relevant_documents": relevant_documents}


# Gestion des erreurs globales
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    return {"status": "error", "message": str(exc)}

# Charger l'index FAISS au démarrage de l'API
@app.on_event("startup")
def startup_event():
    try:
        load_embeddings_with_faiss()
        print("Index FAISS chargé avec succès.")
    except Exception as e:
        print("Erreur lors du chargement de l'index FAISS :", e)

# Démarrer l'application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
