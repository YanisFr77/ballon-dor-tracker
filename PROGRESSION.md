# Journal de bord

## Niveau actuel : 1-2 (Premier contact LLM, puis les stats). Niveau 0 gagné le 2026-10-29 🏆

La finalité : `FINALITE.md`. Les règles et la roadmap : `CLAUDE.md`.

### Niveau 0 (terminé)
`main.py` écrit à la main (7 candidats, formule 1,2 × buts + passes + titres), deux machines synchronisées par GitHub, vérité terrain 2026 dans `donnees/`, première métrique d'eval (somme des écarts = 12), théorie « Building effective agents », boss fight gagné à la 2e revanche. Détail dans `HISTORIQUE.md`.

### Missions des niveaux 1-2 (durée fixe : 5 semaines, fin visée le 2026-12-21)
- [ ] **2.0 Premier appel LLM : Oracle v0.5** (zone noyau). Un script qui envoie les stats des 7 joueurs de `main.py` à Claude et récupère un podium en sortie structurée (Pydantic). On compare son classement à la baseline (`verdict()`, écart total 12).
- [x] 1.1 Source de données : **API-Football retenu** (football-data.org éliminé : pas de stats par joueur en gratuit). Premier appel réussi (`essai_api.py`) : le gratuit couvre les saisons 2022 à 2024, 100 requêtes par jour. Saison 25/26 : un mois du plan Pro au moment du backtest (décidé le 2026-11-16).
- [ ] 1.2 Ingestion API-Football → DuckDB (zone plomberie) : stats par match d'un joueur, puis des 30 nommés d'une édition. Avec `requirements.txt`.
- [ ] 1.3 Tests pytest sur l'ingestion (ce qui entre, ce qui sort).
- [ ] 2.1 Oracle v1 : le LLM classe les 30 nommés d'une édition à partir de DuckDB.
- [ ] 2.2 Première page Streamlit qui affiche l'Oracle v1.
- [ ] Revue globale, puis boss fight des niveaux 1-2.

## Prochaine session : contexte

- **Titre de la prochaine session :** `[2.0] Premier appel LLM : Oracle v0.5`.
- **Mission suivante : la 2.0, en zone noyau.** Démarrer par du concret, pas par de la théorie. Déroulé proposé :
  1. Yanis écrit la spec en 5 lignes (but, entrées, sorties, cas limites, critère de fini).
  2. Clé d'API : Yanis crée un compte sur la Console Anthropic et met 5 $ de crédit (son abonnement Claude ne donne pas accès à l'API, c'est une facturation à part). La clé va dans `.env` sous le nom `ANTHROPIC_API_KEY`. S'il préfère du gratuit pour commencer : une clé Gemini via Google AI Studio (sans carte bancaire), en sachant que le reste du parcours vise l'API Claude.
  3. Installer `anthropic` et `pydantic`, créer `requirements.txt`.
  4. Claude génère `oracle.py`, Yanis relit tout (zone noyau). **Avant d'écrire le code, Claude charge la skill `claude-api`** : l'API a changé (sorties structurées avec `client.messages.parse()`).
  5. Lancer, comparer au classement réel, noter l'écart à côté de celui de la baseline.
