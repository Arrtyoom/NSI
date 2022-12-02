
##def fib(n):
##    if n < 0:
##        return 0
##    if n == 0:
##        return 1
##    if n > 0:
##        return fib(n-2) + fib(n-1)

def fib(n):
    """ Calcule le n-ième nombre de Fibonacci

        @n: nombre entier positif ou nul
        @return: nième nombre de la suite de Fibonacci
    """

    #docstring:
    #    1) decrire ce que fait la fonction
    #    2) decrire les arguments et leur domaine de validité
    #        (=> ce sont les préconditions)
    #    3) décrire la valeur renvoyée

    if n==0 or n==1:
        return 1
    return fib(n-2) + fib(n-1)








TESTS=[    # (n, expected)
    (0,1),
    (1,1),
    (2,2),
    (3,3),
    (4,5),
    (5,8),
    (6,13),
    (7,21),
    (8,34),
    (16,1597),
    (21,17711),
]
for n,expected in TESTS:
    actual = fib(n)
    assert actual==expected, "fib{}: {} should equal {}".format(n,actual,expected)
else:
    print('ok')

