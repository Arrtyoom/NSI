from typing import List
from collections import deque


class Queue:
    def __init__(self): self.__x = deque()

    def is_empty(self): return not bool(self.__x)

    def enqueue(self, v): self.__x.append(v)

    def dequeue(self):   return self.__x.popleft()


class Stack:
    def __init__(self): self.__x = []

    def is_empty(self): return not bool(self.__x)

    def push(self, v): self.__x.append(v)

    def pop(self):   return self.__x.pop()


class OrientedGraphException(Exception):
    pass


# ------------------------------------------------------------------

def reachable(M: List[List[int]], start: int, end: int) -> bool:
    """ Cherche s'il est possible d'aller du noeud d'indice start au
        noeud d'indice end, dnas le labyrinthe représenté par la matrice
        d'adjacence M.

        @M:      matrice carrée NxN, représentant un graphe non pondéré
                 (orienté ou non)
        @start:  indice du sommet de départ
        @end:    indice du sommet d'arrivée
        @return: booléen indiquant s'il est possible d'aller de start à end.
    """
    # Utiliser une pile, pour cette fonction.
    bundle = Stack()
    bundle.push(start)
    marked = set()
    marked.add(start)

    while not bundle.is_empty():

        node = bundle.pop()

        if node == end: return True

        for i in range(len(M[node])):
            if M[node][i] == 1 and i not in marked:
                bundle.push(i)
                marked.add(i)

    return False


def path_finder(M: List[List[int]], start: int, end: int) -> List[int]:
    """ Recherche le chemin le plus court, de l'indice start jusqu'à l'indice
        end, dans un graphe représenté par la matrice d'adjacence M.

        @M:      matrice carrée NxN, représentant un graphe non pondéré
                 (orienté ou non)
        @start:  indice du sommet de départ
        @end:    indice du sommet d'arrivée
        @return: Une liste de tous les indices à traverser, dans l'ordre, pour
                 aller de start à end (start et end inclus). Si aucun chemin
                 n'existe, renvoyer une liste vide.
    """
    bundle = Queue()
    bundle.enqueue((start, [start]))
    marked = set()
    marked.add(start)

    while not bundle.is_empty():

        node, step = bundle.dequeue()

        if node == end: return step

        for i in range(len(M[node])):
            if M[node][i] == 1 and i not in marked:
                bundle.enqueue((i, step + [i]))
                marked.add(i)

    return []


def is_directed(M: List[List[int]]) -> bool:
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j] != M[j][i]: return False
    return True


def connexe_components(M):
    """ Commence par vérifier si le graphe est orienté ou non.
        Si le graphe est orienté, lève une exception OrientedGraphException
        (l'exception est définie pour vous au début du fichier, vous n'avez
        qu'à l'utiliser, comme une exception normale)
        Sinon, renvoie le nombre de composantes connexes du graphe.

        @M:      matrice d'adjacence représentant le graphe
        @throw:  OrientedGraphException si le graphe est orienté
        @return: nombre de composante connexes si le graphe est non orienté

        CONTRAINTES:
            * Utiliser une fonction à part, is_directed, renvoyant un boolean
              qui indique si le graphe est orienté ou non.
            * Lever l'exception depuis la fonction connexe_component
            * implantez le décompte des composantes connexes dans la fonction
              connexe_components en utilisant un parcours en profondeur.
            * utiliser un tableau de booléens pour marquer les noeuds comme vus.
    """
    if not is_directed(M): raise OrientedGraphException()

    N = 0
    marked = set()

    for node in range(len(M)):
        if node in marked:
            continue

        N += 1

        bundle = Stack()
        bundle.push(node)
        marked.add(node)

        while not bundle.is_empty():
            n = bundle.pop()
            for i in range(len(M[n])):
                if M[n][i] == 1 and i not in marked:
                    marked.add(i)
                    bundle.push(i)
    return N

