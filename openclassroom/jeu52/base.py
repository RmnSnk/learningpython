# coding:utf-8

"""On créer une classe Carte et on remplit la liste jeu52cartes avec des instanciation
de cette classe.
Puis on renvoie la liste créer comme paramètre d'un classe représentant un jeu de carte
dans laquelle on va créer plusieurs méthode"""

from random import *

DICTCOULEUR = {"trèfle" : "noir", "pique" : "noir", "coeur" : "rouge", "carreau" : "rouge"}

class Carte():
    

    def __init__(self, enseigne, valeur):

        self.enseigne = enseigne
        self.valeur = valeur

    @property
    def couleur(self):
        return DICTCOULEUR[self.enseigne]

    def __str__(self):
        return f"{self.valeur} de {self.enseigne}"

    def __repr__(self):
        return f"valeur = '{self.valeur}', enseigne = '{self.enseigne}"

class Jeu52():
   
    def __init__(self):
        self.listcarte = [] # le jeu de 52 carte, contient 52 objets Carte
        enseignecarte = ["coeur", "pique", "carreau", "trèfle"]
        valeurcarte = ["as", "roi", "dame", "valet", 10, 9, 8, 7, 6, 5, 4, 3, 2]

        for i in enseignecarte:
            for j in valeurcarte:
                self.listcarte.append(Carte(i,j))

    def __str__(self):
        strlistcarte = [] # Contient les 52 str(Carte)
        for i in self.listcarte:
            strlistcarte.append(str(i))
        return str(strlistcarte)
    
    def __len__(self):
        return len(self.listcarte)

    def melanger(self):
        shuffle(self.listcarte)
    
    def __contains__(self, carte):
        return carte in self.listcarte

    def __iter__(self):
        return Iterpique(self) # l'itérateur est une classe

    def piocher(self):
        shuffle(self.listcarte)
        try: 
            carte = self.listcarte[0]
            del self.listcarte[0]
        except IndexError:
            print("Il n'y a plus de carte")
        return carte


class Iterpique:

    def __init__(self,jeu):
        """On passe 2 attributs : la liste à parcourir et la position de départ"""
        self.jeu = jeu.listcarte 
        self.position = -1

    def __next__(self):
        if self.position == len(self.jeu)-1:
            raise StopIteration
        
        self.position += 1

        if self.jeu[self.position].enseigne == "pique":
            return self.jeu[self.position]
    

jeu = Jeu52()
jeu.melanger()

for carte in jeu:
    if carte != None: # L'itérateur renvoie tourjours une valeur, même "None", on trie après le passage 
        print(carte)
