# coding : uft-8

# nombre de mots = nombre espace + 1

def compteMots(ph):
    'compte le nombre de mot contenus dans une phrase'
    i, nombre_mots = 0, 1
    while i < len(ph):
        if ph[i] == (" "):
            nombre_mots += 1
            i += 1
        else:
            i += 1
    return nombre_mots

    
ph = list(input('Saisissez la phrase : '))

print(compteMots(ph))