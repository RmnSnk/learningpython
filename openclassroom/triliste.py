# coding = utf-8

fi = open("liste_mots_brute", "r")
fo = open("liste_mots_tri", "a")

for mot in fi:
    if len(mot) == 9:
        fo.write(mot)
    else:
        pass
fi.close()
fo.close()
    
print("Done!")

    