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
- [x] Installer l'extension Claude Code dans VS Code
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

### 2026-10-24 : Mission extension Claude Code dans VS Code
- Mission donnée : installer l'extension, ouvrir le dossier, choisir l'interpréteur du venv, prouver dans le terminal intégré.
- Remarque de revue : les messages des commits `43842cd` et `8576951` parlent de l'« étape 4 », alors que ces commits ne touchent que la doc. Un message de commit doit décrire ce qui change.
- Étape 4 : `where.exe python` affiche `.venv` en premier ✅. Mais le venv a été activé **à la main** avec `Activate.ps1`, ce qui ne prouve pas que VS Code utilise l'interpréteur du venv (étape 3). Il faut le prouver dans un nouveau terminal, sans activation manuelle.
- Q1 à moitié : l'idée est juste, mais formulée de façon floue (« pas accès aux bons fichiers »). Q2 pas comprise, elle a été reformulée.
- Preuve validée ✅ (capture d'écran) : extension Claude Code installée et ouverte, dossier du projet ouvert. Dans un nouveau terminal, VS Code active le venv **tout seul** (`Set-ExecutionPolicy -Scope Process ...; & ...\Activate.ps1`), puis `where.exe python` affiche `.venv` en premier.
- Q2 ✅ : il distingue le Python du venv et le Python global, et sait pourquoi on utilise le venv (versions des librairies propres au projet, pas de conflit avec le Python global).
- Q1 toujours à moitié : il mélange encore Git et venv (« il ne va pas être dans un environnement virtuel »). Correction donnée : Git cherche `.git` dans le dossier courant puis dans ses parents (depuis `Documents`, `git status` renvoie `fatal: not a git repository`). VS Code cherche `.venv` à la racine du dossier ouvert (depuis `Documents`, il prend le Python global).
- Visite guidée de l'extension : diff dans l'éditeur, contexte du fichier ouvert ou de la sélection, modes de permission. Conseil donné : passer de « Edit automatically » à un mode qui demande avant chaque modification, plus cohérent avec le contrat.
- **Mission extension validée.**
- Yanis a choisi de rester dans la même session pour l'étape 4 (conversation encore courte). La session est renommée `[0.1-4] main.py : classement des candidats`.
- Question d'échauffement sur `-Scope Process` vs `CurrentUser` posée. Mission étape 4 donnée.
- Réponse à l'échauffement juste sur le fond (Process = le terminal en cours, CurrentUser = permanent pour son compte). Mais elle se termine par un `»` orphelin : sans doute copiée. Questions de contrôle posées : pourquoi VS Code relance-t-il `Process` alors que `CurrentUser` est déjà réglé, et quel scope demande les droits admin ?
- Contrôle ✅ : `LocalMachine` demande les droits admin, et c'est le scope par défaut si on omet `-Scope` (bonus trouvé seul). L'erreur de l'étape 2 sur `CurrentUser` est corrigée. Pour `Process`, il sait qu'il a la priorité sur `CurrentUser` et `LocalMachine`. Complément donné par Claude : VS Code ne connaît pas la configuration de la machine, il garantit donc que l'activation marche partout, sans rien modifier de façon permanente. **Échauffement validé.**
- `main.py` commencé avec une `@dataclass Joueur` (nom, club, buts, `passes_D`, `prix_moyen = 0.0`) et un seul joueur créé avec des arguments positionnels. Choix de la dataclass validé sur le principe, mais il doit l'expliquer (c'est un outil avancé pour son niveau, était-ce une suggestion de l'IA ?). Revue faite : nommage `passes_D`, sens de `prix_moyen` et de sa valeur par défaut, arguments positionnels peu lisibles.

### 2026-10-25 : Recadrage du projet et du contrat
- Yanis remet en question la règle « zéro IA » : son but est d'être AI engineer (piloter l'IA, la challenger, concevoir les algorithmes), pas développeur expert. Argument recevable. Limite rappelée : on ne peut pas relire du code qu'on ne sait pas lire (exemple de la dataclass).
- **Décision : mode copilote à partir du niveau 1.** Spec ou algorithme écrit par Yanis, puis code généré par l'IA, puis relecture avec questions de Claude et chasses au bug annoncées. Le niveau 0 (`main.py`) reste écrit à la main. Les boss fights restent sans IA.
- **Décision : le projet s'élargit (option B).** Il devient un analyste foot IA multi-agents. L'Oracle Ballon d'Or est la fonctionnalité phare et le benchmark d'eval (vérité terrain 2023-2026). L'option C (agent scout/mercato) est gardée pour après le niveau 7.
- **Roadmap réécrite dans `CLAUDE.md`** : dbt et le médaillon complet sont abandonnés, le LLM arrive au niveau 2, deux niveaux nouveaux : les evals et l'observabilité (Langfuse ou LangSmith) au niveau 3, « Construis ton harnais » au niveau 4.
- Mémoire automatique de Claude comparée à `CLAUDE.md` : elle est stockée hors du repo et propre à chaque machine, donc on garde `PROGRESSION.md` comme mémoire du projet.
- « OMP » = **Oh My Pi**, un harnais d'agent de code pour le terminal, à l'opposé de Pi (harnais minimaliste) : beaucoup d'outils intégrés (LSP, navigateur, subagents). À étudier au niveau 4 comme exemple de harnais.

