# Créé par Elève, le 14/10/2022 en Python 3.7
# Créé par fzinelli, le 07/10/2022 en Python 3.7

def fact(n):
    """ renvoie la factorielle de n (n>=0):
            fact(4) == 24
    """
    f = 1
    for m in range(1,1+n):
        f *= m
    return f


def fact(n):

    f = 1
    while n>0:
        f *= n
        n -= 1
    return f

def fact(n):
    if n==0:
        return 1
    return n * fact(n-1)





TESTS = [
    # (argument de fatc(n), résultat),
    (0,1),
    (1,1),
    (4,24),
]

for n,result in TESTS:
    actual = fact(n)
    msg = "fact({}): {} should equal {}".format(n,actual,result)
    assert actual == result, msg







