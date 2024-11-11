from fastapi.testclient import TestClient
from main import app
import os

client = TestClient(app)

# Test d'encodage des documents
def test_encode_documents():
    response = client.post("/encode_documents", json={"documents": ["Test document", "Another document"]})
    assert response.status_code == 200
    assert response.json()["status"] == "success"

# Test de recherche de documents
def test_search_documents():
    response = client.post("/search_documents", json={"query": "Test"})
    assert response.status_code == 200
    assert "relevant_documents" in response.json()
    assert len(response.json()["relevant_documents"]) > 0

# Test de chargement de documents depuis un fichier
def test_load_from_file():
    # Crée un fichier de test
    test_file_path = "test_file.txt"
    with open(test_file_path, "w", encoding="utf-8") as f:
        f.write("Document 1\nDocument 2\nDocument 3\n")

    response = client.post("/load_from_file", json={"file_path": test_file_path})
    assert response.status_code == 200
    assert response.json()["status"] == "success"

    # Supprime le fichier de test après le test
    os.remove(test_file_path)

# Test pour un fichier inexistant
def test_load_from_file_not_found():
    response = client.post("/load_from_file", json={"file_path": "fichier_inexistant.txt"})
    assert response.status_code == 404
    assert response.json()["detail"] == "Fichier de documents introuvable."


# Test pour une requête vide
def test_search_empty_query():
    response = client.post("/search_documents", json={"query": ""})
    assert response.status_code == 400
    assert response.json()["detail"] == "Requête vide."

# Test pour l'index FAISS non initialisé
def test_search_without_encoding():
    from main import index
    if index is not None:
        index.reset()

    response = client.post("/search_documents", json={"query": "Test"})
    assert response.status_code == 500, f"Statut retourné : {response.status_code}, contenu : {response.json()}"
    assert "Index FAISS non initialisé" in response.json()["detail"] or "Index FAISS est vide" in response.json()["detail"]


