"""
Interface & représentation d'une liste chaînée:

    * Une liste chaînée vide sera ici représentée par la valeur None

    * un élément/maillon d'une liste chaînée est un tuple de longueur 2:

            (valeur, suite de la chaîne ou None)

    * la tête de la liste est "à gauche":

         tête-> queue     <=>     1 -> 2 -> 3 -> None

         Cette liste chaînée est donc implantée avec:
            (1, (2, (3, None)))
"""

from typing import NewType, List


LinkedList = NewType('LinkedList', tuple)



def creer_vide() -> LinkedList:
    """ Crée une liste chaînée vide... (oui, c'est une fonction qui ne sert pas
        à grand chose à 1ère vue... :p )
    """
    return None


def ajoute_tete(v:int, linked:LinkedList) -> LinkedList:
    """ ajoute_tete un maillon avec la valeur v à l'avant de la liste chaînée linked """
    return (v,linked)


def tete(linked:LinkedList) -> int:
    """ Renvoie la valeur portée par le maillon à la tête de la liste """
    return linked[0]


def queue(linked:LinkedList) -> LinkedList:
    """ Renvoie la queue du maillon en cours (=la liste chaînée sans le maillon de tête) """
    return linked[1]


def est_vide(linked:LinkedList) -> bool:
    """ Indique si la liste chaînée passée en argument est vide ou non """
    return linked == creer_vide()



#------------------------------



def to_linked_list(lst:List[int]) -> LinkedList:
    """ Convertit une liste d'entiers en liste chaînée:
            [1,22,34]  =>   1 -> 22 -> 34 -> None
        Le premier élément de la liste doit donc être la tête de la liste chaînée.
    """

    linked = creer_vide()
    for v in reversed(lst): ##for v in lst[::-1]:
        linked = ajoute_tete(v,linked)
    return linked




def taille(linked:LinkedList) -> int:
    """ Renvoie la taille de la liste chaînée (nombre de maillons):
            Ex:      a   <=>   1 -> 22 -> 34 -> None
                     taille(a) == 3
    """
    """
    longueur = 0
    if not est_vide(linked): # cas recursif
        longueur += 1
        return(taille(queue(linked)))
    return longueur
    """

    if est_vide(linked):
        return 0
    else:
        couper = queue(linked)
        regner = taille(couper)
        combiner = regner + 1
        return combiner








def somme(linked:LinkedList) -> int:
    """ Renvoie la somme des valeurs de la liste chaînée:
            Ex:      a   <=>   1 -> 22 -> 34 -> None
                     somme(a) == 57
    """

    """ version 0 
    S = 0
    copie = copy.deepcopy(linked)
    print(copie)

    #if est_vide(copie):
    #   return 0
    
    while type(copie[1]) == tuple:
         
        print("element",copie[0])
        S += copie[0] 
        print("somme",S)
        copie = queue(copie)

    return S + copie[0]
    """

    """version 1"""
    if est_vide(linked):
        return 0
    else:
        couper = queue(linked)
        regner = somme(couper)
        combiner = tete(linked) + regner
        return combiner
    
    











def get(linked:LinkedList, i:int) -> int:
    """ Renvoie la valeur du maillon à l'index i (indexation à 0):
            Ex: soit lkl la liste chaînée:    1 -> 22 -> 34 -> None
                get(lkl, 0) == 1
                get(lkl, 2) == 34
                get(lkl, 3) => Exception
    """

    """version 1
    """
    while i != 0:
        
        linked = queue(linked)
        i -= 1

        if tete(linked)==None:
            return Exception
    
    return tete(linked)
    """version recursive
    if i == 0: return tete(linked)
    else: return get(linked(queue(linked)),i-1)
    """



def to_list(a, lst):
    for i in range(taille(a)):
        lst.append(get(a,i))
    return lst



