<<<<<<< HEAD
def volBoite(a, b, c):
    return a * b * c
    
    
a = int(input('Merci de saisir la prenmi�re cote : '))
b = int(input('Merci de saisir la deuxi�me cote : '))
c = int(input('Merci de saisir la troisi�me cote : '))



print(volBoite(a, b, c))
=======

# prg bugg�

valeur = []


def volBoite(a=10, b=10, c=10):
    return a * b * c
    
    
def saisie():
    global valeur
    for i in range(3):
        print('Entrez la valeur ' + str(i + 1) + " : ", end='')
        v = input()
        if v == "":
            valeur.append(v)
        else:
            valeur.append(int(v))
        i = + 1
    return valeur


saisie()
print(valeur)

a = valeur[0]
b = valeur[1]
c = valeur[2]

print(volBoite(a, b, c))


>>>>>>> test
