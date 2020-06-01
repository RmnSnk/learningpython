# coding = utf-8

fi = open("liste_mots_brute", "r")
fo = open("liste_mots_tri", "a")
i = 0

for mot in fi:
    if len(mot) == 9:
        fo.write(mot)
        i += 1        
    else:
        pass
    
fi.close()
fo.close()
    
print(f"Il y a {i} mots dans la liste")
print("Done!")

    