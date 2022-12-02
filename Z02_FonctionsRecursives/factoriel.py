# Créé par Elève, le 07/10/2022 en Python 3.7

from math import factorial

def factorielle(n):
    """
    Renvoie le factoriel de n
    exemple : 5! = 1*2*3*4*5 = 120
    """
    v = 1
    for i in range(1,n+1):
        v *= i
    return v

def fact(n):
    """
    Fonction recursive de factorielle
    s'appelle elle même
    """
    if n == 0:
        return 1
    return n * fact(n-1)








TESTS = [
(0,1),
(1,1),
(5,120),
]


for n,result in TESTS:

    actual = factorielle(n)
    msg = "fact({}): {} should equal {}".format(n,actual,result)
    assert actual == result, msg
    ##assert factorial(v) == factorielle(v),f"Erreur: is {factorielle(v)} should be {factorial(v)}"

print('ok')