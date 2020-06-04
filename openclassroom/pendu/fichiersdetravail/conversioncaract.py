# coding : utf-8
# pour obtenir le mot sans accent

def test(mot_lettre):  # caract = mot ou lettre
    alphab = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
        "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    list_mot_lettre = list(mot_lettre)  # conversion en liste
    list_mot_lettre_check = []  # pour le mot / caractère transformé

    for caract in list_mot_lettre:
        try:
            if alphab.count(caract) == 1:
                list_mot_lettre_check.append(caract)
            elif caract == "é" or caract == "è" or caract == "ê" or caract == "ë":
                caract = "e"
                list_mot_lettre_check.append(caract)
            elif caract == "ï" or caract == "î":
                caract = "i"
                list_mot_lettre_check.append(caract)
            elif caract == "ù" or caract == "ü" or caract == "û":
                caract = "u"
                list_mot_lettre_check.append(caract)
            elif caract == "ö" or caract == "œ":
                caract = "o"
                list_mot_lettre_check.append(caract)
            elif caract == "à" or caract == "â":
                caract = "a"
                list_mot_lettre_check.append(caract)
            elif caract == "ç":
                caract = "c"
                list_mot_lettre_check.append(caract)
            else:
                pass
        except:
            pass  # lever exception si le joeur saisit autre chose q'une seule lettre
    mot_lettre_check = "".join(list_mot_lettre_check)
    return mot_lettre_check


mot = "é"

print(test(mot))
print(mot)