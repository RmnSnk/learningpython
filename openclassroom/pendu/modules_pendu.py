# coding: utf-8

import pickle
from random import randint


def regle():
    'Rappel les régles du pendu'
    print("""Les régles sont simples :
    Le jeu tire au sort un mot d'exactement 8 lettres et vous avez 10 chances
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
        mot = f.readline().strip() #.strip() permet de virer le '\n' à la fin
        i += 1
    f.close()
    mot = mot.lower()
    return mot  # coder pour transformer les caractère spéciaux
# devra retourner 2 mot : un normal avec les accent et un transformé


def pendu(mot_secret):
    'On test la lettre et on permet de remplacer les caractères spéciaux'

    alphab = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
    "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    liste_mot_secret = list(mot_secret)
    
    liste_mot_encours = ["*", "*", "*", "*", "*", "*", "*", "*"]
    
    i, j = 0, 0

    while j <= 10:  # a modifier pour coder la fin de partie
    

        lettre_saisie = input("Lettre : ")

        if lettre_saisie == "e":
            test = ["e", "é", "è", "ê", "ë"]
        elif lettre_saisie == "i":
            test = ["i", "î", "ï"]
        elif lettre_saisie == "o":
            test = ["o", "ô", "ö", "œ"]
        elif lettre_saisie == "a":
            test = ["a", "â"]
        elif lettre_saisie == "u":
            test = ["u", "û", "ü"]
        elif lettre_saisie == "c":
            test = ["c", "ç"]
        else:
            test = lettre_saisie

        while i <= 7:
            if (liste_mot_secret[i] in test) == True:
                liste_mot_encours[i] = liste_mot_secret[i]
            else:
                pass  # pas forcément nécessaire
            i += 1
        mot_encours = "".join(liste_mot_encours)
        print(mot_encours)
        i = 0
    j += 1
    

def fin_partie(coup, x, mot_secret):
    """Fonction qui vérifie si la fin de partie est atteinte,
    renvoie True si atteint"""
    if str(x) == str(mot_secret):
        print("Gagné")
        return True
    elif coup < 10:
        return False    
    else:
        print("Game Over!")
        return True

# coder la boucle des lettres, la fin de partie
# le joueur doit pouvoir proposer un mot
