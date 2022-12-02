
def deep_count(lst, x):
    """ Compte le nombre total d'occurrence de x dans lst, à n'importe
        quelle profondeur.

        @lst: toujours une liste (la fonction ne reçoit jamais un nombre au départ).
              Aucune info disponible sur la profondeur de recursion nécessaire.
        @x:   peut être n'importe quoi... (mais pas une liste)
        @return: int, nombre d'occurences.
    """

    """ version moi
    n = 0

    for v in lst:

        if type(v)!=list: #cas de base

            if v == x:
                n += 1

        else: #cas recursif



    return n

    """

    n = 0
    for v in lst:
        if v==x:
            n+=1
        elif isinstance(v,list):
            n += deep_count(v,x)
    return n

def deep_count(lst,x):
    sum( deep_count(v,x) if isinstance(v,list) else 1 if v==x else 0
        for v in lst )



def tests():

    TESTS = [
        # (lst, recherché, résultat)
        ([1, 1, 2, 1], 1,   3),
        ([1, 1, 2, [1, 1], [0,3], 1], 1,   5),
        ([1, 1, 2, [1, 1], [0,3], 1], 42,  0),
        ([1, 1, 0, [1, 1], [0,3], 1], 0,   2),
        ([[[[[[[[1, [], [1]]]]]]]]], 1,    2),
        ([], "2", 0),
        (["42"], "2", 0),
    ]

    for lst,n,exp in TESTS:
        lst2 = lst[:]
        act = deep_count(lst,n)
        assert lst2==lst, "NAN, on ne mute pas la liste passée en argument..."
        assert act==exp, "deep_count({},{}): {} should equal {}".format(lst,n,act,exp)
    else:
        print('ok')

tests()


