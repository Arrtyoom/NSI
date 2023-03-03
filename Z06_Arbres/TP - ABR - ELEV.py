from typing import List


class BSTree:

    #--------------------------------------------------------------------------
    # interdiction de toucher à cette partie...

    def __init__(self,v,l=None,r=None):
        self.value=v
        self.left=l
        self.right=r

    def __repr__(self):
        vals = [self.value, self.left, self.right]
        while vals[-1] is None: vals.pop()
        msg = ', '.join(repr(x) for x in vals)
        return "BSTree({})".format(msg)

    def __eq__(self, other):
        return( isinstance(other, BSTree)
                and self.value==other.value
                and self.left==other.left
                and self.right==other.right )

    #--------------------------------------------------------------------------
    # A vous de jouer:

    def est_feuille(self):
        return self.left and self.right

    def infixe(self):
        # cas de base
        if self.est_feuille(): return self.value

        # cas recursif
        operateur = self.value
        left_s = self.left.infixe()
        right_s = self.right.infixe()

        return ' {} {} {} '.format(left_s, operateur, right_s)

    def contient(self, v) -> bool :
        """ Renvoie un booléen indiquant si v est présent ou non dans l'arbre """
        # cas de base
        if v == self.value: return True
        # cas récursif 1
        if v < self.value and self.left  is not None: return self.left.contient(v)
        # cas récursif 2
        if v > self.value and self.right is not None: return self.right.contient(v)
        # cas par défaut
        return False

    def insert(self, v) -> 'BSTree' :
        """ Insère la valeur v à une place appropriée dans l'ABR.
            Les valeurs en doublon sont insérées à droite.
            Renvoie la racine de l'ABR après modification.

            @v: int
            @return: BSTree
        """
        # CONTRAINTE: INTERDICTION d'utiliser une fonction auxiliaire

        # if abr is None: return BSTree(v)
        #
        # if v < abr.value:
        #     child_G = insere(abr.left, v)
        #     abr.left = child_G
        # else:
        #     child_D = insere(abr.right, v)
        #     abr.right = child_D
        #
        # return abr

        if v < self.value: # cas de recursif 1
            if self.left is None:
                self.left = BSTree(v)
            else:
                self.left = self.left.insert(v)

        elif v > self.value: # cas de recursif 2
            if self.right is None:
                self.right = BSTree(v)
            else:
                self.right = self.right.insert(v)

        return self

    def to_sorted_list(self) -> List[int]:
        """ Transforme l'abr en une liste triée en ordre croissant. """

        lst = []

        # DFS
        













#**************************************************

def insere(abr, v) -> BSTree:
    """ Insère la valeur v à la place appropriée dans l'ABR passé en argument.
        Les valeurs en doublon sont ignorées.
        Renvoie l'abr après modification.

        @abr: BSTree ou None (pour l'arbre vide)
        @v: int
        @return: BSTree
    """
    # CONTRAINTE: le cas de base DOIT ÊTRE l'arbre vide

    if abr is None: return BSTree(v)

    if v < abr.value:
        child_G = insere(abr.left, v)
        abr.left = child_G
    else:
        child_D = insere(abr.right, v)
        abr.right = child_D

    return abr











def est_ABR(tree):
    """ Teste si l'arbre passé en agrument est un arbre binaire de recherche.

        @tree:   Un arbre binaire, avec les propriétés:
                    tree.value, tree.left, tree.right
        @return: (bool) True si c'est bien un ABR
    """
    raise NotImplementedError('TODO')

    # Sous fonction avec les arguments nécessaires en plus:
    def rec(tree, low, high) -> bool:
        pass










    return rec(..., ..., ...)       # <<<<< A METTRE A JOUR !





#******************************************************************




def testing():

    from random import randrange


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
        except Exception as e:
            msg += '\nExpected {} but was {} (error message printed below)\n{}'.format(cls, type(e),e)
        assert threw, msg


    def assertNoError(f, msg='', cls=Exception):
        msg  += ': '*bool(msg) + f"Shouldn't have raised {cls.__name__}"
        threw,e = False,''
        try:
            f()
        except cls as e:
            threw=True
            msg += "\nException thrown:\n{}".format(repr(e))
        except:
            pass
        assert not threw, msg


    def tell(what):
        print("""\

-----------------
Teste: {}
""".format(what))


    def Test(show_name=True):
        def wrapper(func):
            if show_name:
                tell(func.__name__)
            func()
            print('ok')
        return wrapper


