import requests
from bs4 import BeautifulSoup
import json

url = input("Entrez l'URL de la page à scraper : ")
filename = input("Entrez le nom du fichier JSONL à générer : ")
if not filename.endswith(".jsonl"):
    filename += ".jsonl"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    sections = soup.find_all(['h2', 'p'])  # <h2> et les paragraphes <p>

    data = []
    current_title = ""
    content = ""

    # Parcourir le tout
    for section in sections:
        if section.name == 'h2': 
            if current_title and content:
                # on évite le menu sans container
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
                content = "" 

            current_title = section.get_text()
        elif section.name == 'p': 
            content += section.get_text() + "\n"

    if current_title and content:
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
