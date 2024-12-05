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

### 🖥️ Interface Client en Ligne de Commande
Ce projet inclut une interface client (client.py) qui permet d'interagir directement avec l'API Chatbot via la ligne de commande. L'interface est conviviale et permet d'encoder des documents ou de rechercher des documents pertinents.

### Comment Utiliser l'Interface Client :

1. Étape 1 : Démarrer l'Interface Client
Exécute le script client.py en ligne de commande :
- python client.py

2. Étape 2 : Options Disponibles
Vous serez accueilli par le message suivant :
===========================
Bienvenue dans l'interface de commande pour l'API Chatbot
1. Encoder des documents
2. Rechercher des documents
Choisissez une option (1 ou 2) :
===========================

### Option 1 : Encoder des Documents
Permet d'encoder une nouvelle liste de documents pour la recherche.
Vous serez invité à entrer une liste de documents.

### Option 2 : Rechercher des Documents
Permet de rechercher des documents pertinents en fonction de la requête saisie par l’utilisateur.

### Exemple d’Utilisation

1. Démarrer l'interface client :
python client.py

2. Choisir l'option 2 pour rechercher des documents :
===========================
Bienvenue dans l'interface de commande pour l'API Chatbot
1. Encoder des documents
2. Rechercher des documents
Choisissez une option (1 ou 2) : 2
Entrez votre requête de recherche : droit
===========================

- Résultats de la recherche :
===========================
Documents pertinents trouvés :
ID : 8, Texte : droits fondamentaux., Score : -29.80
ID : 13, Texte : Article 9: Toute personne a droit à la liberté d'expression, sous réserve de ne pas porter atteinte à l’ordre, Score : -48.82
ID : 1, Texte : constituait pas une infraction pénale selon le droit national ou international., Score : -50.61
ID : 7, Texte : Article 5: Toute personne a droit à un recours effectif devant une instance nationale pour les actes violant les, Score : -51.51
ID : 12, Texte : Article 8: Toute personne a droit au respect de sa vie privée et familiale, de son domicile et de sa correspondance., Score : -56.48
===========================

### Fonctionnalités de l'Interface Client :
- Encodage de Documents : Permet à l'utilisateur de saisir et encoder une liste de documents.
- Recherche de Documents : Recherche et affiche les documents les plus pertinents pour la requête saisie.

- Conseils pour l'Utilisation :
Assurez-vous que le serveur API est en cours d'exécution avant d'utiliser client.py. Pour démarrer le serveur

### 📂 Structure du Projet

Chatbot/
├── main.py
├── .gitignore
├── client.py
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
