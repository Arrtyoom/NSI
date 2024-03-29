﻿from collections import deque


class Queue:
    """ Une Queue est représentée avec la TETE de la file A DROITE. """

    def __init__(self, iterable=()): self._q = deque(iterable)

    def __repr__(self): return f"Queue({self._q})"

    def enfile(self, v): self._q.appendleft(v)

    def defile(self):   return self._q.pop()

    def est_vide(self): return len(self._q) == 0


class Stack:
    """ Une Stack est représentée avec le TOP de la pile A DROITE """

    def __init__(self, iterable=()): self._pile = list(iterable)

    def __repr__(self): return f"Stack({self._pile})"

    def empile(self, v): self._pile.append(v)

    def depile(self):   return self._pile.pop()

    def est_vide(self): return len(self._pile) == 0


class Node:
    """ Partie de l'interface que vous avez le droit d'utiliser dans le TD:
            les propriétés (value, msg, left, right)
            node.est_mort()
            node.est_victorieux()
            node.est_feuille()
    """

    def __init__(self, name, msg, l=None, r=None):
        self.value = name
        self.msg = msg
        self.left = l
        self.right = r

    def est_mort(self):
        return self.msg.startswith('Meurt')

    def est_victorieux(self):
        return 'victorieux' in self.msg

    # ------------------------------------------------------------------------
    # Partie de l'interface réservée aux fonctions de tests et de génération:

    def est_feuille(self):
        return self.left is None and self.right is None

    def copy(self):
        if self.est_feuille():
            return Node(self.value, self.msg)
        else:
            return Node(self.value, self.msg, self.left.copy(), self.right.copy())

    def __repr__(self):
        return "Node({}, ...)".format(self.value)

    def __len__(self):
        return 1 + sum(len(child) for child in (self.left, self.right) if child)


def fresh():
    """ construit l'arbre de décision du jeu et renvoie la racine.
        Voir le fichier .PNG joint pour voir l'allure de l'arbre.
    """

    enterDungeon = Node('enter', "Prendre le couloir de gauche ou droite? (G/D)")
    torche = Node('torche', "Allumer la torche? (O/N)")
    dead1 = Node('dead1', "Meurt stupidement, ne voyant pas le piège sur la porte...")
    openD = Node('openD',
                 "Evite le piège sur la porte l'ouvre et voit le trésor. Prendre le trésor ou se méfier et observer? (T/O)")
    dead2 = Node('dead2', "Meurt stupidement, ne voyant pas l'hydre...")
    fight = Node('fight', "Combattre l'hydre? (O/N)")
    dead3 = Node('dead3', "Meurt dignement, tué par l'hydre...")
    dead4 = Node('dead4', "Meurt lâchement, fuyant l'hydre...")

    levier = Node('levier',
                  "Une impasse... Voit un vieux levier dont l'utilité n'est pas évidente... L'actionner? (O/N) Revient ensuite en arrière et prend l'autre couloir...")

    enterDungeon.right = levier
    enterDungeon.left = torche
    torche.right = dead1
    torche.left = openD
    openD.left = dead2
    openD.right = fight
    fight.left = dead3
    fight.right = dead4

    levier.right = torche.copy()
    levier.left = torche.copy()

    openCaptive = levier.left.left
    openCaptive.value = "openCaptive"
    openCaptive.msg = "Voit l'hydre enfermée dans sa cage. Prendre le trésor ou tuer l'hydre? (T/H)"
    openCaptive.left = Node('dead5',
                            "Meurt d'effroi en voulant prendre le trésor, lorsque l'hydre se met à hurler derrière ses barreaux...")
    openCaptive.right = Node('choice', "Voit l'hydre enfermée dans sa cage. Prendre le trésor ou tuer l'hydre? (T/H)")

    fight2 = openCaptive.right
    fight2.right = Node('dead6',
                        "Meurt effaré, lorsque l'hydre passe une tête entre les barreaux de sa cage et réussit tout de même à lui arracher un bras...")
    fight2.left = Node('winner', "Prend le trésor et ressort victorieux du château!")

    n = enterDungeon
    for _ in range(6):
        if n.right is None:
            n.right = Node('nope', '(dead end)')
        n = n.right

    return enterDungeon


# *******************************************************************************


