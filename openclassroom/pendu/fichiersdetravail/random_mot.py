# coding = utf-8

from random import randint

f = open("liste9854", "r")
i = 0
j = randint(0, 9853)

while i <= j:
    mot = f.readline()
    i += 1
f.close()

print(j)
print(mot)
