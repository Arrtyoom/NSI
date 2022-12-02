# Créé par Elève, le 15/09/2022 en Python 3.7

"""
import random

def createur_binnaire():
        for i in range(0,1):
"""


#-------------------------------
#version 2

def add(a,b):

    longueur = max(len(a), len(b))
    #print(longueur)

    a = a.zfill(longueur)
    b = b.zfill(longueur)
    #print(a,b)

    resultat = ''
    retenue = 0

    for i in range(longueur-1,-1,-1):
        #print(i)

       r = retenue

       r += 1 if a[i] == '1' else 0
       r += 1 if b[i] == '1' else 0

       resultat = ('1' if r % 2 == 1 else '0') + resultat
       retenue = 0 if r < 2 else 1

    if retenue != 0 : resultat = '1' + resultat

    return resultat.zfill(longueur)

"""
#-------------------------------
#version 1

def add(a,b):
    return (bin(int(a)) + bin(int(b)))
"""

#-------------------------------
#Programme

a = "1001001"
b = "101100"

print(add(a,b))