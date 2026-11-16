import os

import requests
from dotenv import load_dotenv

# La clé est lue dans .env (jamais écrite dans le code, jamais commitée)
load_dotenv()
CLE_API = os.environ["API_FOOTBALL_KEY"]

URL_BASE = "https://v3.football.api-sports.io"


def appel(route: str, parametres: dict) -> dict:
    reponse = requests.get(
        URL_BASE + route,
        headers={"x-apisports-key": CLE_API},
        params=parametres,
        timeout=10,
    )
    reponse.raise_for_status()
    return reponse.json()


# 1. Le compte : quel plan, combien de requêtes utilisées aujourd'hui
statut = appel("/status", {})
print("Compte :", statut["response"])

# 2. Critères "saisons" et "sélection" : la CDM 2022 (league=1, saison 2022)
# puis la Premier League 25/26 (league=39, saison 2025)
for ligue, saison in [(1, 2022), (39, 2025)]:
    donnees = appel("/fixtures", {"league": ligue, "season": saison})
    print(f"\nLigue {ligue}, saison {saison}")
    print("  Erreurs :", donnees["errors"])
    print("  Nombre de matchs :", donnees["results"])
