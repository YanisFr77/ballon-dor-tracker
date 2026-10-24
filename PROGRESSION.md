# Journal de bord

## Niveau actuel : 0 (Le vestiaire)

### Missions du niveau 0
- [x] 0.1 étape 1 : créer le dossier `ballon-dor-tracker`
- [x] 0.1 étape 2 : environnement virtuel Python (venv), `.gitignore` racine (`.venv/` et `.env`)
- [x] 0.1 étape 3 : `git init`, repo GitHub public, premier push
- [x] 0.1 étape 4 : `main.py` qui classe 5 candidats au Ballon d'Or 2027 avec un score (sans code généré par l'IA)
- [ ] 0.2 "Le transfert" : installer Python, VS Code et Git sur le laptop perso, cloner, ajouter un 6e candidat, push, puis pull sur le PC fixe
- [ ] Théorie : lire "Building effective agents" (Anthropic) et répondre aux 3 questions
  1. Quelle différence entre un workflow et un agent ?
  2. Les agents no-code du boulot, c'est plutôt l'un ou l'autre ?
  3. Un pattern de l'article utile pour le Tracker ?
- [x] Installer l'extension Claude Code dans VS Code
- [ ] Boss fight du niveau 0

**Délai :** fin de la première semaine en entreprise.

## Prochaine session : contexte

- **Titre de la prochaine session :** `[0.2] Le transfert : laptop et 6e candidat`
- **Mission suivante : 0.2 "Le transfert"** (sur le laptop perso) : installer Python, Git et VS Code (avec l'extension Claude Code), `git clone` du repo, recréer le venv, ajouter un **6e candidat** dans `main.py` (à la main, données Transfermarkt 25/26 en club, titres alignés sur les clés du barème), commit, push, puis `git pull` sur le PC fixe. Question à trouver pendant la mission : les commandes pour générer et utiliser un `requirements.txt` (et est-il utile alors que le projet n'a encore aucune librairie ?). Si Yanis n'est pas sur le laptop : faire la théorie à la place.
- **État de `main.py` (étape 4 validée, commit `d1534ad`) :** classe `Joueur` (`score()`, `affiche_joueur()`), `BAREME_TITRES` et `BAREME_PERFORMANCES` en haut du fichier, `classement()` qui trie sur place et affiche. Formule : 1,2 × buts + passes + points des titres. Classement : Yamal 111,8 / Kane 99,2 / Dembélé 93 / Kvara 91,8 / Mbappé 57,4.
- **Échauffement (session 0.2) :** `list[Joueur]` corrigé ✅. `.get()` sur une clé absente vs `[]` testé dans le terminal ✅ (`None` puis erreur au `+=`, ou erreur tout de suite). Reste à lui faire dire : qui exploite les annotations (VS Code/Pylance, mypy), et laquelle des deux versions est préférable (« fail fast »).
- **Données :** source unique **Transfermarkt**, saison 25/26, **stats en club uniquement** (la sélection compte seulement via les titres). Titres issus des pages palmarès.
- **Puis :** théorie "Building effective agents", boss fight du niveau 0. Ensuite, niveau 1 en mode copilote : expliquer à Yanis comment se passe une mission dans ce mode.
- **Dette notée pour le niveau 3 (evals) :** le barème v0 (écarts arbitraires, place de la CAN, titulaire et remplaçant comptés pareil, les titres collectifs qui écrasent les stats), les stats en sélection ignorées (Mbappé a marqué 10 buts au Mondial). Le backtest dira ce qui aide.
- **Points fragiles de Yanis à surveiller :**
  - Annonce « tout est fait » alors que c'est partiel, et saute des questions : relire le fichier avant de valider.
  - Reprend une suggestion d'une autre IA (Gemini) sans savoir l'expliquer : demander d'où vient l'idée quand un élément dépasse son niveau. A même collé une réponse d'IA (« Voici comment lui expliquer... ») à une question de contrôle : exiger une reformulation avec ses mots, ou un test dans le terminal.
  - Réponses parfois approximatives ou trop « manuel » : lui demander de reformuler avec ses mots. Il y arrive quand on insiste.
  - Tuple : croit que `x = a,` crée un tuple avec une « valeur vide en second » (en réalité, un tuple d'un seul élément). À revérifier.
  - Confusion `.env` (secrets) / `.venv` (dossier du venv).
  - Lance des commandes sans vérifier ce qu'elles ciblent. Réflexes Linux dans PowerShell.
  - Mélange les rôles de Git et du venv.
  - Prouve parfois le mauvais point.
  - Messages de commit qui ne décrivent pas ce qui change (progrès : `d1534ad` est bien formulé).- **Points forts :** se débloque seul en lisant les messages d'erreur. Honnête quand on lui demande d'où vient une idée. Pose de bonnes questions de méthode (contrat, mémoire du projet).
- **Environnement :** Windows, PowerShell, Python 3.13.14 (Microsoft Store). Activer le venv avec `.\.venv\Scripts\Activate.ps1`. VS Code avec l'extension Claude Code et l'interpréteur du venv sélectionné. Utiliser le panneau Terminal de l'app, ou coller la sortie du terminal VS Code. Git : branche `main`, remote `origin` = github.com/YanisFr77/ballon-dor-tracker, authentification via Git Credential Manager. Identité : gmail en local pour ce repo, email de l'université en global.

## Historique des sessions

Résumé de 3 à 5 lignes par session. Le détail des anciennes sessions est dans `HISTORIQUE.md`, qui n'est pas lu au démarrage.

### 2026-10-23 : Orientation et venv (0.1 étapes 1-2)
- Cadre posé : objectif AI engineer, contrat prof/élève, rythme selon les mois.
- Venv réussi au 3e essai (l'argument de `venv` est le dossier du venv). Activation débloquée seul (`Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`). `.gitignore` racine OK.

### 2026-10-24 : Git, GitHub et extension VS Code (0.1 étape 3)
- `git init`, branche `main`, premier commit, push réussi via Git Credential Manager.
- Extension Claude Code installée. VS Code active le venv tout seul (preuve dans un nouveau terminal).
- Leçons : `.git` contient tout l'historique local ; Git cherche `.git` dans les dossiers parents, VS Code cherche `.venv` à la racine du dossier ouvert.

### 2026-10-24 : Recadrage, puis `main.py` (0.1 étape 4 validée ✅)
- **Décisions :** mode copilote à partir du niveau 1 (spec par Yanis, code par l'IA, relecture). Le projet devient un analyste foot multi-agents, l'Oracle Ballon d'Or sert de benchmark d'eval. Roadmap réécrite dans `CLAUDE.md`.
- `main.py` : la dataclass (venue de Gemini) a été remplacée par une classe écrite à la main. `self` et `__init__` sont compris. Il y a 5 candidats, des arguments nommés, et un barème des titres en v0 (CDM de Yamal vérifiée : l'Espagne a gagné le Mondial 2026).
- Score, tri avec `key=Joueur.score` (expliqué avec ses mots après un premier collage d'IA) et affichage : le classement attendu est obtenu. Données corrigées par Claude depuis Transfermarkt. Leçons : tri sur place, fonction passée sans parenthèses, conflit d'écriture quand deux agents modifient le même fichier.
- `PROGRESSION.md` compacté à la demande de Yanis : historique résumé, détail archivé dans `HISTORIQUE.md`.
