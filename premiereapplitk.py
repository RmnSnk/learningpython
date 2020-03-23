# coding: utf-8

from tkinter import *
from random import randrange

# --- définition des fonctions gestionnaires d'événements : ---
def drawline():
    "Tracé d'une ligne dans le canevas can1"
    global x1, y1, x2, y2, coul
    can1.create_line(x1, y1, x2, y2, width=1, fill=coul)
    # modification des coordonnées pour la ligne suivante:
    y2, y1 = y2 + 10, y1 + 10

def drawline2():
    "Trace une croix rouge au centre"
    coul = 'red'
    can1.create_line(0, 250, 650, 250, width=1, fill=coul)
    can1.create_line(325, 0, 325, 500, width=1, fill=coul)

def changecolor():
    "Changement aléatoire de la couleur du tracé"
    global coul
    pal = ['purple', 'cyan', 'maroon', 'green', 'red', 'blue', 'orange', 'yellow']
    c = randrange(8)  # => génère un nombre aléatoire de 0 à 7
    coul = pal[c]


#------ Programme principal -------


# les variables suivantes seront utilisées de manière globale :
x1, y1, x2, y2 = 0, 10, 650, 10  # coordonnées de la ligne
coul = 'dark green' # couleur de la ligne
# Création du widget principal ("maître") :
fen1 = Tk()
# création des widgets "esclaves" :
can1 = Canvas(fen1, bg='dark grey', height=500, width=650)
can1.pack(side=LEFT)
bou1 = Button(fen1,text='Quitter',command=fen1.quit)
bou1.pack(side=BOTTOM)
bou2 = Button(fen1,text='Tracer une ligne',command=drawline)
bou2.pack()
bou3 = Button(fen1,text='Autre couleur',command=changecolor)
bou3.pack()
bou4 = Button(fen1, text='Trace une croix rouge', command=drawline2)
bou4.pack()
fen1.mainloop()  # démarrage du réceptionnaire d'événements
fen1.destroy()  # destruction (fermeture) de la fenêtre