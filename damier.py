# coding: utf-8

from tkinter import *

# on créer une fonction qui fait une ligne de 10 cases (boucle)
# on boucle la fonction pour pour faire toutes les lignes

def damier():
    x = 0
    for i in range(5):
        can.create_rectangle(0 + x, 0, 100 + x, 100, fill='ivory')
        can.create_rectangle(100 + x, 0, 200 + x, 100, fill='black')
        x += 200



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