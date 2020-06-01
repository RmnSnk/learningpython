# coding: utf-8

import pickle
from random import randint


def regle():
    'Rappel les régles du pendu'
    print("""Les régles sont simples :
    Le jeu tire au sort un mot d'exactement 8 lettres et vous avez 8 chances
    pour trouver ce mot. Les lettres autorisées sont toutes les lettres de
    l'alphabet, sans aucun accent. Par exemple "e" sera accepté pour e, é, è, ê ...
    Le c sera accepté pour c et ç, enfin le o sera accepté pour oe
    A la fin de la partie, votre score sera égal au nombre de coup restant.
    Si vous perdez, votre score diminuera de 2 points.
    Amusez vous bien ! \n""")

def lecture_score():
    'Fonction qui va lire les scores'
    f = open('score.pickle', 'rb')
    score = pickle.load(f)
    for nom, point in score.items():
        print(f"{nom} a {point} points")
    f.close()
        

def score_joueur(nj):
    'Fonction qui permet au joueur de récupérer son score ou le l\'initialiser'
    f = open('score.pickle', 'rb')
    score = pickle.load(f)
    try:
        sc = score[nj]
    except:
        sc = 0
    f.close()
    return sc


def random_word():
    'Fonction qui choisi un mot au hasard depuis le fichier liste9854'
    f = open("liste9854", "r")
    i = 0
    j = randint(0, 9853)

    while i <= j:
        mot = f.readline()
        i += 1
    f.close()
    return mot.lower()


def pendu(mot_secret):
    'Le joueur propose des lettres jusqu\'à la victoire ou la défaite'
    liste_mot = list(mot_secret)
    mot_encours = ["*", "*", "*", "*", "*", "*", "*", "*"]
    coup = 0  # Nombre de coups joués
    x = []  # Mot en cours de résolution

    while fin_partie(coup, x, mot_secret) == False:
        choix = input("Lettre : ")
        coup += 1
        i = 0
        while i <= 7:
            if choix == liste_mot[i]:
                mot_encours[i] = choix
            i += 1
            x = "".join(mot_encours)
        print(x)
        fin_partie(coup, x, mot_secret)
    

def fin_partie(coup, x, mot_secret):
    """Fonction qui vérifie si la fin de partie est atteinte,
    renvoie True si atteind"""
    print(x)
    print(mot_secret)
    if str(x) == str(mot_secret):
        print("Gagné")
        return True
    elif coup < 10:
        return False    
    else:
        print("Game Over!")
        return True
    
    


# coder la boucle des lettres, la fin de partie
# attention au caractère spéciaux e = e, é, ...