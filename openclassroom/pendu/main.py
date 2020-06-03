# coding : utf-8


from modules_pendu import *


# On appel les règles
regle()

# On les scores
lecture_score()

# On choisi son joueur, on récupére le score
nj = input("Quel est ton nom : ")
print(f"Bienvenue {nj}, ton score est de {score_joueur(nj)} point(s)")

# Le programme chosit un mot au hasard
mot_secret = random_word()
print(mot_secret)  # debug

# Le joueur choisit des lettres jusqu'à la fin de la partie
pendu(mot_secret)
