# coding: utf-8

from tkinter import *
from math import sqrt

# Version avec des clics de sours

# 1 : planète rouge (Mars)
# 2 : planère bleue (Terre)
# echelle : 400 pixel = 76 million de kilomètre (distance Terre Mars)
# Le diamètre des planete n'est pas à l'échelle, mais le ration sont bons
# Rayon de mars : 3389,5 km = 20px, terre : 6371 km = 38px

def dist():
    'fonction qui renvoie la distance entre des deux planètes en millions de km'
    global x1, y1, x2, y2
    # calcul la distance Mars Terre en px
    dist = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    # converti la distance en millions de km
    dist = dist * 0.19
    return dist

def grav():
    'fonction qui renvoie la force de gravité en la Terre et Mars en Newton'
    global m1, m2
    const_grav = 6.67428 / 10**11
    grav = const_grav * m1 * m2 / (dist() * 10**6)**2
    return grav

# reste à programmer : la fonction de déplacement et les boutons
# pour avancer Mars

def avance_mars(gd, hb):
    global x1, y1, r1
    x1, y1 = x1 + gd, y1 + hb
    can1.coords(mars, x1 - 20, y1 - 20, x1 + 20, y1 + 20)
    valDis.configure(text='Distance Terre - Mars : ' +
      str(dist()) + ' millions de km')
    valGrav.configure(text='Force de gravité Terre - Mars : ' +
      str(grav()) + ' Newtons')


def depl_gauche_mars():
    avance_mars(-10, 0)

def depl_droite_mars():
    avance_mars(+10, 0)

def depl_haut_mars():
    avance_mars(0, -10)

def depl_bas_mars():
    avance_mars(0, +10)
    


def avance_terre(gd, hb):
    global x2, y2, r2
    x2, y2 = x2 + gd, y2 + hb
    can1.coords(terre, x2 - 38, y2 - 38, x2 + 38, y2 + 38)
    valDis.configure(text='Distance Terre - Mars : ' +
      str(dist()) + ' millions de km')
    valGrav.configure(text='Force de gravité Terre - Mars : ' +
      str(grav()) + ' Newtons')


def depl_gauche_terre():
    avance_terre(-10, 0)

def depl_droite_terre():
    avance_terre(+10, 0)

def depl_haut_terre():
    avance_terre(0, -10)

def depl_bas_terre():
    avance_terre(0, +10)

# --------------Programme principal-------------------

# Variable globales


# cordonnées départ planete Mars, masse (kg), rayon (px)
x1, y1, m1, r1 = 300, 500, 6.39 * 10**23, 20   

# cordonnées départ planete Terre, masse (kg), rayon (px)
x2, y2, m2, r2 = 700, 500, 5.972 * 10**24, 38


# Création du widget principal
fen1 = Tk()
fen1.title('Gravitation Mars vs Terre')

# Création des widget esclaves
Label(fen1, text='Masse de Mars : 6,39e+23 kg').grid(row=1, column=1, columnspan=2)
Label(fen1, text='Echelle : 100px = 19 millions de km').grid(row=1, column=3, columnspan=4, sticky=W)
Label(fen1, text='Masse de la Terre : 5,972e+24 kg').grid(row=1, column=5, columnspan=6)

valDis = Label(fen1, text='Distance Terre - Mars : ' +
      str(dist()) + ' millions de km')
valDis.grid(row=3, column=1, columnspan=2)

valGrav = Label(fen1, text='Force de gravité Terre - Mars : ' +
      str(grav()) + ' Newtons')
valGrav.grid(row=3, column=5, columnspan=6)

can1 = Canvas(fen1, bg='black', height=1000, width=1000)
can1.grid(row=2, column=1, columnspan=6)
mars = can1.create_oval(x1 - 20, y1 - 20, x1 + 20, y1 + 20, fill='red')
terre = can1.create_oval(x2 - 38, y2 - 38, x2 + 38, y2 + 38, fill='blue')
Button(fen1, text='Quitter', command=fen1.quit).grid(row=4, column=3, columnspan=4, sticky=W)

# Button pour mars

Button(fen1, text='gauche', command=depl_gauche_mars).grid(
    row=4, column=1, sticky=E)
Button(fen1, text='droite', command=depl_droite_mars).grid(
    row=5, column=1, sticky=E)
Button(fen1, text='haut', command=depl_haut_mars).grid(row=4, column=2, sticky=W)
Button(fen1, text='bas', command=depl_bas_mars).grid(row=5, column=2, sticky=W)

# button pour la Terre

Button(fen1, text='gauche', command=depl_gauche_terre).grid(
    row=4, column=5, sticky=E)
Button(fen1, text='droite', command=depl_droite_terre).grid(
    row=5, column=5, sticky=E)
Button(fen1, text='haut', command=depl_haut_terre).grid(row=4, column=6, sticky=W)
Button(fen1, text='bas', command=depl_bas_terre).grid(row=5, column=6, sticky=W)

# démarrage du réceptionnaire d'évènement
fen1.mainloop()
fen1.destroy()