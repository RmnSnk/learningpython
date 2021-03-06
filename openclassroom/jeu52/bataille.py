# coding:utf-8

"""On créer une classe Carte et on remplit la liste jeu52cartes avec des instanciation
de cette classe.
Puis on renvoie la liste créer comme paramètre d'un classe représentant un jeu de carte
dans laquelle on va créer plusieurs méthode"""

from random import *

DICTCOULEUR = {"trèfle" : "noir", "pique" : "noir", "coeur" : "rouge", "carreau" : "rouge"}

DICTORDRE = { "as de coeur" : 1, "roi de coeur" : 2, "dame de coeur" : 3, "valet de coeur" : 4, "10 de coeur" : 5, "9 de coeur" : 6, "8 de coeur" : 7, "7 de coeur" : 8, "6 de coeur" : 9, "5 de coeur" : 10, "4 de coeur" : 11, "3 de coeur" : 12, "2 de coeur" : 13, "as de pique" : 14, "roi de pique" : 15, "dame de pique" : 16, "valet de pique" : 17, "10 de pique" : 18, "9 de pique" : 19, "8 de pique" : 20, "7 de pique" : 21, "6 de pique" : 22, "5 de pique" : 23, "4 de pique" : 24, "3 de pique" : 25, "2 de pique" : 26, "as de carreau" : 27, "roi de carreau" : 28, "dame de carreau" : 29, "valet de carreau" : 30, "10 de carreau" : 31, "9 de carreau" : 32, "8 de carreau" : 33, "7 de carreau" : 34, "6 de carreau" : 35, "5 de carreau" : 36, "4 de carreau" : 37, "3 de carreau" : 38, "2 de carreau" : 39, "as de trèfle" : 40, "roi de trèfle" : 41, "dame de trèfle" : 42, "valet de trèfle" : 43, "10 de trèfle" : 44, "9 de trèfle" : 45, "8 de trèfle" : 46, "7 de trèfle" : 47, "6 de trèfle" : 48, "5 de trèfle" : 49, "4 de trèfle" : 50, "3 de trèfle" : 51, "2 de trèfle" : 52 }    


class Carte():
    

    def __init__(self, enseigne, valeur):

        self.enseigne = enseigne
        self.valeur = valeur

    @property
    def couleur(self):
        return DICTCOULEUR[self.enseigne]

    @property
    def ordre(self):
        return DICTORDRE[self.__str__()]

    def __str__(self):
        return f"{self.valeur} de {self.enseigne}"

    def __repr__(self):
        return f"valeur = '{self.valeur}', enseigne = '{self.enseigne}"

class Jeu52():
   
    def __init__(self):
        self.listcarte = [] # le jeu de 52 carte, contient 52 objets Carte
        enseignecarte = ["coeur", "pique", "carreau", "trèfle"] # ne pas oublier de rajouter les autres enseingne
        valeurcarte = ["as", "roi", "dame", "valet", "10", "9", "8", "7", "6", "5", "4", "3", "2"]

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

    def piocher(self):
        shuffle(self.listcarte)
        try: 
            carte = self.listcarte[0]
            del self.listcarte[0]
        except IndexError:
            print("Il n'y a plus de carte")
        return carte

    def generateur_enseigne(self,enseigne):
        i = 0
        while i< len(self.listcarte):
            if self.listcarte[i].enseigne == enseigne:
                yield self.listcarte[i]
                i += 1
            else:
                i += 1 

    def generateur_valeur(self,valeur):
        i = 0
        while i< len(self.listcarte):
            if self.listcarte[i].valeur == valeur:
                yield self.listcarte[i]
                i += 1
            else:
                i += 1 

    def test_presence(self,ens,val):
        """Méthode pour savoir si une carte créée à la main se trouve dans jeu de départ"""
        test = False    
        for carte in self.listcarte:
            if carte.enseigne == ens and carte.valeur == val:
                test = True
        if test == True:
            print("la carte est dans le jeu")
        else:
            print("la carte n'est pas dans le jeu")


class Joueur():

    def __init__(self,nom):
        self.nom = nom

    def __str__(self):
        return  str(self.nom)


class Main():

    def __init__(self,taille,joueur):
        """ La main est d'une taille variable"""
        self.taille = taille
        self.propri = joueur.nom
        self.listecartemain = []

    def __str__(self):
        strlistcartemain = [] # Contient les 52 str(Carte)
        for i in self.listecartemain:
            strlistcartemain.append(str(i))
        return str(strlistcartemain)
 
    def piocher_main(self, jeu):
        for i in range(self.taille):
            self.listecartemain.append(jeu.listcarte[i])
        for i in range(self.taille):
            del jeu.listcarte[0]

    def trier_main(self):
        "permet de trier la main"
        maintriée = {}
        for carte in self:
            maintriée[carte] = carte.ordre
            # trier le dictionnaire



nom = "Romain"
romain = Joueur(nom)

main = Main(3, romain) #romain est une instance de la classe Joueur

    

jeu = Jeu52()
jeu.melanger()


# Puis faire : trier le jeu ou la main dans l'ordre
# ON EN EST LA : FINIR LA FONCTION TRIER DE LA CLASSE MAIN
# Puis refaire un programme propre qui simulera le jeu de la bataille et donnera sur 1000 parties le nombre de tour à jouer afin qu'il y ait un gagnant, le nom du gagnant de chaque partie.

main.piocher_main(jeu)

for carte in main.listecartemain:
    print(f"{carte} :  {carte.ordre}")
