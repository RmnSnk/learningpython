# coding : utf-8

# Ex : si le joueur tape "e", remplace tous les "e, é, è ,ê ..."

def saisie(mot_secret):
    'On test la lettre et on permet de remplacer les caractères spéciaux'

    alphab = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
    "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    liste_mot_secret = list(mot_secret)
    
    mot_encours = ["*", "*", "*", "*", "*", "*", "*", "*"]
    
    i, j = 0, 0

    while j <= 10:
    

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
                mot_encours[i] = liste_mot_secret[i]
            else:
                pass  # pas forcément nécessaire
            i += 1
        print(mot_encours)
        i = 0
    j += 1

    # coder un test pour interdire toute les saisies n'appartenant pas à alphab

    # code pour démasquer les lettre


# Appel de la fonction
mot = "aöéçaïœû"
saisie(mot)
