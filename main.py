BAREME_TITRES = {
    # 1. Trophées suprêmes
    "CDM": 50,
    "LDC": 35,

    # 2. Championnats domestiques (Top 5)
    "Premier League": 15,
    "La Liga": 12,
    "Serie A": 12,
    "Bundesliga": 10,
    "Ligue 1": 10,

    # 3. Compétitions continentales secondaires
    "CAN": 10,
    "Europa League": 10,
    "Conference League": 5,

    # 4. Coupes nationales
    "FA Cup": 8,
    "Copa del Rey": 7,
    "Coupe d'Allemagne": 6,
    "Coupe de France": 6,
    "Coppa Italia": 6,
    "Carabao Cup": 4,

    # 5. Supercoupes et trophées de prestige courts
    "Coupe Intercontinentale": 5,
    "Supercoupe UEFA": 5,
    "Supercoupe d'Espagne": 3,
    "DFL-Supercup": 3,
    "Trophée des Champions": 3,
    "Supercoupe d'Italie": 3,
    "Community Shield": 2
}

BAREME_PERFORMANCES = {
    "but": 1.2,
    "passe_d": 1.0,

}
# Je dois faire un classement sur les 7 joueurs sélectionnés donc sur 7 et non 30. J'ai ajouté Olisé après le verdict. Pedri ne configure pas dans le top 30, donc il est dernier de notre classement
RANG_REEL = {
    "Lamine Yamal": 3,
    "Harry Kane": 1,
    "Ousmane Dembélé": 5,
    "Khvicha Kvaratskhelia": 4,
    "Kylian Mbappé": 2,
    "Michael Olisé":  6,
    "Pedri": 7
}

class Joueur:
    def __init__(self, nom: str, club: str, buts: int, passes_d: int,  titres_majeurs: list[str]):
        self.nom = nom
        self.club = club
        self.buts = buts
        self.passes_d = passes_d
        self.titres_majeurs = titres_majeurs  # ex: ["LDC", "Euro_Copa_CDM", "Championnat"]

    def affiche_joueur(self):
        print(f"Joueur(nom={self.nom}, club={self.club}, buts={self.buts}, passes_d={self.passes_d}, titres_remporte={self.titres_majeurs})")

    def score(self):
        score_performance = self.buts * BAREME_PERFORMANCES["but"] + self.passes_d * BAREME_PERFORMANCES["passe_d"]
        score_titres = 0
        for t in self.titres_majeurs:
            score_titres += BAREME_TITRES[t]
        return score_performance + score_titres

def classement(joueurs: list[Joueur]):
    joueurs.sort(key=Joueur.score, reverse=True)
    # for i in range (0, len(joueurs)):
        # print(f"{i+1}. {joueurs[i].nom} ({joueurs[i].club}) : {joueurs[i].score()} pts")
    return joueurs

def verdict(joueurs: list[Joueur]):
    ecarts = []
    for i in range (0 ,len(joueurs)):
        # rang prédit est simplement i car joueurs.sort(key=Joueur.score, reverse=True) trie le tableau joueur
        ecart = abs(RANG_REEL[joueurs[i].nom] - (i+1))
        ecarts.append(ecart)
        print(f"{joueurs[i].nom} : prédit {i+1}, réel {RANG_REEL[joueurs[i].nom]}, écart {ecart}")
    return sum(ecarts)


yamal = Joueur(nom="Lamine Yamal", club="FC Barcelona", buts=24, passes_d=18, titres_majeurs=["Supercoupe d'Espagne", "La Liga", "CDM"])
kane = Joueur(nom="Harry Kane", club="FC Bayern", buts=61, passes_d=7,titres_majeurs=["Bundesliga", "Coupe d'Allemagne", "DFL-Supercup"])
dembele = Joueur(nom="Ousmane Dembélé", club="Paris Saint-Germain", buts=20, passes_d=11, titres_majeurs=["Ligue 1", "LDC", "Supercoupe UEFA", "Coupe Intercontinentale", "Trophée des Champions"])
kvara = Joueur(nom="Khvicha Kvaratskhelia", club="Paris Saint-Germain", buts=19, passes_d=11, titres_majeurs=["Ligue 1", "LDC", "Supercoupe UEFA", "Coupe Intercontinentale", "Trophée des Champions"])
mbappe = Joueur(nom="Kylian Mbappé", club="Real Madrid", buts=42, passes_d=7, titres_majeurs=[])
pedri = Joueur(nom="Pedri", club="FC Barcelona", buts=2, passes_d=12, titres_majeurs=["Supercoupe d'Espagne", "La Liga", "CDM"])
olise = Joueur("Michael Olisé", "FC Bayern", 22, 26, ["Bundesliga", "Coupe d'Allemagne", "DFL-Supercup"] )

candidats = [yamal, kane, dembele, mbappe, kvara, olise, pedri]

classement(candidats)
s = verdict(candidats)
print(f"Première métrique d'eval 🎯 : {s}")