
class Node:

    """ Constructeur:
            3 arguments: valeur, gauche, droit.
            Les 2 derniers arguments prennent None par défaut.
            Trois propriétés, value, left et right.
    """
    def __init__(self, valeur, gauche=None, droit=None):
        self.value = valeur
        self.left = gauche
        self.right = droit

    def __str__(self):
        return f"""
    {self.value}
        L:{self.left}
        R:{self.right}
    """

    def est_feuille(self) -> bool:
        """ Indique si l'instance est une feuille ou non """
        return self.right is None and self.left is None

    def taille(self) -> int:
        """ Calcule la taille de l'arbre """

        if self.est_feuille():
            return 1

        else:
            somme = 1

            if self.left is not None:
                somme += self.left.taille()

            if self.right is not None:
                somme += self.right.taille()

        return somme

    def hauteur(self) -> int:
        """ Donne la hauteur de l'arbre """
        if self.est_feuille():
            return 1

        else:
            best = 0

            if self.left is not None:
                hauteurLeft = self.left.hauteur()
                best = hauteurLeft if best < hauteurLeft else best

            if self.right is not None:
                hauteurRight = self.right.hauteur()
                best = hauteurRight if best < hauteurRight else best

            return 1 + best

    def n_feuilles(self) -> int:
        """ Renvoie le nombre de feuilles de l'arbre """
        if self.est_feuille():
            return 1

        else:
            somme = 0

            if self.left is not None:
                somme += self.left.n_feuilles()

            if self.right is not None:
                somme += self.right.n_feuilles()

        return somme

    def n_non_feuilles(self) -> int:
        """ Renvoie le nombre de noeuds qui ne sont PAS des feuilles """
        if self.est_feuille():
            return 0

        else:
            somme = 1

            if self.left is not None:
                somme += self.left.n_non_feuilles()

            if self.right is not None:
                somme += self.right.n_non_feuilles()

        return somme

    def contient(self, value) -> bool:
        """ Indique si l'arbre ou un de ses sous-arbres contient la valeur
            passée en argument.
        """
        # S = [self]
        #
        # while S:
        #
        #     noeudActuel = S.pop()
        #
        #     if noeudActuel.value == value:
        #         return True
        #
        #     if noeudActuel.left is not None :  S.append(noeudActuel.left)
        #     if noeudActuel.right is not None:  S.append(noeudActuel.right)
        #
        # return False

        if self.value == value: return True

        if self.left is not None:
            if self.left.contient(value): return True
        if self.right is not None:
            if self.right.contient(value): return True

        return False

    def max(self) -> int:
        """ Renvoie le maximum de toutes les valeurs présentes dans l'arbre.
        """
        # S = [self]
        # best = 0
        #
        # while S:
        #
        #     noeudActuel = S.pop()
        #
        #     if noeudActuel.value > best:
        #         best = noeudActuel
        #
        #     if noeudActuel.left is not None :  S.append(noeudActuel.left)
        #     if noeudActuel.right is not None:  S.append(noeudActuel.right)
        #
        # return best

        if self.est_feuille():
            return self.value

        else:
            best = self.value

            if self.left is not None:
                maxLeft = self.left.max()
                best = maxLeft if best < maxLeft else best

            if self.right is not None:
                maxRight = self.right.max()
                best = maxRight if best < maxRight else best

            return best

    def prod(self) -> int:
        """ Renvoie le produit de toutes les valeurs présentes dans l'arbre.
        """
        if self.est_feuille():
            return self.value

        else:
            result = self.value

            if self.left is not None:
                result *= self.left.prod()

            if self.right is not None:
                result *= self.right.prod()

            return result




