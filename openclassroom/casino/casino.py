# coding: utf-8

# Petit jeu de roulette

from math import ceil
from random import randint



richesse = 100 # on initialise la richesse du jouer
victoire = richesse * 3 # le joueur gagne si il triple sa mise
mise_check = 0

def fin_partie():
    'fonction qui vérifie si le joueur gagne ou perd'
    if richesse <= 0:
        print("Game Over")
    elif richesse >= victoire:
        print("Gagné, vous avez fait sauter la banque !")
    else:
        mise()
        partie()
    
def mise():
    global mise_check
    'fonction qui demande la mise'
    mise = int(input(f"Combien voulez vous miser, pas plus de {richesse} euros : "))
    if mise > richesse:
        print("Vous n'êtes pas assez riche")
        mise()
    else:
        mise_check = mise
        return mise_check

def pair_impair(a):
    'fonction qui teste le paramètre a, renvoie TRUE si pair, FALSE sinon'
    if a % 2 == 0:
        return(True)
    else:
        return(False)

def partie():
    global richesse
    numero = int(input("Sur quel numéro pariez vous ? : "))
    test_numero = pair_impair(numero)
    banque = randint(0, 49)
    print(f"Le croupier lance la roulette ... le numéro {banque} sort !")
    test_banque = pair_impair(banque)
    if numero == banque:
        richesse += mise_check*3
        print(f"Gagné, vous récupérez votre mise de {mise_check} euros ainsi que {3*mise_check} euros de gains")
        print(f"Vous disposez de {richesse} euros")
        fin_partie()
    elif test_numero == test_banque:
        richesse += mise_check + ceil(mise_check/2)        
        print(f"Petit gain, vous récupérez votre mise de {mise_check} euros ainsi que {ceil(mise_check/2)} euros de gains")
        print(f"Vous disposez de {richesse} euros")
        fin_partie()
    else:
        richesse -= mise_check
        print(f"Perdu, vous il vous reste {richesse} euros")
        fin_partie()
    
def main():
    'Fonction principale'
    print(f"Vous commencez avec {richesse} euros")
    print("Vous gagnez si vous triplez votre mise")
    print("Vous perdez quand vous n'avez plus d'argent")
    print("Bonne chance!")
    mise()
    partie()
    
main()