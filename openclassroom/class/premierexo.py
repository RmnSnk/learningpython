# coding : utf-8

class Personne:
    """ Classe définissant une personne """

    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        self._lieu_residence = "Paris"

    @property
    def lieu_residence(self):
        return self._lieu_residence

    @lieu_residence.setter
   # """Pour changer le lieu de residence et afficher un message"""
    def lieu_residence(self, nouveau_lieu):
        print(f"{self.prenom} {self.nom} déménage à {nouveau_lieu}.")
        self._lieu_residence = nouveau_lieu

humain1 = Personne("sonneck","romain")

print(humain1.nom)
print(humain1.prenom)
humain1.lieu_residence = "Nice"

