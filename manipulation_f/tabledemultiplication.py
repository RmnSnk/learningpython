# coding: utf-8

f = open('table.txt', "w")
i, j = 1, 1
print("Ecriture en cours")
while j <= 20:
    f.write("table de " + str(j) + " :")
    while i <= 10:
        valeur = j * i
        f.write(" " + str(valeur))
        i = i + 1
    f.write("\n")
    i = 0
    j = j + 1
f.close()
print("Ecriture terminée")
