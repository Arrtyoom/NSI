


def extract_pairwise(iter1,iter2):
    """ Parcourt deux iterables de longueurs quelconques, contenant des données,
        et renvoie une liste avec tous les éléments qui sont identiques dans les
        deux itérables à la même position/index:

            iter1 = (1, 2, 3,  4)
            iter2 = (1, 4, 3, -9)
            => renvoie [1,3]

        @iter1:  une séquence indexable (list, tuple, string)
        @iter2:  une séquence indexable (list, tuple, string), de même type qu'iter1
        @return: une liste contenant les valeurs présentes aux mêmes indexes
                 dans les deux iterables.
    """

    result = []
    for i in range(len(iter1 if iter1 < iter2 else iter2)):
        if iter1[i] == iter2[i]:
            result.append(iter1[i])
    return result


def extract_pairwise(iter1,iter2):
    # Redéclarer la fonction et la code avec une list comprehension (vous aurez
    # besoin de 2 lignes de code dnas la fonction, cette fois, pour faire les choses
    # proprement):

    result = [ iter1[i] for i in range(len(iter1 if iter1 < iter2 else iter2)) if iter1 == iter2 ]














def tests():
    TESTS = [
        ([2,58,9,2,46,2],       # iter1
         [2,58,9,2,46,2],       # iter2
         [2,58,9,2,46,2]),      # expected

        ([58,9,2,46,2],
         [2,58,9,2,46],
         []),

        ('abcde',
         'acdbe',
         ['a','e']),

        ((2,58,9,2,46,2),
         (2,58,9,-2,46,2),
         [2,58,9,46,2]),

         ('','',[]),            #iter1,iter2,expected
         ('dfhd','',[]),
         ('','dfhd',[]),
         ('dfhd','d',['d']),
         ('fhd','d',[]),
         ('df','dfhd',['d','f']),
    ]

    for iter1,iter2,expected in TESTS:
        actual = extract_pairwise(iter1[:],iter2[:])
        print('''
---------------
iter1 = {}
iter2 = {}
epxtected: {}
returned:  {}
    '''.format(iter1,iter2,expected,actual))
        assert actual==expected, 'Nope!'

    print('ok')


tests()


