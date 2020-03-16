#Programme bug

valeur = []


def volBoite(a=10, b=10, c=10):
    return a * b * c
    
    
def saisie():
    global valeur
    for i in range(3):
        print('Entrez la valeur ' + str(i + 1) + " : ", end='')
        v = input()
        if v != "":
            valeur.append(int(v))
        i = + 1
    return valeur


saisie()
print('Vous avez saisie : ' + str(valeur))

if len(valeur) == 0:
    print(volBoite())
elif len(valeur) == 1:
    a = valeur[0]
    print(volBoite(a))
elif len(valeur) == 2:
    a = valeur[0]
    b = valeur[1]
    print(volBoite(a, b))
else:
    a = valeur[0]
    b=valeur[1]
    c=valeur[2]
    print(volBoite(a, b, c))    

