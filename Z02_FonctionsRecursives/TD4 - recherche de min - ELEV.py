"""
UTILISER LES FICHIERS PYTHON (avec EduPython):
    Ctrl+F9     lancer le programme (et donc les tests)
    Shift+F9    lancer le programme en mode de déboggage


-----------------------------------------------------------------------------

On recherche le minimum dans une liste de valeurs numériques. On va implanter
une fonction effectuant cette tâche de différentes façons. On part dans un
premier temps du principe que la liste n'est jamais vide.


1) implanter la fonction "min" ci-dessous avec la méthode de votre choix
   (interdit d'utiliser la fonction built-in... :p )

   Hint: Demandez-vous comment vous feriez "à la main" et identifiez ce dont
         vous allez avoir besoin en termes de code.

2) Une fois que les tests passent, réimplanter différemment la fonction (garder
   les versions précédentes, et redéclarer une nouvelle fois la fonction entre
   la dernière version et la fonction de tests). Au final, vous devriez avoir
   les trois versions ci-dessous:
        - boucle while
        - boucle for avec indices (ie. "range")
        - boucle for sans indices (ie. pas de "range")

------------

3) Dans la fonction de tests, changer le booléen de "test_question_3 = False"
   par True. Cela ajoute un test supplémentaire, pour lequel votre code doit
   pouvoir gérer les listes vides. On CHOISIT ici de renvoyer "+infini" si la
   liste est vide. Copiez/collez la dernière version de votre fonction et la
   modifier de manière à ce qu'elle passe les tests.
"""



def min(lst):
    """ Renvoie le minimum d'une liste non vide de nombres

        @lst:    liste de nombres (non vide)
        @return: la valeur minimale dans la liste


    Trame générale:

    best = ...
    # parcourir lst et pour chaque valeur:
        # si la valeur est plus faible que best:
            # remplacer best par la valeur en cours

    return best
    """

    """
    best = float('inf')
    for v in lst:
        if v < best:
            best = v
    return best

    best = float('inf')
    for i in range(len(lst)):
        if lst[i] < best:
            best = lst[i]
    return best
    """
    best = float('inf')
    i = 0
    while i < len(lst):         # for i in range(len(lst)):
        if lst[i] < best:
            best = lst[i]
        i += 1
    return best
    #"""


"""
def min(lst):
    recursivité: version 1
    complexité en temps O(N²)
    # cas de base
    if len(lst)==0:
        return float('inf')

    # cas recursif
    else:
        #couper
        couper = lst[1:]
        #régner
        regner = min(couper)
        #combiner
        combiner = lst[0] if lst[0] < regner else regner

        return combiner
    """

def min(lst,i=0):
    """
    recursivité: version 2

    """
    # cas de base
    if len(lst)==i:
        return float('inf')

    # cas recursif
    else:
        couper = i + 1                                      #couper
        regner = min(lst,couper)                            #régner
        combiner = lst[i] if lst[i] < regner else regner    #combiner

    return combiner


















def tests():

    INF = float('inf')
    TESTS = [               # [ (lst, expected), ...]
        ([1,2,3,5], 1),
        ([1,2,3,1,42,133,-5.999,412,-6], -6),
        ([999,-999,5], -999),
        ([INF], INF),
    ]
    for lst,expected in TESTS:
        lst2 = lst[:]
        actual = min(lst)
        assert actual==expected, "min({}): {} should equal {}".format(lst2, actual, expected)
        assert lst==lst2, "NAN! => ne jamais muter l'argument d'une fonction (sauf si explicitemnt autorisé)"


    test_question_3 = True

    if test_question_3:
        assert min([])==INF, 'Une liste vide devrait renvoyer float("inf")'

    print('ok')

tests()

