# coding = utf-8

mot = "chapeaux"
liste_mot =list(mot)
mot_cache = ["*", "*", "*", "*", "*", "*", "*", "*"]
i = 0

choix = input("Lettre : ")

while i <= 7:
    if choix == liste_mot[i]:
        mot_cache[i] = choix
    i += 1

x = "".join(mot_cache)
print(x)
    