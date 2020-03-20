# coding: utf-8

def saisie_liste():
    'fonction qui permet de saisir une liste'
    i = 1
    liste = []
    while i:
        saisie = input(
            "merci de saisir une valeur (ne rien entrer pour terminer) : ")
        if saisie != '':
            liste.append(int(saisie))
        else:
            i = 0
    return liste


def eleMax(serie, debut, fin):
    maximum, i = serie[debut], debut
    for i in range(debut, fin):
        if serie[i] > maximum:
            maximum = serie[i]
        i += 1
    return maximum


serie = saisie_liste()

resultat = eleMax(serie, debut=0, fin=len(serie))

print(resultat)