## Prochaine session : contexte

- **Titre de la prochaine session :** `[0.1-4] main.py : classement des candidats`
- **Mission suivante :** finir 0.1 étape 4, `main.py` **écrit à la main** (dernier code 100 % manuel du parcours). Mission complète : 5 joueurs dans une seule structure, au moins 3 stats de performance, une fonction de score, des poids définis une seule fois en haut du fichier, un tri fait par le code, un affichage `1. Nom (Club) : X pts`, puis un commit au message descriptif et un push.
- **En attente de Yanis sur `main.py` :** expliquer ce que fait `@dataclass` (pourquoi `print(j)` affiche un rendu lisible) et d'où vient l'idée. Corriger `passes_D` (snake_case, pas d'espace avant `:`), remplacer ou justifier `prix_moyen` et sa valeur par défaut, et utiliser des arguments nommés.
- **Puis :** 0.2 "Le transfert" (laptop), théorie "Building effective agents", boss fight du niveau 0. Ensuite, niveau 1 en mode copilote : il faudra expliquer à Yanis comment se passe une mission dans ce mode.
- **Points fragiles de Yanis à surveiller :**
  - Confusion entre `.env` (fichier de secrets) et `.venv` (dossier du venv) : déjà 2 fois.
  - A tendance à lancer des commandes sans vérifier ce qu'elles ciblent (cas des arguments de `venv`).
  - Réponses parfois trop rapides ou approximatives, ou trop « manuel » (sans doute copiées) : lui demander de reformuler avec ses mots. Il y arrive quand on insiste.
  - Réflexes Linux dans PowerShell (`ls -a`).
  - Mélange les rôles de Git et du venv : deux outils indépendants qui sont juste dans le même dossier.
  - Prouve parfois le mauvais point : il a activé le venv à la main pour prouver que VS Code l'activait.
  - Messages de commit qui ne décrivent pas ce qui change.
- **Points forts :** se débloque seul quand il lit les messages d'erreur (politique d'exécution PowerShell, `git init` manquant, `ls -Force`). A fait le bonus `init.defaultBranch=main`.
- **Environnement :** Windows, PowerShell, Python 3.13.14 (Microsoft Store). Activer le venv avec `.\.venv\Scripts\Activate.ps1`. VS Code est installé avec l'extension Claude Code, et l'interpréteur du venv est sélectionné. Utiliser le panneau Terminal de l'app pour que Claude puisse lire les commandes, ou coller la sortie du terminal VS Code. Git : branche `main`, remote `origin` = github.com/YanisFr77/ballon-dor-tracker, authentification via Git Credential Manager (navigateur). Identité : gmail en local pour ce repo, email de l'université en global.
