# coding: utf-8

# Premier programme de manipulation de fichiers


def fichier():
    global nom_fichier
    nom_fichier = input('Merci de saisir un nom de fichier # : ')
    print('\n')
    

def existance_fichier():
    'Fonction qui vérifié que le fichier existe ou le crée'
    global nom_fichier
    try:
        f = open(nom_fichier, "r")
        f.close()
        print('Ouverture du fichier ' + str(nom_fichier) + '.')
    except:
        f = open(nom_fichier, "w")
        f.close()
        print('Le fichier ' + str(nom_fichier) + ' a été créé.')

def choix_action():
    print()
    print('Fichier de travail : ' + str(nom_fichier) + '\n')
    print('Que souhaitez vous faire ?')
    print('    Choisir un fichier :       1')
    print('    Afficher le fichier :      2')
    print('    Ecrire dans le fichier :   3')
    print('    Phrase la plus longue :    4')
    print('    Quittez :                  5 \n')
    while 1:
        try:
            choix = int(input('Saisir 1, 2, 3, 4 ou 5 : \n'))
            if choix == 1 or choix == 2 or choix == 3 or choix == 4 or choix == 5:
                break
            else:
                print()
                print('On a  dit 1, 2, 3, 4 ou 5 ! \n', color='red')
                choix_action()
        except:
            print('On a dit 1,2,3,4 ou 5 ! \n')
            print()
            choix_action()
            
    if choix == 2:
        lire_fichier()
        print()
        choix_action()
    elif choix == 3:
        ecrire_fichier()
        print()
        choix_action()
    elif choix == 1:
        fichier()
        existance_fichier()
        choix_action()
    elif choix == 4:
        phrase_longue()
        choix_action()
    else:
        print('Exit ...')
        

def lire_fichier():
    'Fonction qui permet de lire un fichier'
    global nom_fichier
    print('### Affichage du fichier : ' + str(nom_fichier) + ' ###' + '\n')
    try:
        f = open(nom_fichier, 'r')
        t = f.read()
        print(t)
        f.close()
    except:
        choix_action()

def ecrire_fichier():  # a coder pour écrire ligne par ligne
    'Fonction qui ecrit dans un fichier'
    global nom_fichier
    print('### Ecriture dans le fichier : ' + str(nom_fichier) + ' ###')
    try:
        f = open(nom_fichier, 'a')
        i = 1
        while i:
            ligne = input("# : ")
            if ligne == "":
                i = 0
            else:
                f.write(ligne)
                f.write('\n')
                f.close()
    except:
        choix_action()

def phrase_longue():
    'Fonction qui trouve la phrase la plus longue'
    global nom_fichier
    print('### La phrase la plus longue du fichier ' +
          str(nom_fichier) + ' est : ###')
    f = open(nom_fichier, 'r')
    i = 1
    tmax = 'Fichier vide'
    nmax = 0
    while i:
        t = f.readline()
        n = len(t)
        if n > nmax:
            nmax = n
            tmax = t
        if n == 0:
            f.close()
            print(tmax + "(" + str(nmax-1) + ' caractères)')
            break
        


# programme principal

nom_fichier = "Aucun, merci de d'abord choisir un fichier (1)"
choix_action()