#******************************************************************

    def fresh():
        """ NE PAS MODIFIER!

            Reconstruit l'arbre en page 2 du sujet. Les tests utilisent cette fonction
            et vous en aurez besoin tout à la fin du TP également.

        """
        return BSTree(7, BSTree(2,  BSTree(1),
                                    BSTree(4, BSTree(3),
                                              BSTree(6))),
                        BSTree(13, None,
                                   BSTree(22, BSTree(17))))

    @Test()
    def tests_contient():
        inside = {7,2,1,4,3,6,13,22,17}
        for n in range(25):
            exp = n in inside
            abr = fresh()
            assert_equal(abr.contient(n), exp)



#******************************************************************


    @Test(False)
    def tests_insertions():

        tree = BSTree(10, BSTree(5,  BSTree(2,  BSTree(0),
                                                BSTree(4)),
                                     BSTree(7,  BSTree(6),
                                                BSTree(8))),
                          BSTree(15, BSTree(12, BSTree(11),
                                                BSTree(13)),
                                     BSTree(17, BSTree(16),
                                                BSTree(18))))

        TESTS = [
            ((10,5),                BSTree(10, BSTree(5)) ),

            ((10,15),               BSTree(10, None,
                                               BSTree(15)) ),

            ((10,5,15),             BSTree(10, BSTree(5),
                                               BSTree(15)) ),

            ((10,5,2,0),            BSTree(10, BSTree(5,  BSTree(2,  BSTree(0)))) ),

            ((10,5,2,4),            BSTree(10, BSTree(5,  BSTree(2,  None,
                                                                     BSTree(4)))) ),

            ((10,15,17,16),         BSTree(10, None,
                                               BSTree(15, None,
                                                          BSTree(17, BSTree(16)))) ),

            ((10,15,12,13),         BSTree(10, None,
                                               BSTree(15, BSTree(12, None,
                                                                     BSTree(13)))) ),

            ((10,5,2,15),           BSTree(10, BSTree(5,  BSTree(2)),
                                               BSTree(15))              ),

            ((10,5,2,15,0,7,4),     BSTree(10, BSTree(5,  BSTree(2,  BSTree(0),
                                                                     BSTree(4)),
                                                          BSTree(7)),
                                               BSTree(15))              ),

            ((10,15,5,2,4,7,0),     BSTree(10, BSTree(5,  BSTree(2,  BSTree(0),
                                                                     BSTree(4)),
                                                          BSTree(7)),
                                               BSTree(15))              ),

            ((10,15,5,2,4,7,0,12,11,13,17,18,16,8,6), tree),
        ]

        tell('insere (fonction)')
        for values,exp in TESTS:
            abr = None
            for v in values:
                abr = insere(abr,v)
            msg = "Ordre d'insertion: {}\n".format(values)
            assert_equal(abr, exp, msg)
        else:
            print('ok')



        tell('insere (fonction) ignore les doublons')
        for values,exp in TESTS:
            abr = None
            for i,v in enumerate(values):
                abr = insere(abr,v)
                #abr = insere(abr, values[randrange(i+1)])
            msg = "Ordre d'insertion: {}\n".format(values)
            assert_equal(abr, exp, msg)
        else:
            print('ok')


        #-----------------------------------------


        tell('insert (méthode)')
        for values,exp in TESTS:
            head, *insertions = values
            abr = BSTree(head)
            for v in insertions:
                abr = abr.insert(v)
            msg = "Ordre d'insertion:\n  BSTree({}), puis insère:\n  {}\n".format(head, insertions)
            assert_equal(abr, exp, msg)
        else:
            print('ok')


        TESTS_DOUBLONS = [
            ((10,5,6),              BSTree(10, BSTree(5, None, BSTree(6))) ),

            ((0,2,1),               BSTree(0, None, BSTree(2, BSTree(1))) ),

            ((10,5,2,15,7,4),     BSTree(10, BSTree(5,  BSTree(2, None,
                                                                    BSTree(4)),
                                                          BSTree(7)),
                                               BSTree(15))              ),
        ]
        tell('insert (méthode): insère les doublons à droite')
        for values,exp in TESTS_DOUBLONS:
            head, *insertions = values
            abr = BSTree(head)
            for v in insertions:
                abr = abr.insert(v)
            msg = "Ordre d'insertion:\n  BSTree({}), puis insère:\n  {}\n".format(head, insertions)
            assert_equal(abr, exp, msg)



