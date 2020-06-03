# coding : utf-8


def pendu(mot_secret):
    'On test la lettre et on permet de remplacer les caractères spéciaux'

    alphab = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
    "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    liste_mot_secret = list(mot_secret)
    
    liste_mot_encours = ["*", "*", "*", "*", "*", "*", "*", "*"]
    
    i, j = 0, 0  # i : les lettres du mot, j : le nombre de coup
    
    liste_lettre_proposees = []

    flag = 2  # flag 1 : proposition faite et bonne, 0 proposition faite et fausse, 2 pas de proposition


    # il faut un flag pour savoir si le joueur tente la proposition
    while j <= 8 or nb_etoiles != 0 or flag == 2:

        # Faire une fonction de test de proposition
        choix_avant_test_saisie = input(
            "Lettre ou #votre proposition : \n ----> ")
        liste_choix_avant_test_saisie = list(choix_avant_test_saisie)

        if liste_choix_avant_test_saisie[0] == "#":
            del liste_choix_avant_test_saisie[0]
            proposition = "".join(liste_choix_avant_test_saisie)
            if proposition == mot_secret:
                flag = 1
                # petite astuce pour calculer le nombre de point par victoire directe
                nb_etoiles = (8 - j)
                break
            else:
                flag = 0
                break            

        lettre_saisie = choix_avant_test_saisie
        print()
        j += 1
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
                pass  # pas forcément nécessaire
            i += 1
        nb_etoiles = liste_mot_encours.count("*")
        nb_coups_restant = 8 - j
        mot_encours = "".join(liste_mot_encours)
        print(f"----> {mot_encours}")
        i = 0
        print(f"Il reste {nb_coups_restant} essais")
        lettre_proposees = "-".join(liste_lettre_proposees)
        print(f"Lettres déjà proposées : {lettre_proposees} \n")
        
        print(nb_etoiles) #debug

        if nb_etoiles == 0:
            break

    if j > 8 or flag == 0:
        defaite()
    elif nb_etoiles == 0 or flag == 1:  # problème a trouver
        victoire(8 - j)
    else:
        pass



# en fait il faut plutôt coder 2 fonctions : victoire et defaite et les appeler dans pendu()

def victoire(points):
    'Donne la victoire, le nombre de points et écrit le score'
    print(f"Félicitations, vous avez gagnez en {8- points} coups")
    print(f"Vous gagnez donc {points} lors de cette partie")
    # coder l'écriture du score (appel fonction avec le nombre de point en argument)
    pass

def defaite():
    "Donne la défaite, et écrit le score -2 points"
    print("Désolé, vous avez perdu, votre score va diminuer de 2 points")
    # coder l'écriture du score (appel fonction avec le nombre de point en argument)
    pass


mot = "égoïstes"
pendu(mot)