# coding:utf-8

from random import *

"Petit script de test de class"

class Carte():
    
    enseignecarte = ["coeur", "pique", "carreau", "trèfle"]
    valeurcarte = ["as", "roi", "dame", "valet", 10, 9, 8, 7, 6, 5, 4, 3, 2]

    def __init__(self):
        enseignecarte = ["coeur", "pique", "carreau", "trèfle"]
        valeurcarte = ["as", "roi", "dame", "valet", 10, 9, 8, 7, 6, 5, 4, 3, 2]

        self.enseigne = choice(enseignecarte)
        self.valeur = choice(valeurcarte)

    def __str__(self):
        return f"{self.valeur} de {self.enseigne}"

i = 0
while i < 11:
    carte1 = Carte()
    print(carte1)
    i += 1

