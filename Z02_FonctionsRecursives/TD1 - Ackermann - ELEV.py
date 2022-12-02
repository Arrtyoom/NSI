

def A(m,n):
    """ Fonction d'Ackermann, définie par:
        	Cas 1 : si m>0 et n=0, 	A(m,n) = A(m-1,1)
        	Cas 2 : si m>0 et n>0,	A(m,n) = A(m-1,A(m,n-1) )
        	Cas 3 : si m=0 et n≥0,	A(m,n) = n+1

        @m, @n:  nombres entiers quelconques
        @throw:  ValueError dans les cas non définis ci-dessus
        @return: Ackermann(m,n)
    """

    if n<0 or m<0:
        raise ValueError

    def rec(m,n):

        if m > 0 and n == 0:
            return rec(m-1,1)

        if m > 0 and n > 0:
            return rec(m-1,rec(m,n-1))

        if m == 0 and n >= 0:
            return n+1

    return rec(m,n)













def tests():

    TESTS = [            # (m, n, result)
        (1,1,3),
        (0,5,6),
        (4,0,13),
        (3,3,61),
    ]

    for m,n,exp in TESTS:
        act = A(m,n)
        assert act==exp, "A({},{}): {} should equal {}".format(m,n,act,exp)
    else:
        print('ok')


    TESTS = [
        (5,-2),
        (-42,0),
        (-1,-1),
    ]

    for m,n in TESTS:
        threw = True
        try:
            A(m,n)
            threw = False
        except ValueError:
            pass
        assert threw, "Should have thrown ValueError()"
    else:
        print('ok (ValueError tests)')

tests()

