
def affichage():
    from itertools import combinations
    def print_comb(lst, n):
        print('combinaisons de {} éléments pris dans {}'.format(n,lst))
        print( list(combinations(lst,n)) )
        print('----')

    lst = [1,2,3,4]

    if True:
        print('affichage:')
        print_comb(lst, 1)
        print_comb(lst, 2)
        print_comb(lst, 3)
        print_comb(lst, 4)

affichage()





def comb(data, n):
    """ Génère toutes les combinaisons de n éléments (n-uplets)
        pris dans la liste data

        @data:   liste de valeurs
        @n:      nombre
        @return: liste de tuples de toutes les combinaisons de n éléménts
    """
# 1  # Si la liste ne contient moins de n éléments:
# 2  #     Renvoyer une liste vide
# 3  # Ou Si n est nul:
# 4  #     Renvoyer une liste contenant un unique tuple vide
# 5  # Fin Si
# 6  #
# 7  # Assigner une liste vide à la variable "out"
# 8  # Assigner à une variable "size" le nombre d'éléments contenus dans data
# 9  #
#10  # Pour tous les indices i allant de 0 à size-n inclus:
#11  #
#12  #     Assigner à "current" un tuple de longueur 1 contenant l'élément à l'indice i de data
#13  #     Assigner à "lst" une liste contenant tous les éléments de data à droite de i (élément i exclus)
#14  #     Assigner à "sub_combs" le résultat de toutes les combinaisons de n-1 éléments pris dans lst
#15  #
#16  #     Pour chaque élément sub de sub_combs:
#17  #         Définir tup qui est la concaténation des tuples "current" et "sub" (dans cet ordre)
#18  #         Ajouter tup à out
#19  #     Fin Pour
#20  # Fin Pour
#21  #
#22  # Renvoyer out

    if len(data) < n:
        return []
    if n == 0:
        return [()]

    out = []
    size = len(data)

    for i in range(size-n+1):

        current = (data[i],)
        lst = data[i+1:
        sub_combs = comb(lst,n-1)

        for sub in sub_combs:
            tup = current + sub
            out.append(tup)

    return out
















def tests():

    from random import randrange as rand
    from itertools import combinations

    def assert_equal(act,exp,msg=''):
        msg += ': '*bool(msg) + "{} should equal {}".format(act,exp)
        assert exp==act, msg


    TESTS = [
        ([1,2,3,4], 0, [()]),
        ([1,2,3,4], 1, [(1,), (2,), (3,), (4,)]),
        ([1,2,3,4], 2, [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]),
        ([1,2,3,4], 3, [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]),
        ([1,2,3,4], 4, [(1, 2, 3, 4)]),
        ([1,2,3,4], 10, []),

    ]

    for lst, n, exp in TESTS:
        msg = "for {} and n={}".format(lst, n)
        act = comb(lst, n)
        assert_equal(act, exp, msg)
        assert_equal(lst, [1,2,3,4], "NAN, on ne mute PAS l'argument...")
    else:
        print('ok')

    for _ in range(20):
        n = rand(20)
        lst = [rand(-20,20) for _ in range(n)]
        exp = list(combinations(lst, n))
        act = comb(lst,n)
        assert_equal(act, exp, "for {} and n={}".format(lst, n))
    else:
        print('ok (random)')

tests()

