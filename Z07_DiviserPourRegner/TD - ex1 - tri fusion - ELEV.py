
"""
Définir une fonction partage(a:List[int]), qui prend en argument un tableau de
longueur quelconque, et "divise" ce tableau en deux. La fonction renvoie un tuple
contenant les deux moitiées du tableau initial.

Contraintes:
    - Ne pas muter le tableau passé en argument.
    - Ne jamais renvoyer le tableau d'origine.
"""


def partage(a: list) -> tuple:
    """
    fonction qui partage la liste en
    a en 2 liste egale b et c

    @param a: List[Int]
    @return:Tuple( 2 * List[Int] )
    """

    moitier = len(a) // 2
    b = a[:moitier]
    c = a[moitier:]
    return b, c


"""
Ecrire quelques tests simples pour la fonction partage:
    - Utiliser une simple boucle (=> pas de fonction dédiée)
    - Faire au minimum 4 tests (pas plus de 6)
    - Bien choisir les arguments des tests de manière à couvrir les cas
      particulier (il y en a 3 spécifiques à couvrir)
    - Penser à mettre un message de feedback, si un test échoue
"""

TESTS = [
    ([], ([], [])),
    ([1], ([], [1])),
    ([1, 2], ([1], [2])),
    ([1, 2, 3], ([1], [2, 3]),),
    ([1, 2, 3, 4], ([1, 2], [3, 4])),
]

for act, exp in TESTS:
    assert partage(act) == exp, f"return {act} should be {exp}"


"""
Créer la fonction fusion(a:List[int], b:List[int]) qui prend en argument 2
tableaux triés et renvoie un tableau également trié, qui est la fusion des
deux premiers tableaux, effectuée en temps linéaire.

Contraintes:
    - Ne pas muter le tableau passé en argument.
    - Ne jamais renvoyer un des tableaux d'origine.
    - Le tableau/la liste en sortie doit être initialisé à la bonne longueur
      dès le départ de votre fonction (donc interdit d'utiliser append/extend/pop).

REMARQUE: Les tests pour cette fonction sont déjà écrits
"""


def fusion(a: list, b: list) -> list:
    """
    fonction qui fusionne la liste triee
    a et b en une fonction triee result

    @param a: List[Int]
    @param b:  List[Int]
    @return: List[Int], resultat de la fusion de a et b
    """

    i, j = 0, 0
    result = [None for _ in range(len(a) + len(b))]

    for indice in range(len(result)):
        if not j < len(b) or (i < len(a) and a[i] < b[j]):
            result[indice] = a[i]
            i += 1
        else:
            result[indice] = b[j]
            j += 1
    return result


"""
Créer la fonction tri_fusion(lst:List[int]) qui prend en entrée un tableau
non trié et renvoie un tableau trié contenant les mêmes valeurs.

Contraintes:
    - Ne pas muter le tableau passé en argument.
    - Ne jamais renvoyer le tableau d'origine.

REMARQUE: Les tests pour cette fonction sont déjà écrits
"""


def tri_fusion(lst:list) -> list:
    """
    prend en argument une liste non triee et la
    renvoie triee

    @param lst: List[Int] non triee
    @return: List[Int] triee  a partir de la list lst
    """

    if len(lst) <= 1:  # cas de base
        return lst

    # cas recursif
    gauche, droite = partage(lst)
    g_triee = tri_fusion(gauche)
    d_triee = tri_fusion(droite)
    resultat = fusion(g_triee, d_triee)
    return resultat










def check():

    def assert_equal(act,exp,msg=''):
        msg += ': '*bool(msg) + "{} should equal {}".format(act,exp)
        assert exp==act, msg

    def tell(what):
        print("""\

-----------------
Test: {}
""".format(what))

    def Test(show_name=True):
        def wrapper(func):
            if show_name: tell(func.__name__)
            func()
            print('ok')
        return wrapper




    @Test()
    def test_fusion():

        TESTS_FUSION = [

            ([1,9,11],[2,4,13], [1,2,4,9,11,13]),

            ([],[], []),

            ([1,5,9],[], [1,5,9]),

            ([],[2,4,6], [2,4,6]),

            ([1,2,3],[4,12], [1,2,3,4,12]),

            ([1,2,3],[-1], [-1,1,2,3]),

            ([5],[1,9], [1,5,9]),

            ([5,6],[0,1,2,9,10,11,12], [0,1,2,5,6,9,10,11,12]),
        ]

        for a,b,exp in TESTS_FUSION:
            msg = "Fusion de {} avec {}".format(a,b)
            actual = fusion(a,b)
            assert_equal(actual, exp, msg)


    from random import randrange
    from itertools import product


    TESTS_TRI = [   # (input, output)

        ([4,1,3,9,3,8], [1,3,3,4,8,9]),

        ([0],[0]),

        ([],[]),

        ([2,1],[1,2]),

        ([3,1,2],[1,2,3]),

        ([3,4,1,5,2],[1,2,3,4,5]),

        ([1, 7, 8, 9, 11, 12, 15, 20, 22], [1, 7, 8, 9, 11, 12, 15, 20, 22]),

        ([1, 7, 8, 9, 11, 12, 15, 20, 22][::-1],  [1, 7, 8, 9, 11, 12, 15, 20, 22]),
    ]



    @Test()
    def tri_fusion_fixed_tests():
        for lst,exp in TESTS_TRI:
            ll=lst[:]
            act=tri_fusion(lst)
            assert ll==lst, "On a dit de ne pas muter les arguments........ xp"
            assert act==exp, "le tri de {} devrait donner: {} mais a donné: {}".format(ll,exp,act)



    def rndArr():
        return [ randrange(-100,100) for _ in range(randrange(10)) ]


    @Test()
    def tri_fusion_random_tests():
        for _ in range(100):
            lst = rndArr()
            exp = sorted(lst)
            act = tri_fusion(lst[:])
            assert act==exp, "le tri de {} devrait donner: {} mais a donné: {}".format(lst,exp,act)



    for func,n_args in (tri_fusion,1), (partage,1), (fusion,2):

        @Test(False)
        def test_():
            tell(f"Renvoie toujours une nouvelle instance: { func.__name__ }")
            inputs = [*product(([2],[],[1,5]), repeat=n_args)]
            for args in inputs:
                outputs = func(*args)

                if func is not partage:  # converts single outputs to tuples of size 1
                    outputs = (outputs,)

                args_id = {id(lst) for lst in args}
                outs_id = {id(lst) for lst in outputs}
                intersect = args_id & outs_id

                call = f"{ func.__name__ }({ ', '.join(map(str,args)) })"

                assert not intersect, "aucune des listes passées en argument ne devrait être renvoyée."+call

check()

