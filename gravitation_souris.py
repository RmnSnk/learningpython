# coding: utf-8

# Modifier pointeur pour creer la planete

from tkinter import *
from math import sqrt


def choix_planete():
    'Renvoie la valeur de planete_choisie pour pouvoir savoir quelle planete utilisée'
    global planete
    planete = planete_choisie.get()
    choix.configure(text='La planete choisie est : ' + str(planete))
    
def pointeur(event):
    'Fonction qui donne les coordonnées du clic'
    clicx = event.x
    clicy = event.y
    print (clicx)  # debug
    print (clicy)
    return (clicx, clicy)



def creation_planete():
    'Créer une planete ou l\' n on clique'
    

# Création du widget principal
fen1 = Tk()
fen1.title('Test buttons radio')

# Création du canvas
can1 = Canvas(fen1, bg='black', height=1000, width=1000)
can1.grid(row=2, column=1, columnspan=6)
can1.bind("<Button-1>", pointeur)

# Création de widget esclaves

# Champs du haut

Label(fen1, text='Masse de Mars : 6,39e+23 kg').grid(row=1, column=1, columnspan=2)
Label(fen1, text='Echelle : 100px = 19 millions de km').grid(row=1, column=3, sticky=E)
Label(fen1, text='Masse de la Terre : 5,972e+24 kg').grid(row=1, column=5, columnspan=6)


# Bouton quitter
Button(fen1, text='Quitter', command=fen1.quit).grid(row=3, column=6)


# Bouton radio de choix de la planete
planete_choisie = StringVar()
bt1 = Radiobutton(fen1, text='Mars', variable=planete_choisie, value='Mars', command=choix_planete)
bt1.grid(row = 3, column = 3)
bt2 = Radiobutton(fen1, text='Terre', variable=planete_choisie, value='Terre', command=choix_planete)
bt2.grid(row=3, column=4)

choix = Label(fen1)
choix.grid(row=4, column=3, sticky=E)





# Boucle principale
fen1.mainloop()
fen1.destroy()
