# coding: utf-8

# importation des modules
from tkinter import *


# ------------ Programme de conversion de température


#----------- Fonctions

def farenheit_vers_celcius():
    'fonction qui transforme des farenheit en celcius'
    pass

def celcius_vers_farenheit():
    'fonction qui transforme des celcius en farenheit'
    pass
    

# ------------Widgets
fen = Tk()
fen.title('Conversion °F < - > °C')

# Label de textes et champs de saisie
Label(fen, text='Température en °F : ').grid(row=1, column=1)
entree_f = Entry(fen)
entree_f.grid(row=1, column=2)


Label(fen, text='Température en °C : ').grid(row=2, column=1)
entree_c = Entry(fen)
entree_c.grid(row=2, column=2)


# Bouton quitter
Button(fen, text='Quitter', command=fen.quit).grid(row=3, column=1, columnspan=2)



# boucle principale
mainloop()
fen.destroy()
