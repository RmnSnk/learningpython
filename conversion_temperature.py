# coding: utf-8

# importation des modules
from tkinter import *


# ------------ Programme de conversion de température


#----------- Fonctions

def farenheit_vers_celcius(event):
    'fonction qui transforme des farenheit en celcius'
    f = int(entree_f.get())
    c = (f - 32) / 1.8
    varTC.set(str(c))


def celcius_vers_farenheit(event):
    'fonction qui transforme des celcius en farenheit'
    c = int(entree_c.get())
    f=c * 1.8 + 32
    varTF.set(str(f))


# ------------Widgets
fen=Tk()
fen.title('Conversion °F < - > °C')

varTF=StringVar()
varTC=StringVar()

# Label de textes et champs de saisie
Label(fen, text='Température en °F : ').grid(row=1, column=1)
entree_f=Entry(fen, textvariable=varTF)
entree_f.bind("<Return>", farenheit_vers_celcius)
entree_f.grid(row=1, column=2)


Label(fen, text='Température en °C : ').grid(row=2, column=1)
entree_c=Entry(fen, textvariable=varTC)
entree_c.bind("<Return>", celcius_vers_farenheit)
entree_c.grid(row=2, column=2)


# Bouton quitter
Button(fen, text='Quitter', command=fen.quit).grid(row=3, column=1, columnspan=2)



# boucle principale
mainloop()
fen.destroy()
