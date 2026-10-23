# Journal de bord

## Niveau actuel : 0 (Le vestiaire)

### Missions du niveau 0
- [x] 0.1 étape 1 : créer le dossier `ballon-dor-tracker`
- [x] 0.1 étape 2 : environnement virtuel Python (venv), `.gitignore` racine (`.venv/` et `.env`)
- [x] 0.1 étape 3 : `git init`, repo GitHub public, premier push
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
- Branche renommée en `main` ✅, plus `init.defaultBranch=main` en global (bonus) ✅. Staging et `git status` faits ✅. Commit `46866f3` "initialisation projet ballon dor tracker" ✅.
- Identité configurée à deux niveaux : email de l'université en global, gmail en local (c'est celui qui a signé le commit). Demander à Yanis si c'est voulu.
- Remote `origin` ajouté ✅. **Le push échoue** : `Password authentication is not supported`, GitHub refuse les mots de passe depuis 2021. Le Git Credential Manager est installé : il faut passer par la connexion navigateur, ou supprimer un identifiant erroné resté dans le Gestionnaire d'identification Windows.
- Push réussi ✅ : `origin/main` est sur `46866f3`, Claude l'a vérifié avec `git ls-remote`.
- Questions : « le local l'emporte sur le global » ✅. « Quel email pour GitHub ? » sans réponse. `where.exe python` ✅. « Qu'a créé `git init` ? » ❌ : il répond « invisible car aucun commit », alors que c'est le dossier `.git`, caché, qui contient tout le dépôt.
- Questions de fin d'étape : Q2 (`.gitignore`) ✅, Q3 (README côté GitHub, push refusé) ✅. Q1 à moitié : `add` ✅, mais pour lui `commit` = « ajouter un commentaire », alors que c'est un **instantané** enregistré dans l'historique. Réponse à préciser.
- Q1 reformulée : correcte, mais rédaction très « manuel », peut-être copiée ; à vérifier avec ses propres mots. `ls -a` échoue, puis Yanis trouve `ls -Force` seul ✅ : `.git` apparaît avec l'attribut `h` (caché). « Si on supprime `.git` » : réponse incomplète (« plus de connexion à GitHub »), il oublie que tout l'historique local est perdu. Email GitHub ✅. Fichiers présents sur github.com ✅.
- Commit expliqué avec ses mots ✅ : « l'id du projet à l'instant t », un point de sauvegarde pour restaurer un fichier. Il reste la question « que perd-on en supprimant `.git` ? ».
- `.git` ✅ : supprimer ce dossier fait perdre tout l'historique local, mais le code actuel reste sur le disque. Nuance donnée par Claude : une copie de l'historique poussé reste aussi sur GitHub. **Étape 3 validée.**

## Prochaine session : contexte

- **Mission suivante :** installer l'extension Claude Code dans VS Code, puis ouvrir le projet dans VS Code. C'est une mission courte, le bon moment pour expliquer ce que l'extension apporte (diff, sélection de code, etc.).
- **Ensuite :** 0.1 étape 4, `main.py` qui classe 5 candidats au Ballon d'Or 2027 avec un score, écrit sans code généré. Penser à activer le venv avant de lancer Python.
- **Puis :** 0.2 "Le transfert" (laptop), théorie "Building effective agents", boss fight du niveau 0.
- **Points fragiles de Yanis à surveiller :**
  - Confusion entre `.env` (fichier de secrets) et `.venv` (dossier du venv) : déjà 2 fois.
  - A tendance à lancer des commandes sans vérifier ce qu'elles ciblent (cas des arguments de `venv`).
  - Réponses parfois trop rapides ou approximatives, ou trop « manuel » (sans doute copiées) : lui demander de reformuler avec ses mots. Il y arrive quand on insiste.
  - Réflexes Linux dans PowerShell (`ls -a`).
- **Points forts :** se débloque seul quand il lit les messages d'erreur (politique d'exécution PowerShell, `git init` manquant, `ls -Force`). A fait le bonus `init.defaultBranch=main`.
- **Environnement :** Windows, PowerShell, Python 3.13.14 (Microsoft Store). Activer le venv avec `.\.venv\Scripts\Activate.ps1`. Utiliser le panneau Terminal de l'app pour que Claude puisse lire les commandes. Git : branche `main`, remote `origin` = github.com/YanisFr77/ballon-dor-tracker, authentification via Git Credential Manager (navigateur). Identité : gmail en local pour ce repo, email de l'université en global.
