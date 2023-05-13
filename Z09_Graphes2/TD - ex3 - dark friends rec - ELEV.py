from copy import deepcopy
from collections import deque
from typing import List


relations = {
    'Maggie':       ['Christopher', 'Cillian'],
    'Tom':          ['Heath'],
    'Christopher':  ['Maggie', 'Michael','Marion'],
    'Margo':        ['Cillian'],
    'Marion':       ['Christian', 'Cillian','Christopher'],
    'Cillian':      ['Marion', 'Maggie', 'Margo'],
    'Christian':    ['Morgan', 'Michael', 'Marion'],
    'Joseph':       ['Gary'],
    'Heath':        ['Tom'],
    'Morgan':       ['Christian'],
    'Anne':         ['Gary'],
    'Gary':         ['Anne', 'Joseph'],
    'Michael':      ['Christian','Christopher'],
    'Arnold':       [],
}

BASE = deepcopy(relations)      # don't touch that...


def en_relation(graphe, machin, truc):
    """ Prend un graphe en entrée, ainsi que deux personnes du graphe, et
        indique si ces peronnes se connaissent ou non.
    """
    # sac = File()
    # sac.enfile(machin)
    # vus = set()
    # vus.add(machin)
    #
    # while not sac.est_vide():
    #     noeud = sac.defile()
    #     if noeud == truc:
    #         return True
    #
    #     for voisin in graphe[noeud]:
    #         if voisin not in vus:
    #             sac.enfile(voisin)
    #             vus.add(voisin)
    # return False

    vus = set()

    def dfs(graphe, machin, truc, vus) -> bool:
        # cas de base
        if machin == truc:
            return True

        # cas recursif
        for voisin in graphe[machin]:
            if voisin not in vus:
                vus.add(voisin)
                if dfs(graphe, voisin, truc, vus): # si dfs -> False alors il continue
                    return True
        return False

    return dfs(graphe, machin, truc, vus)


def en_relation2(graphe, machin, truc):  # TODO
    """ Prend un graphe en entrée, ainsi que deux personnes du graphe, et
        indique si ces peronnes se connaissent ou non.
    """
    vus = set()

    def dfs(graphe, machin, truc, vus) -> bool:
        # cas de base
        if machin == truc:
            return True

        # cas recursif
        for voisin in graphe[machin]:
            if voisin not in vus:
                vus.add(voisin)
                if dfs(graphe, voisin, truc, vus):  # si dfs -> False alors il continue
                    return True
        return False

    return dfs(graphe, machin, truc, vus)


def composition_groupes(graphe) -> List[List[str]]:
    """ Prend en entrée un graphe représentant un réseau social, et renvoie
        la composition exacte de chaque groupe d'amis (sans trier).

        @graphe: dictionnaire de listes de successeurs
        @return: liste de liste de noms (List[List[String]]), chaque sous-liste
                 correspondant à un groupe. Ni la liste globale ni les sous-listes
                 ne sont triées.
    """

    def dfs(noeud, group, vus):
        ...                         # traitementssss
        for voisin in ...:
            if ...:
                ...


    groupes = ...
    vus = ...
    for ppl in graphe:
        if ...:
            group = ...             # ...
            ...
            dfs(ppl, group, vus)    # On parcourt la composante connexe en démarrant sur ppl

    return ...














#-------------------------------------------------------------------
#                              TESTS
#-------------------------------------------------------------------



def tests():

    def assert_equal(act,exp,msg=''):
        assert BASE==relations, "NAAAAAN!! J'ai dit de ne pas modifier le graphe..."
        msg += ': '*bool(msg) + "{} should equal {}".format(act,exp)
        assert exp==act, msg

    def tell(what):
        print("""\

-----------------
Teste: {}
""".format(what))

    def Test(show_name=True):
        def wrapper(func):
            if show_name: tell(func.__name__)
            func()
            print('ok')
        return wrapper


    # helpers:
    christopher,morgan,christian,michael,marion,cillian, maggie, margo, anne, gary, joseph, heath, tom, arnold ='''\
    Christopher Morgan Christian Michael Marion Cillian Maggie Margo Anne Gary Joseph Heath Tom Arnold'''.split()


    def relations_tests(func):

        @Test()
        def tests_relations():
            TESTS = [
                (morgan,christian, True),
                (morgan, tom, False),
                (margo,michael,True),
                (joseph,anne, True),
                (joseph,christopher,False),
                (arnold,christopher,False),
            ]
            for a,b,expected in TESTS:
                assert_equal(func(relations,a,b), expected)
                assert_equal(func(relations,b,a), expected)

    relations_tests(en_relation)
    relations_tests(en_relation2)


    @Test()
    def tests_composition_groupes():

        def order_compo(lst): return sorted(map(sorted,lst))

        EXP = order_compo([
            [morgan,christian,michael,marion,cillian,maggie,christopher,margo],
            [heath, tom],
            [anne, gary, joseph],
            [arnold],
        ])
        """ Donne: [['Anne', 'Gary', 'Joseph'],
                    ['Arnold'],
                    ['Christian', 'Christopher', 'Cillian', 'Maggie', 'Margo', 'Marion', 'Michael', 'Morgan'],
                    ['Heath', 'Tom'],
                   ]
        """

        actual = composition_groupes(relations)
        assert_equal(order_compo(actual), EXP)


tests()

