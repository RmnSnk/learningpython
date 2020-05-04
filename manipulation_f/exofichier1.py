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
    print('    Quittez :                  4 \n')
    while 1:
        try:
            choix = int(input('Saisir 1, 2, 3 ou 4 : \n'))
            if choix == 1 or choix == 2 or choix == 3 or choix == 4:
                break
            else:
                print()
                print('On a  dit 1, 2, 3 ou 4 ! \n', color='red')
                choix_action()
        except:
            print('On a dit 1,2,3 ou 4 ! \n')
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
    print('### Ecriture dans le fichier :' + str(nom_fichier) + ' ###')
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
    except:
        choix_action()


# programme principal

nom_fichier = "Aucun, merci de d'abord choisir un fichier (1)"
choix_action()


