# coding: utf-8

from tkinter import *

def drawcircle():
    'fonction qui va dessiner un cercle'
    global x1, y1, x2, y2, coul
    can1.create_oval(x1, y1, x2, y2, width=4, outline=coul)
    x1, y1, x2, y2, coul = 120, 10, 230, 110, 'black'
    can1.create_oval(x1, y1, x2, y2, width=4, outline=coul)
    x1, y1, x2, y2, coul = 240, 10, 340, 110, 'red'
    can1.create_oval(x1, y1, x2, y2, width=4, outline=coul)
    x1, y1, x2, y2, coul = 65, 60, 165, 160, 'yellow'
    can1.create_oval(x1, y1, x2, y2, width=4, outline=coul)
    x1, y1, x2, y2, coul = 175, 60, 275, 160, 'green'
    can1.create_oval(x1, y1, x2, y2, width=4, outline=coul)    
    

x1, y1, x2, y2, coul = 10, 10, 110, 110, 'blue'


# creation de la fenetre principale
fen1 = Tk()

# creation des widget exclave
can1 = Canvas(fen1, bg='white', height=300, width=600)
can1.pack(side=LEFT)

bou1 = Button(fen1,text='Quitter',command=fen1.quit)
bou1.pack(side=BOTTOM)
bou2 = Button(fen1, text='Tracer les anneaux', command=drawcircle)
bou2.pack()


fen1.mainloop()

fen1.destroy()