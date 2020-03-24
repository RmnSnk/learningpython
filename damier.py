# coding: utf-8

from tkinter import *

# on créer une fonction qui fait une ligne de 10 cases (boucle)
# on boucle la fonction pour pour faire toutes les lignes

def damier():
    x, y = 0, 0
    col1, col2 = 'ivory', 'black'
    for i in range(10):
        can.create_rectangle(x, y, x + 100, y + 100, fill=col1)
        x += 100
        col1, col2 = col2, col1



# programme principal

fen = Tk()
can = Canvas(fen, width=1000, height=1000, bg='red')
can.pack(side=TOP, padx=3, pady=3)
bou1 = Button(fen, text='Quittez', command=fen.quit)
bou1.pack(side=BOTTOM)
bou2 = Button(fen, text='Damier', command=damier)
bou2.pack()

fen.mainloop()
fen.destroy()