#******************************************************************


    @Test()
    def tests_to_sorted_list():

        abr=fresh()
        assert_equal(abr.to_sorted_list(), [1,2,3,4,6,7,13,17,22])
        print("Sur l'ABR du sujet (p.2): ok")


        TESTS = [
            [2, 17, 1, 18, 16, 10],
            [2, 8, 18, 0, 12, 5, 7],
            [11, 4, 15, 5, 14, 3, 9],
            [15, 0, 10, 17, 6, 9, 11],
            [16, 4, 2, 15, 11],
            [11, 7, 10, 0, 8, 13],
            [3, 17, 7, 18, 2, 4],
            [8, 13, 10, 0, 15, 1, 14],
            [1, 18, 10, 3, 6, 11, 8],
            [19, 8, 3, 11, 0, 18, 6],
        ]

        for vals in TESTS:
            abr = None
            for v in vals:
                abr = insere(abr,v)
            msg = f"ABR sans doublons créé par insertions successives de {vals}, abr.to_sorted_list():\n"
            act = abr.to_sorted_list()
            assert_equal(act, sorted(set(vals)), msg)
        print('Sur ABR sans doublons: ok')


        for vals in TESTS:
            head, *values = vals
            abr = BSTree(head)
            for v in values:
                abr = abr.insert(v)
            msg = f"ABR avec doublons créé par insertions successives de {vals}, abr.to_sorted_list():\n"
            act = abr.to_sorted_list()
            assert_equal(act, sorted(vals), msg)
        print('Sur ABR avec doublons: ok')



