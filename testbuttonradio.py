# coding: utf-8

from tkinter import *
from math import sqrt

planete = 'A choisir'

def choix_planete():
    'Renvoie la valeur de planete_choisie pour pouvoir savoir quelle planete utilisée'
    global planete
    planete = planete_choisie.get()
    print (planete)  # debug
   

# Création du widget principal
fen1 = Tk()
fen1.title('Test buttons radio')

# Création du canvas
can1 = Canvas(fen1, bg='black', height=1000, width=1000)
can1.grid(row=2, column=1, columnspan=6)


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
bt2.grid(row = 3, column = 4)

fen1.mainloop()
fen1.destroy()
