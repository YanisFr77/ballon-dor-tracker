# Aide-mémoire

Commandes, syntaxes et concepts réutilisables dans n'importe quel projet. Complété au fil des missions.
Environnement : Windows et PowerShell, sauf mention contraire.

## PowerShell

| Besoin | Commande | À savoir |
|---|---|---|
| Lister les fichiers, cachés compris | `ls -Force` | `ls -a` est un réflexe Linux, il ne marche pas en PowerShell |
| Savoir quel exécutable est utilisé | `where.exe python` | La **première ligne** est celle qui s'exécute (premier trouvé dans le PATH) |
| Version d'un outil | `python --version`, `git --version`, `code --version` | |
| Autoriser les scripts (dont l'activation du venv) | `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` | `CurrentUser` : ton compte seulement, sans droits admin. `Process` : le terminal en cours. `LocalMachine` (par défaut) : demande les droits admin |

## Environnement virtuel (venv)

```powershell
python -m venv .venv            # l'argument est le DOSSIER DU VENV, pas celui du projet
.\.venv\Scripts\Activate.ps1    # activer (PowerShell) ; activate.bat, c'est pour cmd
deactivate                      # désactiver
where.exe python                # preuve : la 1re ligne doit pointer vers .venv\Scripts\python.exe
```

- L'invite affiche `(.venv)` quand il est actif.
- Un venv ne se copie pas et ne se versionne pas (lourd, propre à la machine) : on le **recrée** après un clone.
- VS Code cherche `.venv` à la racine du dossier ouvert : ouvre le dossier du projet, pas son parent.

## `.gitignore` de base (Python)

```
.venv/
.env
```

- `.venv/` = le dossier du venv. `.env` = le fichier des secrets (clés d'API). Deux choses différentes.
- Le `.gitignore` va **à la racine** du projet, pas dans `.venv/`.

## Git

### Configuration

```powershell
git config --global init.defaultBranch main   # nouvelles branches nommées main
git config --global user.email "x@y.z"        # identité par défaut, pour tous les repos
git config user.email "x@y.z"                 # identité de CE repo seulement (le local l'emporte sur le global)
git config user.email                         # afficher la valeur active
git config --local user.email                 # afficher seulement la valeur locale
```

- **Identité** (`user.name`, `user.email`) : texte écrit dans chaque commit, GitHub ne la vérifie pas.
- **Authentification** : qui a le droit de push. Elle est gérée par Git Credential Manager (connexion via le navigateur).
- Push refusé (`access denied` avec le mauvais compte) :
  ```powershell
  cmdkey /delete:git:https://github.com   # ou : Gestionnaire d'identification Windows → supprimer git:https://github.com
  ```
  Ensuite, **vérifie le compte connecté sur github.com dans le navigateur** (sinon il réautorise le mauvais), puis relance `git push`.

### Démarrer un projet

```powershell
git init                                   # crée le dossier caché .git (tout l'historique local)
git branch -M main                         # renommer la branche courante en main
git remote add origin https://github.com/<user>/<repo>.git
git push -u origin main                    # premier push : -u lie main à origin/main
```

### Récupérer un projet existant

```powershell
cd <dossier PARENT>                        # ex. Documents
git clone https://github.com/<user>/<repo>.git   # crée lui-même le dossier <repo>
```

Ne crée pas le dossier à la main avant : tu aurais `repo\repo\`.

### Le quotidien

```powershell
git status                     # où j'en suis : fichiers modifiés, en avance ou en retard sur origin
git diff                       # ce qui a changé, pas encore ajouté
git add <fichier>              # préparer pour le commit
git commit -m "message"        # instantané enregistré dans l'historique
git push                       # envoyer les commits vers GitHub
git pull                       # récupérer ceux de GitHub
git log --oneline -5           # les 5 derniers commits
git ls-remote origin           # voir ce qui est vraiment sur GitHub
```

- Deux machines : `git pull` en arrivant, `git push` en partant. Ce qui n'est pas pushé n'existe pas pour l'autre machine.
- Un message de commit décrit **ce qui change** : `main.py : corrige affiche_joueur et les annotations`, pas `mise à jour`.
- Ne pas modifier le même fichier sur deux machines sans pull/push entre les deux : risque de conflit.
- Git cherche `.git` dans le dossier courant puis dans les dossiers parents.

### Pull Request (PR)

Une demande de fusion d'une branche dans une autre (souvent vers `main`), faite sur GitHub. On relit le diff, puis on clique sur « Merge ». Après la fusion, `git pull` sur chaque machine pour récupérer `main`.

## Python

### Classe

```python
class Joueur:
    def __init__(self, nom: str, buts: int):   # les annotations se mettent sur les paramètres
        self.nom = nom      # self.nom est stocké dans l'objet ; nom est local à __init__
        self.buts = buts

    def score(self) -> float:
        return self.buts * 1.2

j = Joueur(nom="Pedri", buts=2)    # arguments nommés : plus lisible que Joueur("Pedri", 2)
```

### Annotations de type

```python
def classement(joueurs: list[Joueur]) -> None:
```

Python les **ignore** à l'exécution. Elles servent à l'éditeur (Pylance : autocomplétion, soulignement), aux vérificateurs comme `mypy`, et aux humains (bientôt aux LLM, pour décrire des tools).

### Dict : `[]` ou `.get()`

```python
d = {"Liga": 12}
d["Ligue 1"]          # KeyError: 'Ligue 1' → plante tout de suite et nomme la clé fautive
d.get("Ligue 1")      # None, sans erreur → le bug explose plus loin (TypeError au +=)
d.get("Ligue 1", 0)   # 0 : valeur par défaut, quand l'absence est normale
```

Principe du **fail fast** : planter tôt et clairement plutôt que tard et de façon obscure. `[]` quand la clé **doit** exister.

### Trier une liste d'objets

```python
joueurs.sort(key=Joueur.score, reverse=True)   # trie SUR PLACE, ne renvoie rien (None)
tries = sorted(joueurs, key=Joueur.score)      # renvoie une NOUVELLE liste
```

On passe la fonction **sans parenthèses** : `sort` l'appellera sur chaque élément.

### f-string

```python
print(f"{i+1}. {j.nom} : {j.score()} pts")
```

### Piège : la virgule qui crée un tuple

```python
x = [1, 2],      # ([1, 2],) : un tuple d'UN SEUL élément, pas une liste
```

## Agents et LLM (concepts)

Source : « Building effective agents » (Anthropic).

- **Workflow** : le **code** fixe le chemin. **Agent** : le **LLM** tourne en boucle avec des outils et choisit lui-même la suite.
- À savoir : dans un workflow, le chemin est fixe, mais chaque appel au LLM reste **non déterministe**. Le critère n'est pas « code ou no-code ». Un framework (LangGraph, Agent SDK) sert à construire les deux.
- Règle d'or : commencer par **le plus simple qui marche**, et n'ajouter de l'autonomie que si elle fait gagner en eval.

| Pattern | Principe | Quand l'utiliser |
|---|---|---|
| Prompt chaining | Des étapes en file indienne : chaque appel reprend la sortie du précédent | Une tâche découpable en étapes **fixes** |
| Routing | On classe l'entrée, puis on l'envoie vers le bon traitement | Des types de demandes bien distincts (ex. une question de stats → l'agent stats) |
| Parallelization | Des sous-tâches en parallèle (*sectioning*), ou la même tâche plusieurs fois pour voter (*voting*) | Gagner du temps, ou de la fiabilité par le vote |
| Orchestrator-workers | Un LLM découpe la tâche et la distribue à des workers, puis fait la synthèse | Les sous-tâches **ne sont pas prévisibles** à l'avance (ex. « Kane ou Mbappé ? » → stats + actu) |
| Evaluator-optimizer | Un LLM produit, un autre évalue et renvoie un retour, en boucle | Il existe des critères clairs pour juger, et des retours qui améliorent vraiment le résultat |
