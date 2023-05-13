from copy import deepcopy
from collections import deque
from math import inf


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

class Pile:
    def __init__(self): self.__x = []
    def est_vide(self): return not bool(self.__x)
    def empile(self,v): self.__x.append(v)
    def depile(self):   return self.__x.pop()

class File:
    def __init__(self): self.__x = deque()
    def est_vide(self): return not bool(self.__x)
    def enfile(self,v): self.__x.append(v)
    def defile(self):   return self.__x.popleft()

def en_relation(graphe:dict[str,list[str]], machin:str, truc:str)-> bool:
    """ Prend un graphe en entrée, ainsi que deux personnes du graphe, et
        indique si ces peronnes se connaissent ou non.
    """
    sac = File()
    sac.enfile(machin)
    vus = set()
    vus.add(machin)

    while not sac.est_vide():
        noeud = sac.defile()
        if noeud == truc:
            return True
        
        for voisin in graphe[noeud]:
            if voisin not in vus:
                sac.enfile(voisin)
                vus.add(voisin)
    return False

def proximi_t(graphe:dict[str,list[str]], machin:str, truc:str)-> int:

    sac = File()
    sac.enfile((machin,0))
    vus = set()
    vus.add(machin)

    while not sac.est_vide():
        noeud,etape = sac.defile()
        if noeud == truc:
            return etape
        
        for voisin in graphe[noeud]:
            if voisin not in vus:
                sac.enfile((voisin,etape+1))
                vus.add(voisin)
    return inf

def nombre_de_groupes(graphe):
    """ Prend en entrée un graphe représentant un réseau social, et renvoie
        le nombre de groupes d'amis différents.

        @graphe: dictionnaire de listes de successeurs
        @return: nombre de groupes d'amis différents
    """
    compteur = 0
    vus = set()

    for noeud in graphe.keys():
        if noeud in vus:    continue
        else:
            compteur += 1

            sac = Pile()
            sac.empile(noeud)
            vus.add(noeud)

            while not sac.est_vide():
                noeud2 = sac.depile()

                for voisin in graphe[noeud2]:
                    if voisin not in vus:
                        sac.empile(voisin)
                        vus.add(voisin)
    return compteur

def composition_groupes(graphe):
    """ Prend en entrée un graphe représentant un réseau social, et renvoie
        la composition exacte de chaque groupe d'amis (sans trier).

        @graphe: dictionnaire de listes de successeurs
        @return: liste de liste de noms (List[List[String]]), chaque sous-liste
                 correspondant à un groupe. Ni la liste globale ni les sous-listes
                 ne sont triées.
    """
    groupes = []
    vus = set()

    for noeud in graphe.keys():
        if noeud in vus:    continue
        else:
            groupe = []; groupes.append(groupe)

            sac = Pile()
            sac.empile(noeud)
            vus.add(noeud)

            while not sac.est_vide():
                noeud2 = sac.depile()
                groupe.append(noeud2)

                for voisin in graphe[noeud2]:
                    if voisin not in vus:
                        sac.empile(voisin)
                        vus.add(voisin)
    return groupes














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
    christopher,morgan,christian,michael,marion,cillian,maggie,margo,anne,gary,joseph,heath,tom,arnold ='''\
    Christopher Morgan Christian Michael Marion Cillian Maggie Margo Anne Gary Joseph Heath Tom Arnold'''.split()



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
            assert_equal(en_relation(relations,a,b), expected)
            assert_equal(en_relation(relations,b,a), expected)


    @Test(0)
    def test_proximi_t():
        TESTS = [
            (heath, tom, 1),
            (gary, joseph, 1),
            (gary, anne, 1),
            (anne, joseph, 2),
            (arnold, christian, inf),
            (anne, christian, inf),
            (cillian, michael, 3),
            (margo, morgan, 4),
            (marion, christopher, 1),
        ]

        tell('proximi_t: A->B')
        for a,b,n in TESTS:
            act = proximi_t(relations,a,b)
            assert_equal(act, n, "{} et {} sont distants de {}".format(a,b,n))

        tell('proximi_t: A<-B')
        for a,b,n in TESTS:
            act = proximi_t(relations,b,a)
            assert_equal(act, n, "{} et {} sont distants de {}".format(b,a,n))


    @Test()
    def tests_nombre_groupes():
        n = nombre_de_groupes(relations)
        assert n==4, "il y a 4 groupes d'amis, mais {} trouvés à la place...".format(n)


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

