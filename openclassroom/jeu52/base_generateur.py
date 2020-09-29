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


nom = "Romain"
romain = Joueur(nom)
print(romain)

main = Main(7, romain) #romain est une instance de la classe Joueur

    

jeu = Jeu52()
jeu.melanger()


#test des générateurs
"""for carte in jeu.generateur_enseigne("coeur"):
    print(carte)
print()    


for carte in jeu.generateur_valeur("as"):
    print(carte)"""


#Test pour vérifié si la carte créée à la main se trouve dans le jeu
"""# On pioche une carte
carte_piochée = jeu.piocher()
print(f"La carte piochée est : {carte_piochée}")


# on crée une carte et vérifie si la même se trouve dans le jeu
print("On crée une carte et on vérifie si elle se trouve dans le jeu")
ens = input("Merci de saisir une enseigne : ")
val = input("Merci de saisir un valeur : ")

carte_cree = Carte(ens,val)
print(f"la carte créée est : {carte_cree}")

jeu.test_presence(ens,val)"""

# Prochaine étape coder l'attribut listecartemain de la classe Main afin de transférer 7 cartes du jeu vers la main
# Puis faire : trier le jeu ou la main dans l'ordre
# Puis refaire un programme propre qui simulera le jeu de la bataille et donnera sur 1000 parties le nombre de tour à jouer afin qu'il y ait un gagnant, le nom du gagnant de chaque partie.

main.piocher_main(jeu)
print(main)
print(jeu)
