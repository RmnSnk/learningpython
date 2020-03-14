# coding: utf-8

mois = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'aout', 'septembre', 'octobre', 'novembre', 'décembre']

def nomMois(numero):
    return mois[numero - 1]

choix = int(input('Choisissez un chiffre entre 1 et 12 : '))

print(nomMois(choix))


