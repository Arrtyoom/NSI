# Créé par Elève, le 09/09/2022 en Python 3.7
"""
1) Compléter la fonction the_frog jusqu'à passer les tests
2) Compléter ensuite the_frog2:
    - bien lire le docstring: les spécifications ne sont pas les mêmes.
    - si le debugging pose trop de difficultés, passez au fichier suivant

Nota: Il y a qqes aides tout à la fin du fichier, pour vous donner un éventuel
      coup de pouce...
"""


def the_frog(lst):
    """ L'argument "lst" est une liste non vide d'entiers positifs.
        On suppose qu'un crapaud est au départ sur la première case (indice 0),
        et qu'il fait des bonds de cases en cases, la longueur du bond étant
        toujours égale à la valeur sur laquelle il est placé au moment de sauter.

        But: trouver combien de sauts doit faire le crapaud pour sortir de "lst",
             partant de l'indice 0.

        @lst:     liste d'entiers strictement positifs (jamais vide)
        @return:  nombre de sauts avant de sortir de la liste

        Ex: Positions successives (a,b,c,..) du crapaud pour la liste ci-dessous

                lst = [1,1,2,6,1,3,1,1]
            crapaud:   a>b>c> >d>e> > >f         => 5 sauts
    """

    nombre_saut = 0
    indice = 0
    nombre_delement = len(lst)

    while indice < nombre_delement:
        valeur = lst[indice]
        indice += valeur

        nombre_saut += 1
    print(nombre_saut)
    return nombre_saut

    """
    #- valeur = nombre de saut

    nombre_saut = 0

    for v in lst:

        attend = v

        if attend == 1:
            nombre_saut += 1

        attend -= 1

    print(nombre_saut)
    return nombre_saut
    """


















def test_frog():

    TESTS = [
        # (lst, expected)
        ([1,1,2,6,1,3,1,1], 5),
        ([1,1,1,1,1,1,1], 7),
        ([1,2,1,1,1,1,1], 6),
        ([10,1,1,1,1,1,1], 1),
        ([6, 1, 5, 4, 5, 3, 3, 1, 4, 6, 4], 3),
        ([2, 5, 1, 1, 5, 4], 4),
        ([3, 2, 6, 1, 2], 3),
        ([1, 5, 4, 3, 6, 3, 1, 2, 2, 2, 6, 3, 4], 6),
    ]
    for lst,exp in TESTS:
        print('''
---------------------------
lst = {}
expects n_sauts={}
            '''.format(lst,exp))

        act = the_frog(lst)
        assert exp==act, "Your answer: {}, should be: {}".format(act,exp)

    print(f'''

---------------------------
   Tests the_frog finis!
---------------------------
''')

test_frog()




#-------------------------------------------------------------




