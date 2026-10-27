# Vision produit

**Statut : idées de Yanis (2026-10-25), pas encore décidées.** Une idée n'entre dans la roadmap de `CLAUDE.md` qu'une fois décidée. Ce fichier n'est pas lu au démarrage : il sert à la revue globale de fin de niveau.

## Les idées de Yanis

- **Pronostics gratuits** avec des cotes, pour le divertissement : on gagne des points selon ses résultats, jamais d'argent réel.
- **Les points se gagnent** avec les pronostics et avec les objectifs de la simulation de carrière.
- **Les points se dépensent** pour acheter des joueurs, monter une équipe et affronter ses amis en 5 contre 5.
- **Simulation de carrière** : l'IA génère des choix (un choix par saison) et des objectifs (30 buts, le Ballon d'Or) qui rapportent des points.
- **Premium** : l'IA multi-agents propose le meilleur pronostic pour les matchs du lendemain. Achat de points possible.
- **Communautés** par club ou par pays (par exemple « FC Barcelone France »), chat pendant les matchs, scores en direct.
- **Contrainte : halal.** C'est du divertissement, pas un jeu d'argent.

## Revue de Claude (2026-10-25)

| Idée | Utile pour apprendre l'AI engineering ? | Coût hors IA | Verdict |
|---|---|---|---|
| Pronostics de match, ligue entre amis (« Bats l'Oracle ») | **Oui, beaucoup** : voir plus bas | des comptes utilisateurs | **Candidat n°1 pour la finalité** |
| Simulation de carrière | Oui : génération, sorties structurées, état et mémoire de la partie, cohérence des stats | moyen | Extension après le niveau 7, avec le scout |
| Équipe en 5 contre 5 | Faible : un moteur de match, c'est du game design | équilibrage, multijoueur | Backlog |
| Premium « meilleur pronostic » | Oui pour l'IA, mais le produit pose problème | paiement, juridique | À repenser |
| Achat de points | Non | paiement, juridique | Déconseillé |
| Communautés, chat, scores en direct | Non (à part la modération par un LLM) | temps réel, modération, données live payantes | Hors projet |

**Pourquoi les pronostics de match sont un excellent choix.** Ils résolvent deux points de vigilance de `CLAUDE.md` :
- **Taille du jeu d'eval** : un Ballon d'Or par an contre des centaines de matchs par semaine. La vérité terrain arrive tous les week-ends.
- **Contamination** : un match qui n'est pas encore joué ne peut pas être dans la mémoire du LLM. Une prédiction en direct ne triche pas.
- **Baseline toute trouvée** : les cotes des bookmakers donnent des probabilités. Question d'eval honnête : est-ce que l'IA fait mieux que les cotes ? Métriques : Brier score, log loss, calibration.
- **Données** : piste à vérifier au niveau 1, football-data.co.uk (résultats et cotes historiques en CSV, gratuits).

**Points de vigilance :**
1. **Dispersion.** Sept fonctionnalités, c'est le scope d'une startup avec une équipe. Le but reste d'apprendre l'AI engineering : une app qui fait **une** chose bien, mesurée et déployée vaut plus, en entretien, que dix fonctionnalités à moitié finies.
2. **Halal et légal.** Des points gagnés gratuitement, sans valeur en argent et non convertibles, restent du divertissement. Des points **achetés puis misés** se rapprochent d'une mise avec espoir de gain, sur le plan religieux (c'est à Yanis d'en juger) comme sur le plan juridique (en France, l'ANJ encadre les jeux d'argent ; à faire vérifier avant toute monétisation).
3. **Le premium « meilleur pronostic ».** Il sert surtout à des gens qui parient de l'argent réel ailleurs : c'est en tension avec la contrainte halal. Et battre les cotes des bookmakers est très difficile : l'eval risque de montrer que l'IA ne fait pas mieux. C'est une très bonne leçon d'eval, mais un mauvais argument de vente.
4. **Technos.** DuckDB, Streamlit, LangGraph, le RAG et MCP couvrent l'Analyste, l'Oracle et les pronostics. En revanche, des comptes, des points et une ligue entre amis demandent une base transactionnelle (PostgreSQL ; DuckDB est fait pour l'analyse, pas pour plusieurs utilisateurs qui écrivent en même temps) et sans doute un vrai backend (FastAPI). Le chat et le live demandent du temps réel (WebSockets) : Streamlit n'est pas fait pour ça. À décider au niveau 7, pas avant.

## Apprendre et faire une app : les deux, en couches (2026-10-25)

Yanis : « Un Ballon d'Or, c'est une fois par an, je veux une app que les gens utilisent. » Réponse : rien n'est impossible, la vraie limite, c'est le temps (environ 4 à 5 h par semaine). On garde donc tout, mais en couches, et chaque couche doit apprendre une brique d'AI engineering ou rester minimale.

| Couche | Fréquence d'usage | Ce que ça apprend | Quand |
|---|---|---|---|
| Analyste (chat avec sources) | à tout moment | agents, RAG, critique | niveaux 2 à 6 |
| Oracle : la course au Ballon d'Or, mise à jour chaque semaine | chaque semaine | evals, backtest | niveaux 2 et 3 |
| Pronostics de match + l'IA qui pronostique, comparée aux cotes | chaque journée de championnat | evals sur un gros volume, calibration | à partir du niveau 3 |
| Ligues privées entre amis (classement des points) | chaque journée | comptes, PostgreSQL | niveau 7 |
| Communauté : un serveur Discord plutôt qu'un chat fait maison (déjà sur la branche n8n) | en continu | automatisation | branche n8n |
| Équipe en 5 contre 5 avec les points, matchs commentés par un LLM | chaque semaine | génération, sorties structurées | après le niveau 7 |
| Simulation de carrière | à volonté | état, mémoire | après le niveau 7 |

Ligne rouge : **jamais d'achat de points**. Les cotes servent de données, jamais de mise.

## Décision : la monétisation (Yanis, 2026-10-25)

- **Aucun achat de points, sous aucune forme** (non licite, non halal). Seul achat possible : un **abonnement premium**.
- **Garde-fou proposé par Claude, à valider :** le premium ne doit rapporter **aucun point de plus**, sinon c'est un achat de points déguisé (payer, gagner plus de points, acheter de meilleurs joueurs). Les deux exemples de Yanis sont donc à revoir :
  - « Jouer plusieurs fois d'affilée » : si ça donne plus de chances de gagner des points, c'est payer pour des points.
  - « L'IA m'aide à faire mes pronostics » : dans une ligue entre amis, c'est du pay-to-win. Piste : le pronostic de l'Oracle n'est révélé qu'après la clôture des pronostics, et le jeu reste « Bats l'Oracle ».
- **Pistes premium sans avantage en points :** l'Analyste en illimité, le scout, les explications détaillées de l'Oracle, plus de parties en simulation de carrière à condition qu'elles ne rapportent pas de points, des stats perso sur ses propres pronostics.

## Ambition business (Yanis, 2026-10-25)

Yanis : une app viable, qui peut rapporter de l'argent et qui se différencie, le motiverait à aller plus vite. Revue de Claude :

- **La motivation, c'est un vrai atout, mais elle ne crée pas d'heures** : l'agenda de `CLAUDE.md` reste la base du planning. Si le rythme augmente, tant mieux, mais le plan doit tenir sans ça.
- **La concurrence existe déjà** : MPG (Mon Petit Gazon) pour le fantasy entre amis, Sorare, SofaScore et FotMob pour les scores en direct et les communautés, plus des applis de pronostics entre amis. Une app « points + équipe + chat » arrive sur un marché où d'autres ont une équipe entière.
- **Différenciation possible**, à confirmer :
  1. **Une IA qui pronostique avec un bilan public mesuré** : on affiche sa précision réelle, ses sources, et un agent critique bloque les stats inventées. C'est le cœur du projet (« rigueur visible »).
  2. **Des pronostics sans argent, assumés comme tels**, ce qui peut intéresser les fans qui refusent les paris (à vérifier : la taille de ce public est une hypothèse).
- **Valider la demande tôt, comme une eval** : dès que la ligue de pronostics tourne en version minimale (Streamlit ou Discord), la tester avec 5 à 10 amis et mesurer s'ils reviennent chaque semaine (la rétention). On ne construit l'équipe en 5 contre 5 que si cette métrique est bonne.
- **Le coût de l'IA par utilisateur** : chaque question à l'Analyste coûte des tokens. Le premium devra couvrir ce coût, d'où des sujets d'AI engineering à part entière : choix du modèle, cache, limites de la version gratuite.
- **Avant de toucher de l'argent** (plus tard) : statut (micro-entreprise), CGU, RGPD, paiement.

## Idée 2 : l'IA d'entraîneur (Yanis, 2026-10-27)

L'idée : l'IA connaît ton effectif et celui de tes adversaires, analyse leur tactique et leur forme, puis recommande la tactique, la compo et le temps de jeu, et alerte sur les risques de blessure.

**Revue de Claude :**
- **Version clubs pros : non.** Le marché est déjà pris (StatsBomb/Hudl, Opta/Stats Perform, Wyscout, SkillCorner pour la tactique ; Catapult, Kitman Labs pour la charge et les blessures), et les clubs ont leurs propres data scientists. Surtout, l'analyse tactique sérieuse demande des **données de tracking** (la position des 22 joueurs à chaque instant), qui sont privées et coûtent très cher.
- **Prédiction des blessures : non.** Elle demande des données médicales et d'entraînement (GPS, charge), qui sont privées et **sensibles** (données de santé, très encadrées par le RGPD). Même avec ces données, la science reste fragile. Au mieux, une « alerte de charge » (minutes jouées, matchs rapprochés), jamais une prédiction médicale.
- **Pas de vérité terrain** : « la meilleure tactique » ne se mesure pas (on ne rejoue pas le match avec une autre tactique). C'est un gros handicap pour un projet dont la valeur est l'eval.
- **Le filon caché : les entraîneurs amateurs.** Des milliers de clubs, des coachs bénévoles, aucun staff data. Un assistant qui gère les présences, propose une compo, **équilibre le temps de jeu** (un vrai sujet chez les jeunes), prépare des séances (RAG sur des contenus pédagogiques) et rédige le compte-rendu du match à partir d'une note vocale. Les données viennent du coach lui-même, donc pas de problème de source. Usage chaque semaine, utilisateurs faciles à trouver, et un premium qui a du sens (abonnement par club). Limite : on s'éloigne du Ballon d'Or et des stats pros.
- **Recyclage côté fans :** le « rapport d'avant-match » (forme, style, joueurs clés, avec des sources) peut devenir l'explication du pronostic de l'Oracle dans « Bats l'Oracle ».

## Idée 3 : « L'arbitre des débats » (Claude, 2026-10-27)

Entre potes, sur WhatsApp ou Discord : « Mbappé a marqué plus que Haaland en LDC depuis 2020 ! » L'app **tranche le débat** avec les stats sourcées, signale les affirmations fausses et donne le verdict, avec un peu de chambrage.

- C'est **l'agent critique devenu produit** : la brique centrale du projet (anti-stats inventées) devient la fonctionnalité visible.
- **Eval idéale** : des affirmations étiquetées vraies ou fausses, donc une vérité terrain facile à construire, et à volonté.
- **Social et viral par nature** (un bot Discord via n8n, puis l'app), divertissant, halal, et utile toute l'année.
- **Technos couvertes** : agent stats (SQL sur DuckDB), RAG, critique, MCP, evals. C'est le cœur de la roadmap, sans rien ajouter.
- Ça se marie bien avec « Bats l'Oracle » : une même app de divertissement foot dont l'IA **ne ment jamais sur les chiffres**.

## Ce qui ne change pas, quel que soit le choix

Les niveaux 1 à 3 (données, LLM, evals) sont les mêmes pour toutes les idées : rien ne presse pour décider. Seule contrainte dès le niveau 1 : une source avec des **données par match** (date, adversaire, minutes, buts), pas seulement des totaux de saison. Toutes les idées en ont besoin.

## Proposition (à décider par Yanis)

- **Finalité de l'app** : l'Analyste, l'Oracle Ballon d'Or et une **ligue de pronostics entre amis, gratuite, où chacun essaie de battre l'Oracle**. Les points servent au classement et au chambrage, pas à l'argent.
- **Extensions après le niveau 7** : le scout/mercato, puis la simulation de carrière.
- **Backlog, sans engagement** : l'équipe en 5 contre 5, les communautés, le chat, les scores en direct.
- **Monétisation** : pas avant d'avoir des utilisateurs. Si elle arrive un jour, un abonnement aux fonctions d'analyse (questions illimitées à l'Analyste, le scout), jamais des points à miser.