- **Piège à garder en tête pour la 2.0 :** `RANG_REEL` ne doit jamais partir dans le prompt (c'est la vérité terrain). Le Ballon d'Or 2026 est postérieur à la date de coupure des modèles actuels : bonne nouvelle pour l'honnêteté du test.
- **Choix du modèle :** à faire avec Yanis. Ordre de grandeur pour un appel de cette taille : environ 3 centimes avec Opus 5.5, moins d'un dixième de centime avec Haiku 5.5. 5 $ couvrent largement les niveaux 1-2.
- **État de `main.py` (commit `d74348a`) :** classe `Joueur` (`score()`, `affiche_joueur()`), `BAREME_TITRES` et `BAREME_PERFORMANCES`, `RANG_REEL` (rangs sur les 7 candidats), `classement()` qui trie sur place, `verdict()` qui affiche les écarts et renvoie leur somme (12). Classement : Yamal 111,8 / Kane 99,2 / Dembélé 93 / Kvara 91,8 / Pedri 79,4 / Mbappé 57,4.
- **`essai_api.py` :** commité, pas encore relu par Yanis. Zone plomberie : il doit savoir dire ce qui entre et ce qui sort, pas chaque ligne.
- **Acquis de la théorie :** workflow (le code fixe le chemin) contre agent (le LLM tourne en boucle avec des outils et choisit). Pour le projet : routing pour une question simple, orchestrator-workers quand les sous-tâches ne sont pas prévisibles.
- **Dette notée pour le niveau 3 (evals) :** le barème v0 (écarts arbitraires, titres collectifs qui écrasent les stats), les stats en sélection ignorées (Mbappé). Leçons du verdict : (1) partir des **30 nommés**, liste publiée avant le vote ; (2) ne comparer que des rangs pris sur le même ensemble de joueurs ; (3) le critère n°1, « décisif et impressionnant », est absent : pistes, les buts dans les gros matchs, la note moyenne par match, la presse via le RAG ; (4) chaque juré vote pour un top 10 (15, 12, 10, 8, 7, 5, 4, 3, 2, 1 points).
- **Points fragiles de Yanis (5 au plus) :**
  1. Annonce « tout est fait » alors que c'est partiel, et saute des sous-questions : relire le fichier avant de valider, lui faire répondre à chaque partie.
  2. Reprend une réponse d'une autre IA sans savoir l'expliquer : en zone noyau, exiger une reformulation avec ses mots ou un test dans le terminal.
  3. Sature vite sur la spec et sur les questions empilées : spec en 5 lignes, 1 ou 2 questions par message, puis du concret.
  4. A modifié l'ensemble évalué après avoir vu le résultat : à surveiller de près au niveau 3.
  5. Longue pause, puis une nouvelle idée de produit à la reprise : l'idée va au parking de `VISION.md`, et la session démarre par une mission courte.
- **Points forts :** se débloque seul en lisant les messages d'erreur. Honnête sur l'origine d'une idée. Bons réflexes d'eval (a repéré seul le biais des 6 candidats et la fuite de la vérité terrain). Défend ses choix avec de bons arguments.
- **Deux machines :** PC fixe et laptop opérationnels. Une session Claude vit sur une seule machine : pour changer, push, pull, nouvelle session, puis « on reprend ».
- **Environnement :** Windows, PowerShell, Python 3.13 (Microsoft Store). Activer le venv avec `.\.venv\Scripts\Activate.ps1`. Installés dans le venv : `requests`, `python-dotenv`. Git : branche `main`, remote `origin` = github.com/YanisFr77/ballon-dor-tracker, authentification via Git Credential Manager. Clé API-Football dans `.env` (`API_FOOTBALL_KEY`).
- **Écoute en voiture :** `podcasts.md`. Demander de temps en temps ce qu'il a retenu d'un trajet.

## Révisions

Une question flash au « on reprend » sur une notion dont la date est passée (règle dans `CLAUDE.md`). Réussie : J+7, puis J+21, puis la notion sort. Oubliée : J+2. Cinq notions au plus, d'AI engineering seulement.

| Notion | Prochaine révision |
|---|---|
| Workflow contre agent (qui choisit le chemin ?) | 2026-11-16 |
| Les 5 patterns de « Building effective agents » (noms + quand les utiliser) | 2026-11-16 |
| Contamination par la mémoire du LLM, et ses parades | 2026-11-16 |
| Eval honnête : ne jamais changer la prédiction après avoir vu la vérité terrain | 2026-11-16 |

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

### 2026-10-24/25 : Théorie et vision produit
- « Building effective agents », lu en français (traduction du navigateur, plus un lexique). Questions 1 et 2 validées après correction (« déterministe » trop fort, critère « code / no-code » faux). Notion de framework expliquée. Il reste la question 3.
- Aparté de Yanis sur la finalité de l'app (pronostics avec des points, équipe en 5 contre 5, simulation de carrière, premium, communautés), avec la contrainte halal. Revue complète dans `VISION.md` ; la décision reste à prendre.
- Nouvelle règle dans `CLAUDE.md` : une revue globale du projet à chaque fin de niveau.

### 2026-10-27 : Le verdict (0.3 validée ✅)
- Ballon d'Or 2026 : Kane, Mbappé, Yamal, Rodri, Messi. Podium trouvé 2/3. Top 30 officiel enregistré dans `donnees/`.
- Bonne analyse de Yanis : il a repéré seul le biais de sélection (6 candidats contre 30 nommés), et passé les 3 critères officiels en revue avec justesse. Correction : chaque juré vote pour un top 10, pas pour un top 30.

### 2026-10-27/28 : Théorie, question 3 (théorie validée ✅)
- D'abord « prompt chaining » pour décrire en fait un orchestrator-workers mélangé avec du routing. Puis un bon critère (des sous-tâches imprévisibles), mais un exemple à un seul worker.
- Validé avec « Kane ou Mbappé pour le Ballon d'Or ? » (stats + actu). Retenu : routing pour les questions simples, orchestrator-workers pour les complexes.

### 2026-10-29 : Boss fight du niveau 0 gagné (PC)
- Défi pas encore fait (rien de pushé). Revanche du quiz : 1,5/3, perdue. Les idées sont là, la précision manque : bonne réponse abandonnée (`git log`), routing confondu avec orchestrator-workers, parade qui vise la mauvaise fuite.
- Défi gagné après une correction (commit `d74348a`, total des écarts = 12). Leçon clé : Pedri remplacé par Olise après le verdict, c'est une fuite ; un joueur hors du top 30 a quand même un rang connu parmi les candidats (le dernier).
- Revanche n°2 du quiz : 3/3. **Niveau 0 gagné** 🏆. Suite : niveau 1, choix de la source de données.

### 2026-11-16 : Revue complète après 18 jours de pause
- Passe sur tout le projet à la demande de Yanis. Constat : socle sain, mais trop de cérémonie et le LLM arrivait trop tard.
- **Décisions validées par Yanis**, appliquées dans `CLAUDE.md` : contrat en deux zones (noyau et plomberie), niveaux 1-2 joués ensemble avec le LLM d'abord, durée fixe par niveau, suivi allégé, données 25/26 via un mois payant au moment du backtest.
- **Finalité tranchée : Analyste + Oracle**, écrite dans `FINALITE.md` (nouveau). `VISION.md` gelé jusqu'à la fin du niveau 3. Idée 4 (vidéos tactiques sur TikTok) : au parking, canal de sortie après le niveau 6.
- `podcasts.md` créé pour les trajets en voiture. Ce fichier a été allégé, le détail est archivé dans `HISTORIQUE.md`.
