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
    """
    """
    minimum = lst[0]
    for i in range(len(lst)):
        if lst[i] < minimum:
            minimum = lst[i]

    return minimum
    """
    """
    minimum = lst[0]
    for v in lst:
        if v < minimum:
            minimum = v

    return minimum
    """
    """
    minimum = lst[0]
    a = 0
    while a < len(lst):
        if lst[a] > minimum:
            minimum > lst[a]
        a += 1
        print(a)

    return minimum
    """
    """
    minimum = lst[0]
    i = 0
    while i < len(lst):
        if lst[i] < minimum:
            minimum = lst[i]
        i += 1
    return minimum
    """














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


    test_question_3 = False

    if test_question_3:
        assert min([])==INF, 'Une liste vide devrait renvoyer float("inf")'

    print('ok')

tests()

