# coding : utf-8

# Fonction qui vérifie ce que saisit l'utilisateur


def test_saisie(mot_secret):


    alphab = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
    "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    j = True
    
    while j:

        saisie = input(
            "Saisir une seule lettre ou votre proposition de mot : ")
    
        if len(saisie) == 1:
            
                if (saisie in alphab) == True:
                    j = False
                    return saisie.lower()
                else:
                    print("Merci de saisir une lettre minuscule de l'alphabet, sans accent ou caractère spéciaux")

        else:
            valid = input(f"Etes vous certain de vouloir proposer le mot \"{saisie}\" (O/N): ").upper()

        if valid == "O" and saisie == mot_secret:
            j = False
            print("Victoire")
        elif valid == "O" and saisie != mot_secret:
            j = False
            print("Défaite")
        else:
            pass

                
                
                
# a indenter
            

test_saisie("toto")
