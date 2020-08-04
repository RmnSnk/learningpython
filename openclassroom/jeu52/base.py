# coding:utf-8

"""On créer une classe Carte et on remplit la liste jeu52cartes avec des instanciation
de cette classe.
Puis on renvoie la liste créer comme paramètre d'un classe représentant un jeu de carte
dans laquelle on va créer plusieurs méthode"""

class Carte():
    
    def __init__(self, enseigne, valeur):

        self.enseigne = enseigne
        self.valeur = valeur

    def __str__(self):
        return f"{self.valeur} de {self.enseigne}"

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
        

jeu52 = Jeu52()
print(jeu52)