def the_frog2(lst):
    """ Même problème que précédemment, mais la liste "lst" contient cette fois
        des entiers quelconques. Renvoyer -1 si le crapaud ne peut pas sortir
        de "lst"

        @lst:    liste d'entiers
        @return: nombre de sauts nécessaires pour sortir de "lst" ou -1
    """

    #------------------------------------
    #version 4
    #complexite o(1) = T(N) = O(N) (N = longueur de la liste)
    #        au mieux       au pire

    nombre_saut = 0
    indice = 0
    nombre_delement = len(lst)
    historique = {}                 # historique = set()

    while indice < nombre_delement and indice >= 0:

        if indice in historique:
            return -1

        historique[indice] = None   # historique.add(indice)

        valeur = lst[indice]
        indice += valeur
        #print(indice)

        nombre_saut += 1

    #print(nombre_saut)
    return nombre_saut

    """


    #------------------------------------
    #version 3
    #complexite o(N) = T(N) = O(N) (N = longueur de la liste)
    #        au mieux       au pire

    nombre_saut = 0
    indice = 0
    nombre_delement = len(lst)
    historique = [False] * nombre_delement

    while indice < nombre_delement and indice >= 0:

        if historique[indice]:
            return -1

        historique[indice] = True

        valeur = lst[indice]
        indice += valeur
        #print(indice)

        nombre_saut += 1

    #print(nombre_saut)
    return nombre_saut


    #------------------------------------
    #version 2
    #complexite o(1) = T(N) = O(N²) (N = longueur de la liste)
    #        au mieux       au pire

    nombre_saut = 0
    indice = 0
    nombre_delement = len(lst)
    historique = [False]

    while indice < nombre_delement and indice >= 0:

        historique.append(indice)
        #print(historique)

        valeur = lst[indice]
        indice += valeur
        #print(indice)

        if indice in historique:
            #print(nombre_saut)
            return -1

        nombre_saut += 1

    #print(nombre_saut)
    return nombre_saut


    #------------------------------------
    #version 1
    #complexite o(N) = T(N) = O(N) (N = longueur de la liste)
    #        au mieux       au pire

    nombre_saut = 0
    indice = 0
    nombre_delement = len(lst)
    historique = []

    while indice < nombre_delement and indice >= 0:

        historique.append(indice)
        #print(historique)

        valeur = lst[indice]
        indice += valeur
        #print(indice)

        ## complexite en temps = n

        if nombre_saut > nombre_delement:
            return -1

        nombre_saut += 1

    #print(nombre_saut)
    return nombre_saut

    """












def test_frog2():

    TESTS = [
        # (lst, expected)
        ([-1,-1,-1,-1], 1),
        ([-1,-2,-1,-1], 1),
        ([1,1,0,1,1,1,1], -1),
        ([1,1,2,1,-2,1], -1),
        ([1,1,2,-1,-1,1], -1),
        ([1,1,1,1,1,1,1], 7),
        ([1,2,1,1,1,1,1], 6),
        ([1,2,0,1,1,1,1], 6),
        ([10,1,1,1,1,1,1], 1),
        ([6, 1, 5, 4, 5, 3, 3, 1, 4, 6, 4], 3),
        ([2, 5, 1, 1, 5, 4], 4),
        ([3, 2, 6, 1, 2], 3),
        ([1, 5, 4, 3, 6, 3, 1, 2, 2, 2, 6, 3, 4], 6),
        ([1], 1),
        ([-1], 1),
        ([0], -1),
        ([-100], 1),
        ([3,1,2,2,4,-4,-4,22,-7,1,6,12,-24,0,2,0], -1),
    ]
    for lst,exp in TESTS:
        print('''\
---------------------------
lst = {}
expects n_sauts={}
'''.format(lst,exp))

        act = the_frog2(lst)
        assert exp==act, "Your answer: {}, should be: {}".format(act,exp)

    print(f'''
---------------------------
   Tests the_frog2 finis!
---------------------------
''')

test_frog2()




"""
AIDES:
------


Pour la fonction the_frog:


    1) commencer par identifier les contraintes/informations pertinentes ou
       utiles pour le problème, puis se demander comment les représenter dans
       le code.

    2) Vu les préconditions du problème, à quoi correspond une "sortie de liste"
       pour le crapaud? Comment l'identifier dans le code?

    3) de quel(s) type(s) de structures de contrôles (dans le code) va-t-on avoir
       besoin pour résoudre le problème?





Pour la fonction the_frog2:

    * Si vous avez l'impression que l'interpréteur est bloqué, pensez à vérifier
    si le code est toujours en cours d'exécution ou non ("ampoule rouge" dans le
    coin inférieur droit d'EduPython)

    * Si le code ne termine pas... n'oubliez pas que le "petit carré rouge",
    en haut, vous permet d'interrompre le programme. Cherchez ensuite l'origine
    du problème dans votre code.

    => pensez à utiliser les outils de déboggage:
            - print là où ça vous semble utile dans le code
            - placez des points d'arrêt et utilisez "F9" pour lancer le mode
              de déboggage.
"""

