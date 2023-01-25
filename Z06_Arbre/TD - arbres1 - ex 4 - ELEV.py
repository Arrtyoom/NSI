
def est_feuille(tree):
    return tree[1] == []


def taille(tree):
    """ Renvoie le nombre de fichiers et de dossiers """
    return 1 if est_feuille(tree) else 1+sum(taille(enfant) for enfant in tree[1])


def hauteur(tree):
    """ Renvoie la hauteur de l'arbrorescence (arbre vide: h=0) """
    return 1 if est_feuille(tree) else 1+max(hauteur(enfant) for enfant in tree[1])


def nombre_fichiers(tree):
    """ Renvoie le nombre de fichiers de l'arborescence """
    return 1 if est_feuille(tree) else sum(nombre_fichiers(enfant) for enfant in tree[1])


def nombre_dossiers(tree):
    """ Renvoie le nombre de dossiers de l'arborescence """
    return 0 if est_feuille(tree) else 1 + sum(nombre_dossiers(enfant) for enfant in tree[1])


def exist(tree, path):
    """ Indique si le dossier ou le fichier, donné avec son chemin complet,
        est présent dans l'arborescence ou pas.

            path = "C:/bla.py"  -> False
            path = "C:/Windows" -> True
            path = "D:/Windows" -> False
            path = "C:/Windows/uninstall.exe" -> True
            path = "C:/Windows/steam.exe" -> False

        Si l'arbre est vide on considère qu'on renvoie toujours False.
    """
    lst_noms = path.split('/')  # découpage du chemin en liste de segments
    children = [tree]           # pour homogénéiser + simplifier le raisonnement


    # HARDCODE

    #print(lst_noms)
    #print(children)
    #print(len(lst_noms))
    #print(len(children[0]))

    for obj in children:
        msg = f"{obj[0]}"
        #print(msg)
        if path == msg : return True

        for o in obj[1]:
            msg = f"{obj[0]}/{o[0]}"
            #print(msg)
            if path == msg : return True

            for p in o[1]:
                msg = f"{obj[0]}/{o[0]}/{p[0]}"
                #print(msg)
                if path == msg : return True
    return False

    # Fonction valid(liste d'enfants, indice du segment recherché):
    #     Si on a dépassé la fin de la liste de noms:
    #         ...? False
    #     Fin Si
    #     Pour chaque sous-arbre de la liste d'enfants:
    #         Si le nom du sous-arbre correspond au segment recherché:
    #             ...? True
    #         Fin Si
    #     Fin Pour
    #     ...?
    # Fin Fonction

    return ...














#-------------------------------------------------------------------------------
#                                   TESTS
#-------------------------------------------------------------------------------


def tests():

    def fresh():
        hack    = ["hack.msi", []]
        spritz  = ["spritz.cook", []]
        uninst  = ["uninstall.exe", []]
        steam   = ["steam.exe", []]
        eduP    = ["edupython.exe", []]
        bagels  = ["bagels.exe", []]
        meh     = ["meh", []]

        windows = ["Windows", [uninst]]
        programs= ["Programs", [eduP,steam]]
        nvidia  = ["NVidia", [bagels]]

        c = ["C:", [nvidia, programs, spritz, windows, hack, meh]]

        from collections import namedtuple
        Data = namedtuple('Data', 'tree isFile taille hauteur nombre_fichiers nombre_dossiers')

        return c, [
            Data(c, False, 11, 3, 7, 4),

            Data(nvidia, False, 2, 2, 1, 1),
            Data(windows, False, 2, 2, 1, 1),
            Data(programs, False, 3, 2, 2, 1),

            Data(bagels, True, 1, 1, 1, 0),
            Data(eduP, True, 1, 1, 1, 0),
            Data(steam, True, 1, 1, 1, 0),
            Data(uninst, True, 1, 1, 1, 0),
            Data(spritz, True, 1, 1, 1, 0),
            Data(hack, True, 1, 1, 1, 0),
            Data(meh, True, 1, 1, 1, 0),
        ]


    def assert_equal(act,exp,msg=''):
        msg += ': '*bool(msg) + "{} should equal {}".format(act,exp)
        assert exp==act, msg


    def assertError(f, msg='', cls=Exception):
        msg  += ': '*bool(msg) + "Should have raised an exception"
        threw = False
        try:
            f()
        except cls:
            threw = True
        assert threw, msg


    def assertNoError(f, msg='', expect=Exception):
        msg  += ': '*bool(msg) + "Shouldn't have raised any exception"
        threw = False
        try:
            f()
        except expect:
            threw=True
        assert not threw, msg


    def tell(what):
        print("""\
-----------------
Tests: {}
        """.format(what))



    #----------------------------------------------


    for f in (taille, hauteur, nombre_fichiers, nombre_dossiers):
        prop = f.__name__
        tell(prop)
        _,data = fresh()
        for d in reversed(data):
            assert_equal(f(d.tree), getattr(d,prop), "pour "+repr(d.tree[0]))
        else:
            print('ok')


    #----------------------------------------------

    tell("exist")

    TESTS = [
        (False, ""),
        (False, "HDD"),
        (True,  "C:"),
        (False, "C:/bla.py"),
        (True,  "C:/Windows"),
        (True,  "C:/Windows/uninstall.exe"),
        (False, "C:/Windows/steam.exe"),
        (False, "C:/Programs/steam"),
        (True,  "C:/Programs/steam.exe"),
        (False, "C:/Programs/steam.exe/gna!"),
    ]
    for exp,path in TESTS:
        tree,_ = fresh()
        print(f"{ path !r} should return: { exp }")
        assert_equal(exist(tree,path), exp)
    print('ok')

tests()


