# coding: utf-8

from tkinter import *

def drawcirclebleu():
    'fonction qui va dessiner un cercle bleu'
    x1, y1, x2, y2, coul = 10, 10, 110, 110, 'blue'
    can1.create_oval(x1, y1, x2, y2, width=4, outline=coul)

def drawcirclenoir():
    'fonction qui va dessiner un cercl noir'
    x1, y1, x2, y2, coul = 120, 10, 230, 110, 'black'
    can1.create_oval(x1, y1, x2, y2, width=4, outline=coul)

def drawcirclerouge():
    'fonction qui va dessiner un cercle rouge'
    x1, y1, x2, y2, coul = 240, 10, 340, 110, 'red'
    can1.create_oval(x1, y1, x2, y2, width=4, outline=coul)

def drawcirclejaune():
    'fonction qui va dessiner un cercle jaune'
    x1, y1, x2, y2, coul = 65, 60, 165, 160, 'yellow'
    can1.create_oval(x1, y1, x2, y2, width=4, outline=coul)

def drawcirclevert():
    'fonction qui va dessiner un cercle vert'
    x1, y1, x2, y2, coul = 175, 60, 275, 160, 'green'
    can1.create_oval(x1, y1, x2, y2, width=4, outline=coul)    
    



# creation de la fenetre principale
fen1 = Tk()

# creation des widget exclave
can1 = Canvas(fen1, bg='white', height=170, width=350)
can1.pack(side=LEFT)

bou1 = Button(fen1,text='Quitter',command=fen1.quit)
bou1.pack(side=BOTTOM)

bou2 = Button(fen1, text='Anneau bleu', command=drawcirclebleu)
bou2.pack()
bou3 = Button(fen1, text='Anneau noir', command=drawcirclenoir)
bou3.pack()
bou4 = Button(fen1, text='Anneau rouge', command=drawcirclerouge)
bou4.pack()
bou5 = Button(fen1, text='Anneau jaune', command=drawcirclejaune)
bou5.pack()
bou6 = Button(fen1, text='Anneau vert', command=drawcirclevert)
bou6.pack()


fen1.mainloop()

fen1.destroy()