def tests():
    TESTS = []  # list of tuples:
    #    (matrice, start, end, "a une solution", shortest size)

    M1 = ("M1",
          [[0, 1, 1, 1, 0, 0],
           [1, 1, 1, 0, 1, 1],
           [1, 1, 1, 1, 1, 0],
           [1, 0, 1, 1, 1, 1],
           [0, 1, 1, 1, 0, 1],
           [0, 1, 0, 1, 1, 1]])

    TESTS.append((M1, 0, 5, True, 3))
    TESTS.append((M1, 5, 0, True, 3))
    TESTS.append((M1, 2, 4, True, 2))
    TESTS.append((M1, 4, 2, True, 2))
    TESTS.append((M1, 2, 5, True, 3))
    TESTS.append((M1, 5, 2, True, 3))

    M2 = ("M2",
          [[1, 0, 1, 1, 0, 0, 0, 0, 1, 0],
           [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
           [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
           [1, 0, 1, 0, 1, 0, 1, 0, 0, 0],
           [0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
           [0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
           [0, 0, 1, 1, 1, 0, 0, 0, 0, 1],
           [0, 0, 1, 0, 1, 1, 0, 1, 0, 1],
           [1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
           [0, 1, 1, 0, 1, 1, 1, 1, 1, 0]])

    TESTS.append((M2, 1, 8, True, 3))
    TESTS.append((M2, 8, 1, True, 3))
    TESTS.append((M2, 7, 6, True, 3))

    M3 = ("M3",
          [[0, 0, 1, 0, 0, 0, 0],
           [0, 1, 0, 0, 0, 0, 0],
           [1, 0, 0, 0, 0, 1, 0],
           [0, 0, 0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 1],
           [0, 0, 1, 0, 0, 1, 0],
           [0, 0, 0, 0, 1, 0, 0]])

    TESTS.append((M3, 1, 4, False, 0))
    TESTS.append((M3, 0, 2, True, 2))
    TESTS.append((M3, 3, 0, False, 0))
    TESTS.append((M3, 5, 0, True, 3))
    TESTS.append((M3, 6, 4, True, 2))
    TESTS.append((M3, 4, 6, True, 2))

    M4 = ("M4",
          [[1, 1, 0, 0, 0, 0, 1],
           [1, 0, 0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 1, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [1, 0, 1, 0, 0, 0, 0]])

    TESTS.append((M4, 0, 0, True, 1))
    TESTS.append((M4, 1, 2, True, 4))
    TESTS.append((M4, 2, 1, False, 0))

    M5 = ("M5",
          [[1, 1, 0, 0, 0, 0, 1],
           [1, 0, 0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 1],
           [0, 1, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 1, 0],
           [0, 0, 0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0, 0, 0]])

    TESTS.append((M5, 0, 0, True, 1))
    TESTS.append((M5, 2, 3, True, 5))
    TESTS.append((M5, 3, 2, True, 5))

    def test_reachable():
        for (nomM, M), depart, fin, hasSol, size in TESTS:
            mat_str = '\n'.join(map(str, M))  # si on veut afficher la matrice

            print("--------\nmatrice {}:\n{}\ndepart: {}, fin: {}".format(nomM, mat_str, depart, fin))
            # affichage avant l'appel pour faciliter le débogage

            copyM = [r[:] for r in M]
            doable = reachable(copyM, depart, fin)
            assert doable == hasSol
        print('ok')

    test_reachable()

    def test_cherche(func):
        for (nomM, M), depart, fin, hasSol, size in TESTS:
            mat_str = '\n'.join(map(str, M))  # si on veut afficher la matrice

            print("--------\nmatrice {}:\n{}\ndepart: {}, fin: {}".format(nomM, mat_str, depart, fin))
            # affichage avant l'appel pour faciliter le débogage

            copyM = [r[:] for r in M]
            path = func(copyM, depart, fin)

            print("chemin trouvé: ", path)
            # affichage après l'appel pour connaître le résultat renvoyé avant
            # les vérifications

            msg = validate(M, path, depart, fin, hasSol, size)
            assert not msg, msg
        print('ok')

    def validate(M, path, depart, fin, hasSol, size):
        if not hasSol:
            if path:
                return "Il n'y a pas de chemin pour cette situation (mais a renvoyé {})".format(depart, fin, path)
            return ""

        if not path:
            return "pas de chemin renvoyé alors qu'une solution existe ({})".format(path)

        if len(path) != len(set(path)):
            return "il ne devrait pas y avoir d'indices en doublon dans le chemin: " + str(path)

        if path[0] != depart:
            return "Le chemin devrait démarrer au point de départ ({}): {}".format(depart, path)

        if path[-1] != fin:
            return 'Le chemin devrait terminer sur "fin" ({}): {}'.format(fin, path)

        if len(path) != size:
            return "le chemin n'a pas la bonne longueur: {} devrait être {}".format(len(path), size)

        for a, b in zip(path, path[1:]):
            if not M[a][b]:
                return "Impossible de passer de {} à {} (path={})".format(a, b, path)

        return ""

    test_cherche(path_finder)

    print('*****************')

    def connex():
        TESTS = [(M1, 1), (M2, 1), (M3, 4), (M4, -1), (M5, 2)]

        for (nom, M), N in TESTS:
            copyM = [r[:] for r in M]

            mat_str = '\n'.join(map(str, M))  # si on veut afficher la matrice
            print("--------\nComposantes connexes de {}:\n{}".format(nom, mat_str))
            # affichage avant l'appel pour faciliter le débogage

            if N < 0:
                try:
                    connexe_components(copyM)
                    assert False, "Graphe orienté: aurait dû lever une OrientedGraphException"
                except OrientedGraphException:
                    pass
            else:
                actual = connexe_components(copyM)
                assert actual == N, "Composantes connexes de {}: {} devrait être égal à {}".format(nom, actual, N)

    connex()


tests()
