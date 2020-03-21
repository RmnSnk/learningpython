# coding: utf-8
i, j = 1, 1


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

serie = saisie_liste()
len_serie = len(serie)

def eleMax(serie, debut=0, fin=len_serie):
    maximum, i = serie[debut], debut
    for i in range(debut, fin):
        if serie[i] > maximum:
            maximum = serie[i]
        i += 1
    return maximum


resultat = eleMax(serie, 1, 8)

print(resultat)
