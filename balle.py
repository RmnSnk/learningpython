# coding: utf-8

# Programme qui fait avancer une balle

balle = [250, 50, 15, 'yellow']  # x,y de départ ; rayon ; couleur

from tkinter import *

# widget maitre

fen = Tk()
fen.title("La petite balle qui avance")

# widgets exclaves

can = Canvas(fen, bg='grey', width=500, height=100)
can.grid(row=1, column = 1, columnspan=2)
balle_oval = can.create_oval(balle[0] - balle[2], balle[1] - balle[2], balle[0] + balle[2], balle[1] + balle[2], fill=balle[3])

Button(text="Quittez", command=fen.quit).grid(row=5, column=2, sticky=E)


# Programme principal

mainloop()
fen.destroy()



