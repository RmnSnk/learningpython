# coding: utf-8

import pickle
from random import randint


def logo():
    print("""
     JEU DU PENDU !
       ==========
	| /    |
	|/     O
	|     ~|~
	|     /|
	|
	|
   ===========
   """)

def regle():
    'Rappel les régles du pendu'
    print(
        """Les régles sont simples :
    Le jeu tire au sort un mot d'exactement 8 lettres et vous avez le droit de vous
    tromper 8 fois. Les lettres autorisées sont toutes les lettres de
    l'alphabet, sans aucun accent. Par exemple "e" sera accepté pour e, é, è, ê ...
    Le c sera accepté pour c et ç, enfin le o sera accepté pour oe.
    Vous pouvez proposer un mot, mais il faut alors respecter l'accentuation et les caractères
    spéciaux.
    A la fin de la partie, votre score sera égal au nombre de coup restant.
    Si vous perdez, votre score diminuera de 2 points.
    Amusez vous bien ! \n""")

def lecture_score():
    'Fonction qui va lire les scores'
    f = open('score.pickle', 'rb')
    score = pickle.load(f)
    for nom, point in score.items():
        print(f"{nom} a {point} points")
    print()
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
    
    # i : les lettres du mot, j : le nombre de coup joués, k = npmbre erreur
    i, j, k = 0, 0, 0
    
    liste_lettre_proposees = []
    
    lettre_saisie = str()

    flag = 2  # flag 1 : proposition faite et bonne, 0 proposition faite et fausse, 2 pas de proposition
    
    nb_etoiles = 8
    

    while j <= 7 and nb_etoiles != 0 and flag == 2:

        nb_coups_restant = 8 - j
        
        l = True

        while l:
    
            choix_avant_test_saisie = input(
                "Saisir une seule lettre ou votre proposition de mot : ")
        
            if len(choix_avant_test_saisie) == 1:
                
                    if (choix_avant_test_saisie in alphab) == True:
                        lettre_saisie = choix_avant_test_saisie.lower()
                        l = False
                    else:
                        print("Merci de saisir une lettre minuscule de l'alphabet, sans accent ou caractère spéciaux")
    
            else:

                if len(choix_avant_test_saisie) != 8:
                    print(f" ==> Attention le mot doit contenir exactement 8 lettres et non pas {len(choix_avant_test_saisie)}.")
                    
                else:

                    valid = input(f" ==> Etes vous certain de vouloir proposer le mot \"{choix_avant_test_saisie}\" (O/N): ").upper()

                    if valid == "O" and choix_avant_test_saisie == mot_secret:
                        l = False
                        # coder le nombre de points
                        victoire(nb_coups_restant)
                        flag = 1
                    elif valid == "O" and choix_avant_test_saisie != mot_secret:
                        l = False
                        defaite(mot_secret)
                        flag = 0
                    else:
                        pass

        print()

        liste_lettre_proposees.append(lettre_saisie)

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

        while i <= 7:  # car il y a 8 lettres dans le mot
            if (liste_mot_secret[i] in test) == True:
                liste_mot_encours[i] = liste_mot_secret[i]
            else:
                k += 1  # compte ne nombre de nom présent

            i += 1

        if k == 8:  # si k = 8 la lettre n'est pas présente
            j += 1
       
        k = 0

        nb_etoiles = liste_mot_encours.count("*")
        mot_encours = " ".join(liste_mot_encours)
        print(f"==> {mot_encours} <== \n")
        i = 0
        print(f"Il reste {nb_coups_restant} essais et {nb_etoiles} lettres à trouver")
        lettre_proposees = "-".join(liste_lettre_proposees)
        print(f"Lettres déjà proposées : {lettre_proposees} \n")

        if nb_etoiles == 0:
            break

    if j > 7 or flag == 0:
        defaite(mot_secret)
    elif nb_etoiles == 0 or flag == 1: 
        victoire(8 - j)
    else:
        pass



def victoire(points):
    'Donne la victoire, le nombre de points et écrit le score'
    print(f"Félicitations, vous avez gagnez en {8- points} erreurs")
    print(f"Vous gagnez donc {points} point(s) lors de cette partie")
    # coder l'écriture du score (appel fonction avec le nombre de point en argument)
    quit()
    pass


def defaite(mot_secret):
    "Donne la défaite, et écrit le score -2 points"
    print("Désolé, vous avez perdu, votre score va diminuer de 2 points")
    print(f"Le mot recherché était : {mot_secret}.")
    # coder l'écriture du score (appel fonction avec le nombre de point en argument)
    (quit)
    pass



# coder l'écriture des scores
# coder le test des lettres proposée
# corriger pendu() pour ne compter que les erreurs !