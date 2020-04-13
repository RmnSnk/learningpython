# coding: utf-8

# Programme qui fait avancer une balle

balle = [250, 50, 15, 'yellow']  # x,y de départ ; rayon ; couleur
f = 0

from tkinter import *

# Fonctions qui permettent de faire avancer la balle

def avance(pas):
    'Fonction qui fait avancer la balle'
    global balle
    balle[0] = balle[0] + pas
    can.coords(balle_oval, balle[0] - balle[2], balle[1] - balle[2], balle[0] + balle[2], balle[1] + balle[2])


def droite():
    'Fonction qui avance vers la droite'
    avance(20)

def gauche():
    'Fonction qui avance vers la gauche'
    avance(-20)
    

def mouvement():
    'Foncion qui met en mouvement la balle et gérant les allers retours'
    global balle, f
    if f == 0:
        droite()
        if balle[0] > 500:
            f = 1
    if f == 1:
        gauche()
        if balle[0] < 0:
            f = 0

    
# widget maitre

fen = Tk()
fen.title("La petite balle qui avance")

# widgets exclaves

can = Canvas(fen, bg='grey', width=500, height=100)
can.grid(row=1, column = 1, columnspan=2)
balle_oval = can.create_oval(balle[0] - balle[2], balle[1] - balle[2], balle[0] + balle[2], balle[1] + balle[2], fill=balle[3])

button_avance = Button(text="< >", command=mouvement)
button_avance.grid(row=5, column=1, sticky=W)
Button(text="Quittez", command=fen.quit).grid(row=5, column=2, sticky=E)


# Programme principal

mainloop()
fen.destroy()



