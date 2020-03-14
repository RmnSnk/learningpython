# coding: utf-8


def inverse(ch):
    'fonction qui renvoi l inverse d un mot'
    i, invlist = 0, []
    while i < len(ch):
        invlist.append(ch[(len(ch) - 1 - i)])
        i = i + 1
    strl1 = ''.join(invlist)  # transforme une liste en str
    return strl1

    




cha = list(input('Saisissez un mot : '))  # lis() transforme un str en list


print(inverse(cha))
