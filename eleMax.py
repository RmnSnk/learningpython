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


def eleMax(serie, debut, fin):
    maximum, i = serie[debut], debut
    for i in range(debut, fin):
        if serie[i] > maximum:
            maximum = serie[i]
        i += 1
    return maximum


serie = saisie_liste()

while i:
    a = int(input('Saissisez le début de la recherche | Entrez pour passer : '))
    if a > len(serie) or a < 0:
        print('Vous êtes idiot')
    else:
        i = 0

while j:
    b = int(input('Saissisez la fin de la recherche | Entrez pour passer : '))
    if b > len(serie) or b <= a:
        print('BAKA !!!')
    else:
        j = 0

## Il reste à coder la prise en compte de a = début et b = fin

resultat = eleMax(serie, debut=0, fin=len(serie))

print(resultat)
