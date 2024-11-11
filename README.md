# Chatbot
# API de Recherche Optimisée avec FAISS

## 📖 Description
Cette API permet d'encoder des documents et de rechercher les documents les plus pertinents en utilisant l'index **FAISS** pour une recherche rapide et optimisée.

## 🚀 Fonctionnalités
- Encodage des documents en vecteurs d'embeddings.
- Indexation et recherche optimisée avec **FAISS**.
- Chargement des documents depuis un fichier texte.
- Documentation automatique via Swagger UI.

## 🛠️ Installation
Suivez ces étapes pour installer et exécuter l'API localement.

### Prérequis
- Python 3.10 ou plus récent.
- Pip (gestionnaire de paquets Python).

### Étapes d'Installation
1. Clonez le dépôt :
   git clone <https://github.com/SarraBrahem/Chatbot.git>
   cd Chatbot


2. Installez les dépendances :
pip install -r requirements.txt

3. Lancez le serveur :
uvicorn main:app --host 127.0.0.1 --port 8000 --reload

### 📄 Documentation de l'API
Accédez à la documentation Swagger UI ici : http://127.0.0.1:8000/docs

### 📌 Endpoints de l'API
POST /encode_documents
Encode une liste de documents et les sauvegarde.

- Exemple de Requête
{
    "documents": [
        "Le climat change, il est temps d'agir.",
        "Article 1 : Toute personne a droit au respect de sa vie privée."
    ]
}

- Exemple de Réponse
{
    "status": "success",
    "message": "Documents encodés et sauvegardés."
}

### POST /load_from_file
Charge des documents depuis un fichier texte et les encode.

- Exemple de Requête
{
    "file_path": "articles_law.txt"
}

- Exemple de Réponse
{
    "status": "success",
    "message": "Documents encodés et sauvegardés."
}

### POST /search_documents
Recherche les documents les plus pertinents pour une requête donnée.

- Exemple de Requête
{
  "query": "droit"
}

- Exemple de Réponse
{
  "relevant_documents": [
    {
      "id": 8,
      "text": "droits fondamentaux.",
      "similarity_score": -29.803171157836914
    },
    {
      "id": 13,
      "text": "Article 9: Toute personne a droit à la liberté d'expression, sous réserve de ne pas porter atteinte à l’ordre",
      "similarity_score": -48.82200241088867
    },
    {
      "id": 1,
      "text": "constituait pas une infraction pénale selon le droit national ou international.",
      "similarity_score": -50.614471435546875
    },
    {
      "id": 7,
      "text": "Article 5: Toute personne a droit à un recours effectif devant une instance nationale pour les actes violant les",
      "similarity_score": -51.511207580566406
    },
    {
      "id": 12,
      "text": "Article 8: Toute personne a droit au respect de sa vie privée et familiale, de son domicile et de sa correspondance.",
      "similarity_score": -56.47993850708008
    }
  ]
}

### 🧪 Tests
Lancez les tests unitaires pour vérifier que toutes les fonctionnalités de l'API fonctionnent correctement.

pytest test_main.py

- Exemple de Résultats des Tests

============================= test session starts =============================
collected 6 items

test_main.py::test_encode_documents PASSED
test_main.py::test_search_documents PASSED
test_main.py::test_load_from_file PASSED
test_main.py::test_load_from_file_not_found PASSED
test_main.py::test_search_empty_query PASSED
test_main.py::test_search_without_encoding PASSED

============================== 6 passed in 3.00s ===============================

### 📂 Structure du Projet

Chatbot/
├── main.py
├── test_main.py
├── README.md
├── requirements.txt
├── articles_law.txt
├── embeddings.json
├── .dist/
├── .pytest_cache/
└── __pycache__/


### 🤝 Contributeur
Sarra Brahem

### 📅 Licence
Ce projet est sous licence MIT. Vous êtes libre de l'utiliser, de le modifier et de le distribuer.