import requests

BASE_URL = "http://127.0.0.1:8000"

def encode_documents():
    file_path = input("Entrez le chemin du fichier texte à encoder (par exemple, articles_law.txt) : ")
    response = requests.post(f"{BASE_URL}/load_from_file", json={"file_path": file_path})
    if response.status_code == 200:
        print("Documents encodés avec succès !")
    else:
        print(f"Erreur : {response.json().get('detail', 'Erreur inconnue')}")

def search_query():
    query = input("Entrez votre requête de recherche : ")
    response = requests.post(f"{BASE_URL}/search_documents", json={"query": query})
    if response.status_code == 200:
        documents = response.json()["relevant_documents"]
        print("Documents pertinents trouvés :")
        for doc in documents:
            print(f"ID : {doc['id']}, Texte : {doc['text']}, Score : {doc['similarity_score']:.2f}")
    else:
        print(f"Erreur : {response.json().get('detail', 'Erreur inconnue')}")

def main():
    print("Bienvenue dans l'interface de commande pour l'API Chatbot")
    print("1. Encoder des documents")
    print("2. Rechercher des documents")
    choix = input("Choisissez une option (1 ou 2) : ")

    if choix == "1":
        encode_documents()
    elif choix == "2":
        search_query()
    else:
        print("Choix invalide.")

if __name__ == "__main__":
    main()
