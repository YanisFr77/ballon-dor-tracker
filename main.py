from dataclasses import dataclass

@dataclass
class Joueur:
    nom: str
    club: str
    buts: int
    passes_D : int
    prix_moyen: float = 0.0


j = Joueur("Lamine Yamal", "FC Barcelona", 18, 20, 150.0)
print(j)