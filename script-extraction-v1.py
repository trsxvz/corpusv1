import requests
from bs4 import BeautifulSoup
import json

# Demander à l'utilisateur de saisir l'URL et le nom du fichier .jsonl
url = input("Entrez l'URL de la page à scraper : ")
filename = input("Entrez le nom du fichier JSONL à générer : ")

# Ajouter automatiquement l'extension ".jsonl" si elle n'est pas présente
if not filename.endswith(".jsonl"):
    filename += ".jsonl"

# Envoyer une requête pour obtenir le contenu de la page
response = requests.get(url)

# S'assurer que la requête a réussi
if response.status_code == 200:
    # Parser le HTML avec BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Trouver les sections pertinentes du contenu (à ajuster selon la structure HTML)
    sections = soup.find_all(['h2', 'p'])  # Par exemple, capturer les titres <h2> et les paragraphes <p>

    # Initialiser la liste pour stocker les données
    data = []
    # Variables pour stocker le titre courant et les paragraphes associés
    current_title = ""
    content = ""

    # Parcourir les sections et organiser le contenu
    for section in sections:
        if section.name == 'h2':  # Si c'est un titre de section (h2)
            # Si nous avons du contenu accumulé, enregistrons la section précédente
            if current_title and content:
                # Ne pas ajouter l'élément si le titre est "Menu en bas"
                if current_title.strip() != "Menu en bas":
                    data.append({
                        "title": current_title.strip(),
                        "url": url,
                        "content": content.strip(),
                        "category1": "NA",
                        "category2": "NA",
                        "category3": "NA",
                        "category4": "NA",
                        "filierespecifique": "NA",
                        "datespecifique": "NA"
                    })
                content = ""  # Réinitialiser le contenu pour la prochaine section

            # Mettre à jour le titre de la section
            current_title = section.get_text()
        elif section.name == 'p':  # Si c'est un paragraphe
            # Ajouter le texte au contenu
            content += section.get_text() + "\n"

    # Ajouter la dernière section après la boucle
    if current_title and content:
        # Ne pas ajouter l'élément si le titre est "Menu en bas"
        if current_title.strip() != "Menu en bas":
            data.append({
                "title": current_title.strip(),
                "url": url,
                "content": content.strip(),
                "category1": "NA",
                "category2": "NA",
                "category3": "NA",
                "category4": "NA",
                "filierespecifique": "NA",
                "datespecifique": "NA"
            })

    # Écriture avec sauts de ligne pour la lisibilité
    with open(filename, 'w', encoding='utf-8') as f:
        for entry in data:
            f.write(json.dumps(entry, ensure_ascii=False, indent=4) + "\n")

    print(f"Données extraites et sauvegardées dans {filename}")
else:
    print(f"Erreur lors du chargement de la page : {response.status_code}")
