# coding: utf-8

# Premier programme de manipulation de fichiers


def choix_action():
    print('Que souhaitez vous faire ?')
    print('    Afficher un fichier :    1')
    print('    Ecrire dans le fichier : 2 \n')

# programme principal

nom_fichier = input('Merci de saisir un nom de fichier: ')
choix_action()

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
    print('Vous avez choisi 1')  # a remplacer par le code
else:
    print('Vous avez choisi 2')  # a remplacer par le code


