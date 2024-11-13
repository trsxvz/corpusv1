# SCRIPT EN COURS DE REALISATION - NON FONCTIONNEL POUR LE MOMENT

# ---------- IMPORTATION DES LIBRAIRIES UTILES ----------

# Importation des modules système :
import os
import sys

# Importation de Pip (en cas d'installation spécial de python) :
try:
    import pip
except ImportError:
    # Téléchargement et installation de get-pip.py pour installer pip
    os.system(f'{sys.executable} -m ensurepip --default-pip')
    os.system(f'{sys.executable} -m pip install --upgrade pip')

# Pour gérer les requêtes HTTP :
try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests

# Pour scrap des pages HTML :
try:
    from bs4 import BeautifulSoup
except ImportError:
    os.system('pip install beautifulsoup4')
    from bs4 import BeautifulSoup

# Pour pouvoir travailler avec les fichiers JSON (librairie incluse par défaut à python) : 
import json

# ---------- DÉBUT DU SCRAP ----------