# ⚔️ Boss fight du niveau 0 : le défi « Le verdict en code »

**Sans IA, sans internet.** Le laptop dans le train, c'est parfait.

## Règles

- **Interdit :** Claude (l'extension VS Code reste fermée), Gemini, Copilot, internet.
- **Autorisé :** ton propre code, `aide_memoire.md`, les messages d'erreur de Python, et `help()` dans le terminal Python (exemple : `python`, puis `help(abs)`, puis `q` pour sortir). C'est la doc hors ligne.
- **Durée visée :** environ 1 h.
- **Avant de partir :** `git pull` (avec réseau !).

## La mission

Au niveau 0.3, tu as comparé ta prédiction au vrai classement à la main. Cette fois, c'est `main.py` qui rend le verdict.

### Étape 1 : la dette

Ligne 54 : remplace les deux `BAREME_PERFORMANCES.get(...)` par des crochets (fail fast).

### Étape 2 : le vrai classement

Crée un dictionnaire `RANG_REEL` en haut du fichier : pour chacun de tes 6 joueurs, son rang réel, à partir de `donnees/ballon_dor_2026_top30.csv`.

⚠️ Deux pièges, à régler toi-même avec un commentaire qui justifie ton choix :
1. Souviens-toi de la leçon du verdict : on ne compare que des rangs pris **sur le même ensemble de joueurs**.
2. Un de tes joueurs n'est pas dans le top 30.

### Étape 3 : la fonction `verdict`

Écris une fonction `verdict(joueurs: list[Joueur])`, appelée après `classement(candidats)`. Pour chaque joueur, dans l'ordre de ta prédiction, elle affiche une ligne comme celle-ci :

```
Lamine Yamal : prédit 1, réel ?, écart ?
```

L'écart est toujours positif ou nul (indice : une fonction de base de Python, à trouver avec `help()` ou dans ta mémoire). À la fin, elle affiche la **somme des écarts** : plus elle est petite, meilleure est la prédiction. C'est ta toute première métrique d'eval 🎯

### Étape 4 : le commit

Commit **dans le train, sans réseau**, avec un message qui décrit ce qui change. Tu pushes en arrivant.

## Conditions de victoire

1. `python main.py` affiche le classement, puis le verdict, sans erreur.
2. Les chiffres sont justes (je les vérifierai).
3. Tu sais expliquer chaque ligne que tu as écrite (je t'interrogerai sur une ligne au hasard).
4. Le message de commit est propre.

Au retour : pull sur la machine, puis « on reprend ».
