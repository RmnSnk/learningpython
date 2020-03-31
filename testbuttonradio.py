# coding: utf-8

from tkinter import *
from math import sqrt

planete = 'A choisir'

def valeur():
    'Renvoie la valeur de planete_choisie pour pouvoir savoir quelle planete utilisée'
    global planete
    planete = planete_choisie.get()
    print (planete)  # debug
   

# Création du widget principal
fen1 = Tk()
fen1.title('Test buttons radio')

Button(fen1, text='Quitter', command=fen1.quit).pack()

planete_choisie = StringVar()


bt1 = Radiobutton(fen1, text='Mars', variable=planete_choisie, value='Mars', command=valeur)
bt1.pack()

bt2 = Radiobutton(fen1, text='Terre', variable=planete_choisie, value='Terre', command=valeur)
bt2.pack()

fen1.mainloop()
fen1.destroy()