def concat(a:LinkedList, b:LinkedList) -> LinkedList:
    """ Concatène les deux listes chaînées a et b, en ajoutant b à la fin de a:

            a  <=>  1 -> 2 -> 3 -> None
            b  <=>  4 -> 5 -> None

            concat(a,b)  ==  1 -> 2 -> 3 -> 4 -> 5 -> None
    """

    #creer list vide
    #ajouter les valeurs en partant des dernieres valeurs de b puis celle de a 
    #retourner la list concatener 

    """
	#Version Iterative

    lst = []
	
    to_list(a, lst)
    to_list(b, lst)

    c = creer_vide()
    for v in reversed(lst):
        c = ajoute_tete(v,c)
    
    return c
	"""
	#Version Recursive

    if est_vide(a):
        return b
    else:
        couper   = queue(a)
        regner   = concat(couper)
        combiner = ajoute_tete( tete(a) , regner )
        return combiner


    """version 0
    c = creer_vide()
    print(a,b,c)
    
    for i in range(taille(b),0):

        v = get(i)
        ajoute_tete(v,c)
        print(v,c)

    print(c)
    return c
    """
    

        












#-----------------------------------------------------------
#-----------------------------------------------------------
#-----------------------------------------------------------




def tests():
    class Nope(Exception): pass
    def assert_equal(act,exp,msg=''):
        msg += ': '*bool(msg) + "{} should equal {}".format(act,exp)
        assert exp==act, msg
    def ok(msg=''):
        print(msg + ' ok')
    def unlinked(linked):
        lst = []
        while linked:
            lst.append( tete(linked) )
            linked = queue(linked)
        return lst
    #----------------------------------------------------------


    vide = creer_vide()
    ok('creer_vide()' + str(vide))


    a = ajoute_tete(3,vide)
    b = ajoute_tete(2,a)
    c = ajoute_tete(1,b)

    for i,linked in enumerate((c,b,a)):
        exp = [1,2,3][i:]
        assert_equal(unlinked(linked), exp, 'Your linked list was: '+str(linked))
    ok('ajoute_tete(v, linked)')


    for v,linked in ((3,a), (2,b), (1,c)):
        assert_equal(tete(linked), v)
    ok('tete(linked)')


    linked = c
    for i in range(3):
        exp = [1,2,3][i:]
        assert_equal(unlinked(linked), exp, 'Your linked list was: '+str(linked))
        linked = queue(linked)
    ok('queue(linked)')


    for linked in (a,b,c, vide):
        assert_equal(est_vide(linked), linked == vide, 'Your linked list was: '+str(linked))
    ok('est_vide(linked)')


    #------------------------------------------------


    TESTS = (
        [1,2,3,5,6,54],
        [1,1,1,1,2],
        [],
        [33],
    )
    for lst in TESTS:
        linked = to_linked_list(lst[:])
        assert_equal(unlinked(linked), lst, 'Your linked list was: '+str(linked))
        if not lst:
            assert_equal(linked, vide, 'Your linked list was: '+str(linked))
    ok('to_linked_list(lst)')


    for lst in TESTS:
        linked = to_linked_list(lst[:])
        assert_equal(taille(linked), len(lst), 'Your linked list was: '+str(linked))
    ok('taille(linked)')


    for lst in TESTS:
        linked = to_linked_list(lst[:])
        assert_equal(somme(linked), sum(lst), 'Your linked list was: '+str(linked))
    ok('somme(linked)')


    for lst in TESTS:
        linked = to_linked_list(lst[:])
        for i,v in enumerate(lst):
            assert_equal(get(linked,i), lst[i], 'Your linked list was: '+str(linked))
        try:
            get(linked, len(lst))
            raise Nope('should have raised an exception of any kind')
        except Nope as nope:
            raise nope
        except:
            pass
    ok('get(linked, i)')


    TESTS = [
        ([], []),
        ([1], [2]),
        ([2], [1]),
        ([], [33]),
        ([42], []),
        ([1,2,3], [4,5,6,8,2,4,9]),
        ([5,5,4,8,2,1,8,5,2,8], [2,87,1]),
    ]
    for a,b in TESTS:
        link1 = to_linked_list(a)
        link2 = to_linked_list(b)

        actual = concat(link1, link2)
        assert_equal(unlinked(actual), a+b, 'Your linked list was: '+str(linked))
    ok('concat(a,b)')


tests()


