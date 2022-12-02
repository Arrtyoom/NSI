# Créé par Elève, le 09/10/2022 en Python 3.7

"""
1) Lire la spécification de la fonction à implanter puis, en partant uniquement
   de la structure "edges" définie dans la fonction "tests", dessiner le graphe
   correspondant, en considérant que le graphe est orienté.




2.1) Quel changement doit être opéré sur le schéma si la même structure ("edges")
     est utilisée pour définir un graphe non orienté, maintenant?




2.2) Quand on va implanter la fonction "edges_to_dict", que devra-t-on faire "en
     plus", si le graphe est considé comme non orienté?




3) Implanter la fonction "edges_to_dict"
"""


def edges_to_dict(edges, oriented=True):
    """ Prend en entrée une liste d'arcs ou d'arêtes pondérées et un argument
        indiquant si le graphe doit être considéré comme orienté ou non.
        Renvoie un dictionnaire de dictionnaires d'entiers ("successeurs"
        ou "voisins") représentant ce graphe.

        @edges:    Tuple de tuples (noeud de départ, noeud d'arrivée, poids)
                   Aucune garantie quant à l'ordre des arêtes/arcs.
        @oriented: Booléen indiquant si "edges" décrit un graphe orienté ou non.
        @return:   le graphe sous forme de "dict de dicts d'entiers"

        exemple: voir les tests ci-dessous
    """
    dct = {}

    for x,y,_ in edges:
        dct[x] = {}
        dct[y] = {}

    for x,y,z in edges:
        dct[x][y] = z
        if not oriented:
            dct[y][x] = z

    return dct














def tests():

    def assert_equal(act,exp,msg=''):
        msg += ': '*bool(msg) + "{} should equal {}".format(act,exp)
        assert exp==act, msg

    edges = (
         ('F', 'P', 1),     # (départ, arrivée, poids)
         ('W', 'Q', 2),
         ('F', 'Q', 5),
         ('Q', 'O', 8),
         ('J', 'O', 6),
         ('O', 'C', 6),
         ('J', 'C', 8),
         ('O', 'W', 3),
         ('W', 'J', 1),
         ('W', 'C', 1),
    )


    withOrient = {
         'C': {},
         'F': {'P': 1, 'Q': 5},
         'J': {'C': 8, 'O': 6},
         'O': {'C': 6, 'W': 3},
         'P': {},
         'Q': {'O': 8},
         'W': {'C': 1, 'J': 1, 'Q': 2},
    }

    act = edges_to_dict(edges, True)
    assert_equal(act, withOrient)
    print('ok')


    withoutOrient = {
         'C': {'J': 8, 'O': 6, 'W': 1},
         'F': {'P': 1, 'Q': 5},
         'J': {'C': 8, 'O': 6, 'W': 1},
         'O': {'C': 6, 'J': 6, 'Q': 8, 'W': 3},
         'P': {'F': 1},
         'Q': {'F': 5, 'O': 8, 'W': 2},
         'W': {'C': 1, 'J': 1, 'O': 3, 'Q': 2},
    }

    act = edges_to_dict(edges, False)
    assert_equal(act, withoutOrient)
    print('ok')

tests()

