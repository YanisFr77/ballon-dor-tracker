# Journal de bord

## Niveau actuel : 0 (Le vestiaire)

### Missions du niveau 0
- [x] 0.1 étape 1 : créer le dossier `ballon-dor-tracker`
- [x] 0.1 étape 2 : environnement virtuel Python (venv), `.gitignore` racine (`.venv/` et `.env`)
- [ ] 0.1 étape 3 : `git init`, repo GitHub public, premier push
- [ ] 0.1 étape 4 : `main.py` qui classe 5 candidats au Ballon d'Or 2027 avec un score (sans code généré par l'IA)
- [ ] 0.2 "Le transfert" : installer Python, VS Code et Git sur le laptop perso, cloner, ajouter un 6e candidat, push, puis pull sur le PC fixe
- [ ] Théorie : lire "Building effective agents" (Anthropic) et répondre aux 3 questions
  1. Quelle différence entre un workflow et un agent ?
  2. Les agents no-code du boulot, c'est plutôt l'un ou l'autre ?
  3. Un pattern de l'article utile pour le Tracker ?
- [ ] Installer l'extension Claude Code dans VS Code
- [ ] Boss fight du niveau 0

**Délai :** fin de la première semaine en entreprise.

## Historique des sessions

### 2026-10-23 : Session d'orientation
- Cadre posé : objectif AI engineer, projet fil rouge, contrat prof/élève, rythme selon les mois.
- Dossier créé, `CLAUDE.md` et `PROGRESSION.md` en place.
- Décisions techniques (détail dans `CLAUDE.md`) :
  - **GCP** retenu pour le niveau 6, car c'est le cloud du boulot. Essai gratuit à activer seulement à ce moment-là, avec une alerte de budget.
  - Stack du boulot notée : BigQuery, Superset, S3NS. Piste : un dashboard Superset sur le Tracker.
  - **Architecture médaillon** : bronze au niveau 1, silver et gold avec **dbt** au niveau 2.
  - **DuckDB** remplace SQLite : fonctionne hors ligne et avec dbt, et le passage à BigQuery sera simple.
- Mission étape 2 (venv) donnée.
- Étape 2, premier essai : Python 3.13.14 (version Microsoft Store). La commande `python -m venv Python C:\...\ballon-dor-tracker` a créé **deux** venvs : un dans `Python/`, et un à la racine du projet (`Include/`, `Lib/`, `Scripts/`, `pyvenv.cfg`, plus un `.gitignore` contenant `*` qui ignorerait tout le projet). Yanis doit nettoyer et recommencer avec `.venv`.
- Leçon : chaque argument donné à `venv` est un dossier où créer un environnement.
- Deuxième essai : le dossier `Python/` est bien supprimé, mais le venv a de nouveau été créé à la racine (`python -m venv C:\...\ballon-dor-tracker`). Point à retenir : l'argument est le **dossier du venv**, pas le dossier du projet.
- Troisième essai réussi ✅ : racine nettoyée, `python -m venv .venv` lancé depuis le projet, dans le panneau Terminal de l'app (Claude peut le lire).
- Tentative de preuve refusée : `cd .venv` puis `python --version` ne prouve rien. Entrer dans un dossier n'active pas le venv, et la version est la même dans les deux cas. Indice offert : le script d'activation se trouve dans `.venv\Scripts`, et une fois le venv actif, l'invite affiche `(.venv)`.
- Activation réussie ✅ : `activate.bat` ne marche pas dans PowerShell (c'est le script pour cmd). `Activate.ps1` a été bloqué par la politique d'exécution, et Yanis a débloqué seul, sans indice, avec `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`. L'invite affiche `(.venv)`.
- Preuve validée ✅ : `where.exe python` affiche `.venv\Scripts\python.exe` en premier (le premier trouvé dans le PATH est celui qui est utilisé).
- Explication de `RemoteSigned` : correcte dans l'ensemble (les scripts téléchargés sont acceptés s'ils sont signés). `CurrentUser` : **faux**, ce scope sert justement à ne **pas** avoir besoin des droits admin, et ne touche que son compte.
- `.gitignore` : Yanis a modifié celui que venv génère **dans `.venv/`** au lieu d'en créer un à la racine. À refaire.
- Questions : Q1 ✅. Q2 ❌ (rien de sensible dans `.venv` ; la raison : c'est lourd, propre à la machine et recréable). Q3 ❌ (`git clone` ne ramène pas le venv) : piste donnée, `requirements.txt`.
- Q2 ✅ (taille, et inutile puisqu'il se recrée ; complément : un venv est propre à la machine). Q3 ✅ sur le concept `requirements.txt`, à préciser : il liste des **librairies et leurs versions**, pas des commandes. Les commandes pour le générer et l'utiliser seront à trouver pendant la mission 0.2.
- `.gitignore` racine créé, mais il contient `.env/` au lieu de `.venv/` (nouvelle confusion `.env` / `.venv`). Le `.gitignore` interne de `.venv` est bien revenu à son état d'origine.
- `.gitignore` racine corrigé ✅ : `.venv/` et `.env` (bonus fait). **Étape 2 validée.**
- Règle ajoutée au `CLAUDE.md` : Claude conseille de lui-même le bon moment pour changer de session et prépare le passage de relais dans ce fichier.

### 2026-10-24 : Mission 0.1 étape 3 (Git et GitHub)
- Mission donnée. Oubli de Claude : `git init` n'était pas écrit explicitement. Yanis l'a trouvé seul en lisant l'erreur `fatal: not a git repository`.
- `git init` fait. `git status` affiche `.gitignore`, `CLAUDE.md` et `PROGRESSION.md`, mais pas `.venv` ✅. La branche s'appelle `master`, elle doit encore devenir `main`.

## Prochaine session : contexte

- **Mission suivante :** 0.1 étape 3, "Git et GitHub" : `git init`, premier commit (`CLAUDE.md`, `PROGRESSION.md`, `.gitignore`), création d'un repo GitHub public, premier push. Vérifier avec `git status` que `.venv` n'apparaît pas.
- **Ensuite :** installer l'extension Claude Code dans VS Code, puis l'étape 4 (`main.py`).
- **Points fragiles de Yanis à surveiller :**
  - Confusion entre `.env` (fichier de secrets) et `.venv` (dossier du venv) : déjà 2 fois.
  - A tendance à lancer des commandes sans vérifier ce qu'elles ciblent (cas des arguments de `venv`).
  - Réponses parfois trop rapides ou approximatives : lui demander de préciser.
- **Points forts :** se débloque seul quand il lit les messages d'erreur (cas de la politique d'exécution PowerShell).
- **Environnement :** Windows, PowerShell, Python 3.13.14 (Microsoft Store). Activer le venv avec `.\.venv\Scripts\Activate.ps1`. Utiliser le panneau Terminal de l'app pour que Claude puisse lire les commandes. Ensuite, étape 2 terminée → étape 3 (Git et GitHub).