def newbie(dungeon: Node):
    """ Reçoit un arbre de décision en entrée et recherche la mort ayant lieu
        le plus tôt possible dans le jeu (= en ayant fait le moins d'actions/de
        choix possible). Renvoie le message de la mort en question.

        @dungeon: (Node) arbre de décision du jeu
        @return:  (str)  message de la mort ayant lieu le plus tôt possible.
    """
    file = Queue()
    file.enfile(dungeon)

    while not file.est_vide():

        noeud = file.defile()

        if noeud.est_mort():
            return noeud.msg

        for enfant in [noeud.left, noeud.right]:
            if enfant is not None: file.enfile(enfant)


def newbie_details(dungeon: Node):
    """ Reçoit un arbre de décision en entrée et recherche la mort ayant lieu
        le plus tôt possible dans le jeu (= en ayant fait le moins d'actions/de
        choix possible). Renvoie le nombre d'actions "nécessaires" ainsi que le
        message de la mort en question, sous la forme d'un tuple.

        @dungeon: (Node) arbre de décision du jeu
        @return:  tuple(int, str)  nombre d'actions nécessaires et message pour
                  "mourrir au plus vite"
    """
    file = Queue()
    file.enfile((0, dungeon))

    while not file.est_vide():

        indice, noeud = file.defile()

        if noeud.est_mort():
            return indice, noeud.msg

        for enfant in [noeud.left, noeud.right]:
            if enfant is not None: file.enfile((indice + 1, enfant))


def diehard(dungeon: Node):
    """ Comme newbie, mais renvoie cette fois le message de la mort ayant lieu
        le plus tard possible (si plusieurs réponses sont possibles, prendre
        celle le plus à droite de l'arbre).
    """
    file = Queue()
    file.enfile(dungeon)
    last = ""

    while not file.est_vide():

        noeud = file.defile()

        if noeud.est_mort():
            last = noeud.msg

        for enfant in [noeud.left, noeud.right]:
            if enfant is not None: file.enfile(enfant)

    return last


def diehard_left(dungeon: Node):
    """ Renvoie cette fois un tuple(nombre d'actions, message) pour la mort
        "le plus tard possible", mais cette fois, le plus à GAUCHE de l'arbre.
    """
    file = Queue()
    file.enfile((0, dungeon))
    last = 0, ""

    while not file.est_vide():

        indice, noeud = file.defile()

        if noeud.est_mort():
            last = indice, noeud.msg

        for enfant in [noeud.right, noeud.left]:
            if enfant is not None: file.enfile((indice + 1, enfant))

    return last


def dfs_winner(dungeon: Node):
    """ Reçoit un arbre de décision en entrée et recherche le noeud permettant
        sortir victorieux du donjon. Renvoie le message du noeud en question.

        A FAIRE EN UTILISANT UN DFS ITERATIF.

        @dungeon: (Node) arbre de décision du jeu
        @return:  (str) message du noeud victorieux.
    """
    pile = Stack()
    pile.empile(dungeon)

    while not pile.est_vide():

        noeud = pile.depile()

        if noeud.est_victorieux():
            return noeud.msg

        for enfant in [noeud.left, noeud.right]:
            if enfant is not None: pile.empile(enfant)


def dfs_winner_rec(node: Node):
    """ Reçoit un arbre de décision en entrée et recherche le noeud permettant
        sortir victorieux du donjon. Renvoie le message du noeud en question.

        A FAIRE EN UTILISANT UN DFS RECURSIF.

        @dungeon: (Node) arbre de décision du jeu
        @return:  (str)  message victorieux
    """

    if node is None:
        return None

    if node.est_victorieux():
        return node.msg

    for enfant in [node.left, node.right]:
        result = dfs_winner_rec(enfant)
        if result is not None:
            return result
    return None


# *******************************************************************************


def tests():
    def assert_equal(act, exp, msg=''):
        msg += ': ' * bool(msg) + "{} should equal {}".format(act, exp)
        assert exp == act, msg

    def tell(what):
        print("""\

-----------------
Teste: {}""".format(what))

    def test_that(TESTS):
        for func, exp in TESTS:
            tell(func.__name__)
            act = func(fresh())
            assert_equal(act, exp)
            print('ok')

    test_that([
        (newbie, "Meurt stupidement, ne voyant pas le piège sur la porte..."),
        (newbie_details, (2, "Meurt stupidement, ne voyant pas le piège sur la porte...")),

        (diehard, "Meurt lâchement, fuyant l'hydre..."),
        (diehard_left, (5,
                        "Meurt effaré, lorsque l'hydre passe une tête entre les barreaux de sa cage et réussit tout de même à lui arracher un bras...")),
    ])

    test_that([
        (dfs_winner, "Prend le trésor et ressort victorieux du château!"),
        (dfs_winner_rec, "Prend le trésor et ressort victorieux du château!"),
    ])


tests()
