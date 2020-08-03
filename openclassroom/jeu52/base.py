# coding:utf-8

"""On créer une classe Carte et on remplit la liste jeu52cartes avec des instanciation
de cette classe.
Puis on renvoie la liste créer comme paramètre d'un classe représentant un jeu de carte
dans laquelle on va créer plusieurs méthode"""

enseignecarte = ["coeur", "pique", "carreau", "trèfle"]
valeurcarte = ["as", "roi", "dame", "valet", 10, 9, 8, 7, 6, 5, 4, 3, 2]
jeu52cartes = []

class Carte():
    
    def __init__(self, enseigne, valeur):

        self.enseigne = enseigne
        self.valeur = valeur

    def __str__(self):
        return f"{self.valeur} de {self.enseigne}"

class Jeu52():

    def __init__(self, deck):
        self.deck = deck

    def __str__(self):
        """a coder pour afficher le contenu du deck"""

for i in enseignecarte:
    for j in valeurcarte:
        carte = Carte(i,j)
        jeu52cartes.append(carte)

deck = Jeu52(jeu52cartes)

