# Journal de bord

## Niveau actuel : 1-2 (Premier contact LLM, puis les stats). Niveau 0 gagné le 2026-10-29 🏆

La finalité : `FINALITE.md`. Les règles et la roadmap : `CLAUDE.md`.

### Niveau 0 (terminé)
`main.py` écrit à la main (7 candidats, formule 1,2 × buts + passes + titres), deux machines synchronisées par GitHub, vérité terrain 2026 dans `donnees/`, première métrique d'eval (somme des écarts = 12), théorie « Building effective agents », boss fight gagné à la 2e revanche. Détail dans `HISTORIQUE.md`.

### Missions des niveaux 1-2 (durée fixe : 5 semaines, fin visée le 2026-12-21)
- [ ] **2.0 Premier appel LLM : Oracle v0.5** (zone noyau). Script `prediction_llm.py` : il envoie les stats des candidats de `main.py` à un LLM, récupère un classement en sortie structurée (Pydantic) et le mesure avec `verdict()`, comme la baseline (écart 12). **Le script tourne. Reste : finir la relecture par Yanis, remettre `main.py` à 7 candidats, commit.**
  - Spec validée : en entrée nom, club, buts, passes, titres ; jamais `RANG_REEL`, ni le score de la formule, ni le barème ; en sortie les 7 classés avec une phrase de justification.
  - **Résultats du 2026-11-16** (`gemini-3.5-flash-lite`, 1 appel chacun) : sonde de contamination propre (le modèle s'arrête à mars 2026, ne connaît pas le vainqueur). Essai 1 : réponse refusée par `verifier()` (club collé au nom, prompt ambigu), écart 18 relu à la main. Essai 2, prompt clarifié : **écart 8, contre 12 pour la baseline**. 18 puis 8 montre surtout la variance, pas une victoire : à mesurer sur plusieurs appels au niveau 3.
- [x] 1.1 Source de données : **API-Football retenu** (football-data.org éliminé : pas de stats par joueur en gratuit). Premier appel réussi (`essai_api.py`) : le gratuit couvre les saisons 2022 à 2024, 100 requêtes par jour. Saison 25/26 : un mois du plan Pro au moment du backtest (décidé le 2026-11-16).
- [ ] 1.2 Ingestion API-Football → DuckDB (zone plomberie) : stats par match d'un joueur, puis des 30 nommés d'une édition. **Les données sont dynamiques (rappel de Yanis, 2026-11-16)** : l'ingestion doit pouvoir être relancée pour rafraîchir les stats, et chaque prédiction porte la date de ses données. L'automatisation (chaque semaine) arrive avec n8n ou Cloud Scheduler.
- [ ] 1.3 Tests pytest sur l'ingestion (ce qui entre, ce qui sort).
- [ ] 2.1 Oracle v1 : le LLM classe les 30 nommés d'une édition à partir de DuckDB.
- [ ] 2.2 Première page Streamlit qui affiche l'Oracle v1.
- [ ] Revue globale, puis boss fight des niveaux 1-2.

## Prochaine session : contexte

- **Titre de la prochaine session :** `[2.0] Fin de la relecture de prediction_llm.py`.
- **Où on s'est arrêtés (2026-11-16 au soir) :** `prediction_llm.py` tourne, résultats notés ci-dessus. On était en pleine **relecture (zone noyau)**. Yanis a commité l'essentiel lui-même (`f9c89ac`, « reprise + premier llm », avec `adam` dedans). Restent à commiter : ce passage de relais dans `PROGRESSION.md` et `.gitignore` (`__pycache__/` ajouté).
- **Première chose à faire : `main.py` contient un 8e joueur de test, `adam`** (ajouté par Yanis en fin de session, sans doute pour voir l'empreinte changer). Il n'est pas dans `RANG_REEL` : `python main.py` et `prediction_llm.py` plantent sur `KeyError: 'adam'` dans `verdict()`. Lui demander ce qu'il a observé (un 4e appel est parti à 21h19, nouveau fichier dans `cache_llm/`), valider l'expérience, puis **lui faire retirer `adam`** et vérifier que `python main.py` affiche 12. Ne pas le retirer à sa place sans lui en parler.
- **Relecture, état :**
  - Validé : pourquoi le tri alphabétique dans `construire_prompt` (l'ordre de la liste soufflerait notre classement) ; le LLM ne génère que le classement et les justifications, les écarts viennent de `verdict()`.
  - Expliqué, à faire reformuler : le texte entre `"""` n'est pas envoyé au LLM, seul le texte du `return` l'est (le prompt = ce qui s'affiche dans le terminal) ; on envoie un texte, pas la fonction ; `empreinte` = code de 16 caractères calculé sur modèle + prompt + schéma, qui sert de nom de fichier de cache.
  - **Question en attente :** « si tu changes un seul mot du prompt et que tu relances, que se passe-t-il, et pourquoi ? » (réponse attendue : nouvelle empreinte, pas de fichier de cache, donc un nouvel appel).
  - Pas encore relus : les classes Pydantic `Ligne` et `Classement`, `verifier()`, le bloc `par_nom` / `ordre_llm`. Une ou deux questions, pas plus.
- **Ensuite :** cocher la 2.0, commit et push (message proposé : « 2.0 : premier appel LLM (prediction_llm.py), règle Budget LLM »), puis mission 1.2 (ingestion API-Football → DuckDB, zone plomberie). Option courte avant la 1.2 : verrouiller les 7 noms dans le schéma (enum), proposé à Yanis et remis à plus tard.
- **Comment marche `prediction_llm.py` :** `construire_prompt()` (fiches `Nom : … | Club : … | Buts : …`, tri alphabétique) ; `appeler_llm(prompt, schema)` (cache dans `cache_llm/`, confirmation `o/n` avant chaque appel, tokens affichés, journal `journal_llm.jsonl`) ; `verifier()` (les 7 noms exacts, sinon `ValueError`) ; une sonde de contamination en premier (« Qui a remporté le Ballon d'Or 2026 ? »). Modèle : constante `MODELE`.
- **Fournisseur LLM : Gemini gratuit** (décidé le 2026-11-16, clé `GEMINI_API_KEY` dans `.env`). SDK `google-genai` 3.3.0 : `client.interactions.create(model=, input=, response_format={"type": "text", "mime_type": "application/json", "schema": ...})`, réponse dans `.output_text`, tokens dans `.usage.total_input_tokens` / `total_output_tokens`. Modèles gratuits : `gemini-3.5-flash-lite` (mise au point), `gemini-4-hydrogen` (mesure à garder). Sur l'offre gratuite, les prompts servent à améliorer les produits de Google : jamais de donnée personnelle. Les 5 $ Anthropic attendront la comparaison de modèles (niveau 3) ; ce jour-là, charger la skill `claude-api`.
- **Budget LLM :** règle dans `CLAUDE.md`, section « Budget LLM ». Claude annonce chaque appel (nombre, modèle, coût) et c'est Yanis qui lance le script dans son terminal.
- **État de `main.py` :** classe `Joueur`, `BAREME_TITRES`, `RANG_REEL` (7 candidats), `classement()` trie sur place, `verdict()` affiche les écarts et renvoie leur somme (12 avec les 7). Les trois dernières lignes sont sous `if __name__ == "__main__":` pour pouvoir importer sans tout relancer.
- **`essai_api.py` :** commité, pas encore relu par Yanis. Zone plomberie : il doit savoir dire ce qui entre et ce qui sort.
- **Dette notée pour le niveau 3 (evals) :** répéter les appels et faire la moyenne (variance 18 puis 8) ; le barème v0 ; les stats en sélection ignorées ; partir des **30 nommés** ; ne comparer que des rangs pris sur le même ensemble ; le critère « décisif et impressionnant » absent ; chaque juré vote pour un top 10 ; contamination partielle possible (Gemini connaît la saison jusqu'en mars 2026) : parade des joueurs anonymisés.
- **Points fragiles de Yanis (5 au plus) :**
  1. Annonce « tout est fait » alors que c'est partiel : lui faire répondre à chaque partie.
  2. En zone noyau, confond vite ce qui est du code, du commentaire et du prompt : faire reformuler avec ses mots, ou montrer dans le terminal.
  3. Sature vite sur la spec et sur les questions empilées, et perd le fil après une pause : rappeler en une phrase à quoi sert le fichier, 1 ou 2 questions par message, puis du concret.
  4. A modifié l'ensemble évalué après avoir vu le résultat (Olise, puis `adam` en test) : à surveiller de près au niveau 3.
  5. Une nouvelle idée de produit : une ligne au parking de `VISION.md`, puis retour à la mission.
- **Points forts :** a repéré seul la contamination avant le premier appel, et demandé seul une règle de budget. Pose les bonnes questions (« qui calcule les écarts ? », « tu me recommandes ça parce que tu es Claude ? »). Se débloque seul en lisant les erreurs. Expérimente dans le terminal.
- **Deux machines :** PC fixe et laptop. Une session Claude vit sur une seule machine : push, pull, nouvelle session, puis « on reprend ». La clé Gemini est dans le `.env` du **PC fixe** seulement : à recopier sur le laptop.
- **Environnement :** Windows, PowerShell, Python 3.13. Venv : `.\.venv\Scripts\Activate.ps1`. Sur une autre machine : `pip install -r requirements.txt`. Git : branche `main`, remote `origin` = github.com/YanisFr77/ballon-dor-tracker.
- **Écoute en voiture :** `podcasts.md`.

## Révisions

Une question flash au « on reprend » sur une notion dont la date est passée (règle dans `CLAUDE.md`). Réussie : J+7, puis J+21, puis la notion sort. Oubliée : J+2. Cinq notions au plus, d'AI engineering seulement.

| Notion | Prochaine révision |
|---|---|
| Workflow contre agent (qui choisit le chemin ?) | 2026-11-16 |
| Les 5 patterns de « Building effective agents » (noms + quand les utiliser) | 2026-11-16 |
| Contamination par la mémoire du LLM, et ses parades | 2026-11-23 (réussie le 16/11 : repérée seul avant le premier appel) |
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

### 2026-11-16 (soir) : Premier appel LLM (2.0, presque finie)
- Gemini gratuit choisi après une question franche de Yanis sur le biais de Claude. Règle « Budget LLM » ajoutée à `CLAUDE.md`.
- `prediction_llm.py` : sonde de contamination propre, essai 1 refusé (prompt ambigu, écart 18), essai 2 à 8 contre 12 pour la baseline. Leçon : un appel n'est pas une mesure.
- Relecture commencée, pas finie. `main.py` laissé avec un joueur de test (`adam`) à retirer. Commit `f9c89ac` par Yanis.
