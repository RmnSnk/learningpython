# coding: utf-8

# Premier programme de manipulation de fichiers




def fichier():
    global nom_fichier
    nom_fichier = input('Merci de saisir un nom de fichier # : ')
    

def existance_fichier():
    'Fonction qui vérifié que le fichier existe'
    global nom_fichier
    try:
        f = open(nom_fichier, "r")
        f.close()
        return 1
    except:
        fichier()
        return 0

def choix_action():
    print('Que souhaitez vous faire ?')
    print('    Afficher un fichier :    1')
    print('    Ecrire dans le fichier : 2 \n')
    while 1:
        try:
            choix = int(input('Saisir 1 ou 2 : '))
            if choix == 1 or choix == 2:
                break
            else:
                print()
                print('On a  dit 1 OU 2 ! \n', color='red')
                choix_action()
        except:
            print('On a dit 1 OU 2 ! \n')
            print()
            choix_action()
            
    if choix == 1:
        print('Vous avez choisi 1')
        lire_fichier()
    else:
        print('Vous avez choisi 2')
        ecrire_fichier()
    
def lire_fichier():  # a coder
    'Fonction qui permet de lire un fichier'
    pass

def ecrire_fichier():  # a coder
    'Fonction qui ecrit dans un fichier'
    pass


# programme principal

fichier()

while existance_fichier() == 0:
    existance_fichier()

choix_action()


