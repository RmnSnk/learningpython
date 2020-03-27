# coding: utf-8

from tkinter import *
from math import sqrt

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
Label(fen1, text='Masse de Mars : 6,39e+23 kg').grid(row=1, column=1)
Label(fen1, text='Echelle : 100px = 19 millions de km').grid(row=1, column=2)
Label(fen1, text='Masse de la Terre : 5,972e+24 kg').grid(row=1, column=3)
Label(fen1, text='Distance Terre - Mars : ' +
      str(dist()) + ' millions de km').grid(row=3, column=1)
Label(fen1, text='Force de gravité Terre - Mars : ' +
      str(grav()) + ' Newtons').grid(row=3, column=3)

can1 = Canvas(fen1, bg='black', height=1000, width=1000)
can1.grid(row=2, column=1, columnspan=3)
mars = can1.create_oval(x1 - 20, y1 - 20, x1 + 20, y1 + 20, fill='red')
terre = can1.create_oval(x2 - 38, y2 - 38, x2 + 38, y2 + 38, fill='blue')
Button(fen1, text='Quitter', command=fen1.quit).grid(row=4, column=2, sticky=S)



# démarrage du réceptionnaire d'évènement
fen1.mainloop()
