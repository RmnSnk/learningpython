def saisie_liste():
    'fonction qui permet de saisir une liste'
    i = 1
    liste = []
    while i:
        saisie = input("merci de saisir une valeur (ne rien entrer pour terminer) : ")
        if saisie != '':
            liste.append(saisie)
        else:
            i = 0
    return liste

