# coding: utf-8

f = open('table.txt', "w")
i, j = 1, 1

while j <= 20:
    print("table de " + str(j) + " :")
    while i <= 10:
        valeur = j * i
        print(str(valeur))
        f.write(" " + str(valeur))
        i = i + 1
    j = j + 1
f.close()