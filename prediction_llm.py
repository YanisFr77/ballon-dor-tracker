"""Oracle v0.5 : un LLM classe les 7 candidats de main.py.

On compare ensuite son classement au vrai, avec la même mesure que la
formule de main.py (la baseline, écart total 12).

Lancer :  python prediction_llm.py
"""

import hashlib
import json
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel, Field

from main import Joueur, candidats, classement, verdict

MODELE = "gemini-3.5-flash-lite"
DOSSIER_CACHE = Path("cache_llm")
JOURNAL = Path("journal_llm.jsonl")
SONDE = (
    "Qui a remporté le Ballon d'Or 2026 ? Si tu ne le sais pas, dis-le, ne devine pas. "
    "Indique aussi jusqu'à quelle date vont tes connaissances."
)


# --- 1. La forme de la réponse qu'on impose au LLM ---

class Ligne(BaseModel):
    nom: str = Field(description="Le nom du joueur, recopié à l'identique")
    justification: str = Field(description="Une phrase qui explique sa place")


class Classement(BaseModel):
    lignes: list[Ligne] = Field(description="Tous les joueurs, du 1er au dernier")


# --- 2. Le prompt ---

def construire_prompt(joueurs: list[Joueur]) -> str:
    """Ne lit que nom, club, buts, passes et titres.

    N'y entrent jamais : RANG_REEL (la vérité terrain), le score de la
    formule, le barème.
    """
    # Ordre alphabétique : l'ordre de la liste ne doit rien souffler au LLM.
    joueurs_tries = sorted(joueurs, key=lambda j: j.nom)
    fiches = []
    for j in joueurs_tries:
        titres = ", ".join(j.titres_majeurs) or "aucun"
        fiches.append(
            f"- Nom : {j.nom} | Club : {j.club} | Buts : {j.buts} | "
            f"Passes décisives : {j.passes_d} | Titres : {titres}"
        )
    return (
        "Tu es juré du Ballon d'Or 2026 (saison 2025/26).\n"
        "Classe ces joueurs du 1er au dernier, à partir de ces seules données.\n"
        "Chaque joueur apparaît une fois. Dans ta réponse, le nom est exactement "
        "le texte du champ « Nom », sans le club.\n\n"
        + "\n".join(fiches)
    )


# --- 3. L'appel au LLM, avec cache et journal (règle « Budget LLM ») ---

def appeler_llm(prompt: str, schema: dict | None = None) -> str:
    """Renvoie le texte du LLM. Même prompt et même modèle : pas de nouvel appel.

    Avec un schéma, la réponse est du JSON qui le respecte. Sans, du texte libre.
    """
    empreinte = hashlib.sha256((MODELE + prompt + json.dumps(schema)).encode()).hexdigest()[:16]
    fichier = DOSSIER_CACHE / f"{empreinte}.json"

    if fichier.exists():
        print(f"[cache] réponse relue dans {fichier}, aucun appel au LLM")
        return json.loads(fichier.read_text(encoding="utf-8"))["texte"]

    if input(f"1 appel à {MODELE} (offre gratuite). On y va ? (o/n) ") != "o":
        raise SystemExit("Appel annulé.")

    client = genai.Client()  # lit GEMINI_API_KEY dans l'environnement
    if schema is None:
        reponse = client.interactions.create(model=MODELE, input=prompt)
    else:
        reponse = client.interactions.create(
            model=MODELE,
            input=prompt,
            response_format={"type": "text", "mime_type": "application/json", "schema": schema},
        )
    appel = {
        "date": datetime.now().isoformat(timespec="seconds"),
        "modele": MODELE,
        "tokens_entree": reponse.usage.total_input_tokens,
        "tokens_sortie": reponse.usage.total_output_tokens,
        "prompt": prompt,
        "texte": reponse.output_text,
    }
    print(f"[appel] {appel['tokens_entree']} tokens en entrée, {appel['tokens_sortie']} en sortie")

    DOSSIER_CACHE.mkdir(exist_ok=True)
    fichier.write_text(json.dumps(appel, ensure_ascii=False, indent=2), encoding="utf-8")
    with JOURNAL.open("a", encoding="utf-8") as f:
        f.write(json.dumps(appel, ensure_ascii=False) + "\n")
    return appel["texte"]


# --- 4. Le contrôle de la réponse ---

def verifier(reponse: Classement, joueurs: list[Joueur]) -> None:
    """Le schéma garantit la forme, pas le fond : on contrôle les noms."""
    attendus = sorted(j.nom for j in joueurs)
    recus = sorted(ligne.nom for ligne in reponse.lignes)
    if recus != attendus:
        raise ValueError(f"Classement invalide.\nAttendus : {attendus}\nReçus : {recus}")


# --- 5. Le déroulé ---

if __name__ == "__main__":
    load_dotenv()

    # Sonde de contamination : si le modèle connaît déjà le vainqueur,
    # sa « prédiction » peut venir de sa mémoire. À lire avant le classement.
    print("=== Sonde : le modèle connaît-il déjà le résultat ? ===")
    print(appeler_llm(SONDE), "\n")

    prompt = construire_prompt(candidats)
    print(prompt, "\n")

    reponse = Classement.model_validate_json(appeler_llm(prompt, Classement.model_json_schema()))
    verifier(reponse, candidats)

    print("\n=== Classement du LLM ===")
    for rang, ligne in enumerate(reponse.lignes, start=1):
        print(f"{rang}. {ligne.nom} : {ligne.justification}")

    # On remet les objets Joueur dans l'ordre du LLM, pour les mesurer
    # avec la même fonction verdict() que la baseline.
    par_nom = {j.nom: j for j in candidats}
    ordre_llm = [par_nom[ligne.nom] for ligne in reponse.lignes]

    print("\n=== Écarts du LLM ===")
    ecart_llm = verdict(ordre_llm)
    print("\n=== Écarts de la baseline (formule de main.py) ===")
    ecart_baseline = verdict(classement(candidats))

    print(f"\nÉcart total : LLM {ecart_llm}, baseline {ecart_baseline} (plus petit = meilleur)")