#******************************************************************


    @Test(False)
    def tests_est_abr():

        TESTS = [
        	( True , BSTree(10) ),                                 #0

        	( True , BSTree(10,   BSTree(5),
                                  BSTree(15)) ),

        	( True , BSTree(10,   BSTree(-10)) ),                  #2

        	( True , BSTree(10,   None,
                                  BSTree(22)) ),

        	( True , BSTree(-10,  BSTree(-20),                     #4
                                  BSTree(-5))   ),

        	( True , BSTree(10,   BSTree(5, None,
                                            BSTree(8))) ),

        	( True , BSTree(9,    None,                            #6
                                  BSTree(11, BSTree(10))) ),

        	( False , BSTree(10,  BSTree(11)) ),

        	( False , BSTree(10,  None,                            #8
                                  BSTree(8)) ),

        	( False , BSTree(-10, BSTree(20),
                                  BSTree(-5))  ),

        	( False , BSTree(-10, BSTree(-20),                     #10
                                  BSTree(-15))  ),

        	( False , BSTree(10,  BSTree(5),
                                  BSTree(8))  ),

        	( False , BSTree(9,   None,                            #12
                                  BSTree(11, None,
                                             BSTree(10))) ),
        ]

        tell('est_ABR, 1ère étape: arbre "courts"')
        for i,(exp,tree) in enumerate(TESTS):
            msg = '\n\nTest {} avec:\n{}\n'.format(i, tree)
            assert_equal(est_ABR(tree), exp, msg)
        else:
            print('ok')




        TESTS_DEEPER = [
            ( True , BSTree(10, BSTree(5,  BSTree(-1, BSTree(-2),           #0
                                                      BSTree(4)),
                                           BSTree(7,  BSTree(6),
                                                      BSTree(8))),
                                BSTree(15, BSTree(12, BSTree(11),
                                                      BSTree(13)),
                                           BSTree(17, BSTree(16),
                                                      BSTree(18)))) ),

            ( True , BSTree(10, BSTree(5,  BSTree(-1, BSTree(-2),           #1
                                                      None),
                                           BSTree(7,  BSTree(6),
                                                      BSTree(8))),
                                BSTree(15, BSTree(12, BSTree(11),
                                                      BSTree(13)),
                                           BSTree(17, BSTree(16),
                                                      BSTree(18)))) ),

            ( True , BSTree(10, BSTree(5,  BSTree(-1, None,                 #2
                                                      BSTree(4)),
                                           BSTree(7,  BSTree(6),
                                                      BSTree(8))),
                                BSTree(15, BSTree(12, BSTree(11),
                                                      BSTree(13)),
                                           BSTree(17, BSTree(16),
                                                      BSTree(18)))) ),

            ( True , BSTree(10, BSTree(5,  BSTree(-1, BSTree(-2),           #3
                                                      BSTree(4)),
                                           BSTree(7,  BSTree(6),
                                                      BSTree(8))),
                                BSTree(15, None,
                                           BSTree(17, BSTree(16),
                                                      BSTree(18)))) ),

            ( True , BSTree(10, BSTree(5,  BSTree(-1, BSTree(-2),           #4
                                                      BSTree(4)),
                                           BSTree(7,  BSTree(6),
                                                      BSTree(8))) ) ),

            ( True , BSTree(10, None,                                       #5
                                BSTree(15, BSTree(12, BSTree(11),
                                                      BSTree(13)),
                                           BSTree(17, BSTree(16),
                                                      BSTree(18)))) ),

            ( False , BSTree(10, BSTree(5,  BSTree(2,  BSTree(0),           #6
                                                       BSTree(1)),
                                            BSTree(7,  BSTree(6),
                                                       BSTree(8))),
                                 BSTree(15, BSTree(12, BSTree(11),
                                                       BSTree(13)),
                                            BSTree(17, BSTree(16),
                                                       BSTree(18)))) ),

            ( False , BSTree(10, BSTree(5,  BSTree(2,  BSTree(0),           #7
                                                       BSTree(4)),
                                            BSTree(7,  BSTree(5.1),
                                                       BSTree(6))),
                                 BSTree(15, BSTree(12, BSTree(11),
                                                       BSTree(13)),
                                            BSTree(17, BSTree(16),
                                                       BSTree(18)))) ),

            ( False , BSTree(10, BSTree(5,  BSTree(2,  BSTree(0),           #8
                                                       BSTree(4)),
                                            BSTree(7,  BSTree(5.1),
                                                       BSTree(12))),
                                 BSTree(15, BSTree(12, BSTree(11),
                                                       BSTree(13)),
                                            BSTree(17, BSTree(16),
                                                       BSTree(18))))  ),

            ( False , BSTree(10, BSTree(5,  BSTree(2,  BSTree(0),           #9
                                                       BSTree(4)),
                                            BSTree(7,  BSTree(5.1),
                                                       BSTree(9))),
                                 BSTree(15, BSTree(12, BSTree(-1),
                                                       BSTree(13)),
                                            BSTree(17, BSTree(16),
                                                       BSTree(18)))) ),

            ( False , BSTree(10, BSTree(5,  BSTree(2,  BSTree(0),           #10
                                                       BSTree(4)),
                                            BSTree(7,  BSTree(5.1),
                                                       BSTree(9))),
                                 BSTree(15, BSTree(12, BSTree(11),
                                                       BSTree(22)),
                                            BSTree(17, BSTree(16),
                                                       BSTree(18)))) ),

            ( False , BSTree(10, BSTree(5,  BSTree(2,  BSTree(0),           #11
                                                       BSTree(4)),
                                            BSTree(7,  BSTree(5.1),
                                                       BSTree(9))),
                                 BSTree(15, BSTree(12, BSTree(11),
                                                       BSTree(13)),
                                            BSTree(17, BSTree(9),
                                                       BSTree(18)))) ),

            ( False , BSTree(10, BSTree(5,  BSTree(2,  BSTree(0),           #12
                                                       BSTree(4)),
                                            BSTree(7,  BSTree(5.1),
                                                       BSTree(9))),
                                 BSTree(15, BSTree(12, BSTree(11),
                                                       BSTree(13)),
                                            BSTree(17, BSTree(16),
                                                       BSTree(16)))) ),

            ( False , BSTree(10, BSTree(5,  BSTree(2,  BSTree(0),           #13
                                                       BSTree(4)),
                                            BSTree(7,  BSTree(5.1),
                                                       BSTree(9))),
                                 BSTree(15, BSTree(12, BSTree(11),
                                                       BSTree(13)),
                                            BSTree(17, BSTree(5),
                                                       BSTree(18)))) ),
        ]

        tell('est_ABR, 2e étape: arbres plus profonds')
        for i,(exp,tree) in enumerate(TESTS_DEEPER):
            msg = '\n\nTest {}\n'.format(i)
            assert_equal(est_ABR(tree), exp, msg)
        else:
            print('ok')






    """  <<<  Supprimer pour activer le test

    @Test()
    def tests_to_descending_list():
        abr = fresh()
        act = abr.to_descending_list()
        assert_equal(act, sorted([1,2,3,4,6,7,13,17,22], reverse=True))
    #"""



    """  <<<  Supprimer pour activer le test

    @Test()
    def tests_v_in_tree():
        abr  = fresh()
        func = lambda: 25 in abr
        msg  = 'la "magic method" nécessaire pour "x in abr" n\'est pas implantée'
        assertNoError(func, msg)


        inside = {7,2,1,4,3,6,13,22,17}
        for n in range(25):
            exp = n in inside
            abr = fresh()
            act = n in abr
            assert_equal(act, exp)
    #"""

testing()


