# coding: utf-8

# reste à coder le choix du début fin de la recherche en modifiant la boucle while de la fonction changeCar sans doute par in range

parametres = []


def changeCar(ch, ca1, ca2, debut, fin):
    'Fonction qui modifie un caractère d\'une phrase'
    i = 0
    while i < len(ch):
        if ch[i] == ca1:
            ch[i] = ca2
            i += 1
        else:
            i += 1
    ch_join = ''.join(ch)
    return ch_join


chaine_caractere = str(input('Saissez une phrase : '))
ch_liste = list(chaine_caractere)

ca1 = str(input('Saisissiez le caractère à remplacer : '))
ca2 = str(input('Saisissez le caractère de remplacement : '))
debut = str(input('Saisissez le début | <ENTER> pour passer : '))
fin = str(input('Saisissez la fin | <ENTER> pour passer: '))

# on créer un liste dont le nombre d'élément varie en fonction des éléments saisis

parametres.append(ch_liste)
parametres.append(ca1)
parametres.append(ca2)
if debut != "":
    parametres.append(debut)
else:
    parametres.append(0)
if fin != "":
    parametres.append(fin)
else:
    parametres.append(len(ch_liste) + 1)



print(changeCar(parametres[0], parametres[1],
      parametres[2], parametres[3], parametres[4]))
