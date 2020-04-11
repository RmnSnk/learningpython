# coding: utf-8

# Programme qui fait avancer une balle

balle = [250, 50, 15, 'yellow']  # x,y de départ ; rayon ; couleur

from tkinter import *

# Fonctions qui permettent de faire avancer la balle

def avance(pas):
    'Fonction qui fait avancer la balle vers la droite'
    global balle
    balle[0] = balle[0] + pas
    can.coords(balle_oval, balle[0] - balle[2], balle[1] - balle[2], balle[0] + balle[2], balle[1] + balle[2])


def droite():
    avance(20)

def gauche():
    avance(-20)
    
def sens():
    #il faut arriver a programmer les allez retours, peut être en se souvenant de la position n-1
        

    
# widget maitre

fen = Tk()
fen.title("La petite balle qui avance")

# widgets exclaves

can = Canvas(fen, bg='grey', width=500, height=100)
can.grid(row=1, column = 1, columnspan=2)
balle_oval = can.create_oval(balle[0] - balle[2], balle[1] - balle[2], balle[0] + balle[2], balle[1] + balle[2], fill=balle[3])

button_avance = Button(text="< >", command=sens)
button_avance.grid(row=5, column=1, sticky=W)
Button(text="Quittez", command=fen.quit).grid(row=5, column=2, sticky=E)


# Programme principal

mainloop()
fen.destroy()