def tests():
    def err_msg(msg, base):
        return base if not msg else f'{msg}: {base}'

    def assert_equal(act, exp, msg=''):
        assert exp == act, err_msg(msg, "{} should equal {}".format(act, exp))

    def assertError(f, msg='', cls=Exception):
        threw = False
        try:
            f()
        except cls:
            threw = True
        assert threw, err_msg("Should have raised an exception", msg)

    def assertNoError(f, msg='', expect=Exception):
        threw = False
        try:
            f()
        except expect:
            threw = True
        except Exception as meh:
            pass
        assert not threw, err_msg("Shouldn't have raised an exception", msg)

    def tell(what):
        print("""\
-----------------
Tests: {}
        """.format(what))

    TREES = [
        Node(0),  # A

        Node(0,  # B
             None,
             Node(5)),

        Node(2,  # C
             Node(-6)),

        Node(42,  # D
             Node(23),
             Node(412)),

        Node(1,  # E
             Node(2),
             Node(3,
                  Node(4,
                       None,
                       Node(6)),
                  Node(42,
                       Node(-11)))),
    ]

    A, B, C, D, E = TREES
    CONTAIN_TESTS = [
        ('A', A, 0, True),
        ('A', A, 25, False),
        ('D', D, 23, True),
        ('D', D, 412, True),
        ('D', D, 232, False),
        ('E', E, 6, True),
        ('E', E, -11, True),
        ('E', E, 16, False),
        ('E', E, None, False),
    ]

    PATHS = [
        (True, [
            ('',),
            ('R',),
            ('L',),
            ('L', 'R'),
            ('L', 'RRL', 'RLR'),
        ]),
        (False, [
            (),
            ('',),
            ('',),
            ('',),
            ('', 'R', 'RL', 'RR'),
        ])
    ]

    tell('est_feuille')
    for exp, exp_paths in PATHS:
        for paths, tree, nom in zip(exp_paths, TREES, 'ABCDE'):
            for path in paths:
                node = tree
                for c in path:
                    node = getattr(node, 'right' if c == 'R' else 'left')
                assert_equal(node.est_feuille(), exp,
                             f'Arbre {nom}, valeur du noeud: {node.value}')

    EXPS = [
        # hauteur taille n_feuilles n_non_feuilles max prod
        (1, 1, 1, 0, 0, 0),
        (2, 2, 1, 1, 5, 0),
        (2, 2, 1, 1, 2, -12),
        (2, 3, 2, 1, 412, 397992),
        (4, 7, 3, 4, 42, -66528),
    ]

    def test_method(meth):
        tell(meth)
        func, i = getattr(Node, meth), i_method[meth]
        for n, tree in enumerate(TREES, 1):
            assert_equal(func(tree), EXPS[n - 1][i], f'Arbre {n}')
            # "func(tree)" est équivalent ici à "tree.method()"
        print('ok')

    def check_exist_method(meth, *args):
        tree = TREES[0]
        check = lambda: getattr(tree, meth)(*args)

        assertNoError(check, f"Méthode {meth} non définie", AttributeError)

        msg = f"On devrait maitenant pouvoir appeler la méthode {meth} avec {len(args)} argument"
        assertNoError(check, msg, TypeError)

    methods = 'hauteur taille n_feuilles n_non_feuilles max prod'.split()
    i_method = {meth: i for i, meth in enumerate(methods)}
    # tests pour hauteur, taille, n_feuilles et n_non_feuilles:
    for meth in methods[:-2]:
        test_method(meth)

    # Tests pour contient
    for nom, tree, value, exp in CONTAIN_TESTS:
        actual = tree.contient(value)
        neg = ' ne' if not exp else ''
        pas = ' pas' if not exp else ''
        msg = f"L'arbre {nom}{neg} contient{pas} la valeur {value}"
        assert_equal(actual, exp, msg)

    # tests pour max et prod:
    for meth in methods[-2:]:
        check_exist_method(meth)
        test_method(meth)

    tell('hauteur: argument par défaut + test des deux conventions')
    check_exist_method('hauteur', False)

    i = i_method['hauteur']
    for n, tree in enumerate(TREES, 1):
        assert_equal(tree.hauteur(False), EXPS[n - 1][i] - 1, f'Arbre {n}')


tests()
