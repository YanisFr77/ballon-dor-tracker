# Journal de bord

## Niveau actuel : 0 (Le vestiaire)

### Missions du niveau 0
- [x] 0.1 étape 1 : créer le dossier `ballon-dor-tracker`
- [x] 0.1 étape 2 : environnement virtuel Python (venv), `.gitignore` racine (`.venv/` et `.env`)
- [x] 0.1 étape 3 : `git init`, repo GitHub public, premier push
- [x] 0.1 étape 4 : `main.py` qui classe 5 candidats au Ballon d'Or avec un score (sans code généré par l'IA). C'est en réalité l'édition **2026** (saison 25/26 plus la CDM), et non 2027 comme prévu au départ.
- [x] 0.2 "Le transfert" : installer Python, VS Code et Git sur le laptop perso, cloner, ajouter un 6e candidat, push, puis pull sur le PC fixe
- [ ] 0.3 "Le verdict" (**à partir du 26 octobre 2026**, date de la cérémonie) : comparer le classement de `main.py` au vrai résultat. C'est la première eval du projet : combien de joueurs du podium ont été trouvés ? Quels joueurs du top 10 réel manquent dans les candidats ? Qu'est-ce que le barème v0 a raté ?
- [ ] Théorie : lire "Building effective agents" (Anthropic) et répondre aux 3 questions
  1. Quelle différence entre un workflow et un agent ?
  2. Les agents no-code du boulot, c'est plutôt l'un ou l'autre ?
  3. Un pattern de l'article utile pour le Tracker ?
- [x] Installer l'extension Claude Code dans VS Code
- [ ] Boss fight du niveau 0

**Délai :** fin de la première semaine en entreprise.

## Prochaine session : contexte

- **Titre de la prochaine session :** `[0.3] Le verdict du Ballon d'Or 2026` à partir du 26/10, sinon `[0.T] Théorie : Building effective agents`.
- **Mission suivante :** à partir du 26 octobre, **0.3 "Le verdict"** en priorité (une session courte : Yanis cherche le résultat officiel et le compare au classement de `main.py`, sans modifier le barème). Avant cette date, ou en mode téléphone : **la théorie** (lire "Building effective agents" et répondre aux 3 questions). Ensuite, le boss fight du niveau 0, puis le niveau 1 en mode copilote (expliquer d'abord comment se passe une mission dans ce mode).
- **Roadmap revue le 2026-10-24** (détail dans `CLAUDE.md`, section « Points de vigilance ») : une page Streamlit dès le niveau 2 (tranche verticale), la contamination du backtest à traiter au niveau 3 (joueurs anonymisés, top 30 de chaque édition), une source de données à choisir au niveau 1 (Transfermarkt n'a pas d'API), et trois briques ajoutées : pytest, Pydantic, Docker.
- **Échauffement de la prochaine session de code (1 question max) :** la ligne 54 utilise toujours `BAREME_PERFORMANCES.get(...)`. Yanis a dit vouloir des crochets (fail fast), mais ne l'a pas fait. Question de la 0.2 restée ouverte, à poser au moment où on installe la première librairie : générer et utiliser un `requirements.txt`.
- **État de `main.py` (commit `72cbf33`) :** classe `Joueur` (`score()`, `affiche_joueur()`), `BAREME_TITRES` (accès en `[t]`) et `BAREME_PERFORMANCES` en haut du fichier, `classement(joueurs: list[Joueur])` qui trie sur place et affiche. Formule : 1,2 × buts + passes + points des titres. Classement : Yamal 111,8 / Kane 99,2 / Dembélé 93 / Kvara 91,8 / Pedri 79,4 / Mbappé 57,4.
- **Deux machines :** le PC fixe et le laptop sont opérationnels (le laptop a Python 3.13.7, Git 2.53, VS Code 1.140, et le compte GitHub YanisFr77 enregistré). Une session Claude vit sur une seule machine : pour changer de machine, push de `PROGRESSION.md`, pull, nouvelle session, puis « on reprend ».
- **`aide_memoire.md` :** créé à la demande de Yanis, à compléter au fil des missions (règle dans `CLAUDE.md`).
- **Données du niveau 0 :** saisie manuelle depuis **Transfermarkt**, saison 25/26, **stats en club uniquement** (la sélection compte seulement via les titres). Titres issus des pages palmarès. À partir du niveau 1, il faudra une source qui ait une API (à choisir).
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
  - Messages de commit irréguliers : `d1534ad` et `72cbf33` sont bien formulés, `2714001` non.
  - Annotations : a cru que l'interpréteur les exploite (ce sont l'éditeur et mypy qui s'en servent).
  - Perd patience quand les questions s'empilent (règle ajoutée dans `CLAUDE.md` : 1 ou 2 questions par message, seulement celles qui bloquent).
- **Points forts :** se débloque seul en lisant les messages d'erreur. Honnête quand on lui demande d'où vient une idée. Pose de bonnes questions de méthode (contrat, mémoire du projet, aide-mémoire). Teste dans le terminal quand on le lui demande. Bon pronostic de classement.
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

### 2026-10-24 : Le transfert (0.2 validée ✅)
- Échauffement : `list[Joueur]` corrigé, `.get()` contre `[]` testé dans le terminal, principe du fail fast compris, `BAREME_TITRES[t]` adopté.
- Laptop : repo cloné (leçon : `git clone` crée lui-même le dossier), identité gmail en local, venv recréé. Le push est d'abord refusé à cause du compte de la fac (`yanis-saclay`) enregistré dans le Credential Manager, puis corrigé. Leçon : l'identité et l'authentification sont deux choses différentes.
- Pedri ajouté en 6e candidat (commit `72cbf33`), 5e avec 79,4 pts. La boucle laptop → GitHub → PC fixe fonctionne.
- `aide_memoire.md` créé. Nouvelle règle dans `CLAUDE.md` : 1 ou 2 questions par message au maximum.
- Revue globale du projet à la demande de Yanis. 4 propositions intégrées dans `CLAUDE.md` : tranche verticale (Streamlit dès le niveau 2), contamination du backtest et top 30, choix d'une source de données avec API, et ajout de pytest, Pydantic et Docker. Découverte : `main.py` prédit en fait l'édition **2026**, dont la cérémonie a lieu le 26/10, d'où la mission 0.3 « Le verdict ».
