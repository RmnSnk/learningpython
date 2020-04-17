# coding: utf-8

# Programme qui fait tourner une balle

from tkinter import *
from math import *

# permet de faire référence au centre du canevas plutôt qu'au coin
chgrp = [250, 250]

ry = 150  # rayon de rotation
# x,y de départ ; rayon ; couleur
balle = [0 + ry + chgrp[0], 0 + chgrp[1], 15, 'yellow']

ag = 0.17  # angle de rotation en radian

# Fonctions qui permettent de faire avancer la balle
# on va avoir xballe = rayon de rotation * cos angle
# on va avoir xballe = rayon de rotation * sin angle

def rotation():
    global balle, ry, ag
    balle[0] = ry * cos(ag) + chgrp[0]
    balle[1] = ry * sin(ag) + chgrp[1]
    can.coords(balle_oval, balle[0] - balle[2], balle[1] - balle[2],
               balle[0] + balle[2], balle[1] + balle[2])  # a voir
    pass

    
# widget maitre

fen = Tk()
fen.title("La petite balle qui avance")

# widgets exclaves

can = Canvas(fen, bg='grey', width=500, height=500)
can.grid(row=1, column = 1, columnspan=2)
balle_oval = can.create_oval(balle[0] - balle[2], balle[1] - balle[2],
                             balle[0] + balle[2], balle[1] + balle[2], fill=balle[3])
centre_oval = can.create_oval(248, 248, 252, 252, fill='red')


button_avance = Button(text="< >", command=rotation)
button_avance.grid(row=5, column=1, sticky=W)


Button(text="Quittez", command=fen.quit).grid(row=5, column=2, sticky=E)


# Programme principal

mainloop()
fen.destroy()



