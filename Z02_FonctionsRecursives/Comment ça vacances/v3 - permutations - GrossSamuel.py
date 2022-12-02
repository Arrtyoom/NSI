# Créé par Elève, le 29/10/2022 en Python 3.7

"""
RAPPEL: pour définir un tuple de longueur 1, n'oubliez pas la virgule à rajouter
        impérativement à la fin:    tup_one = (1,)
"""

# Fonction permut(lst):
#     Si lst est vide:
#         Renvoyer une liste contenant un tuple vide
#     Fin Si
#
#     result = une liste vide
#     Pour chaque indices i possible de lst:
#         cut = liste contenant tous les éléments de lst autres que celui à l'index i
#         sub_perms = permut(cut)
#         Pour chaque sub contenue dans sub_perms:
#             combined = tuple contenant l'élément à l'index i concaténé avec sub
#             Ajouter combined à result
#         Fin Pour
#     Fin Pour
#     Renvoyer result
# Fin Fonction


""" version 1 """
def permut(lst):

    if len(lst) == 0:
        lst_v = [ () ]
        return lst_v

    result = []
    for i in range(len(lst)):

        cut = lst[:]
        del cut[i]

        sub_perms = permut(cut)
        for sub in sub_perms:

            combined = (lst[i],) + sub
            result.append(combined)
            """
                    Erreur trouver : me renvoyer (2,(3,(5,))) parce que je mettais
                    un tuple dans un tuple: (sub,)
                    Pour ca que j'ai opter pour l'atrocite: (list((lst[i],))+list(sub))

                FZ: je pense qu'en fait, c'est juste parce qu'au départ tu as dû essayer
                    (lst[i]) + sub   -> qui t'a donné une erreur et tu es alors parti sur les listes
                    alors que ce n'était que la virgule qui manquait pour avoir un tuple (alors que
                    "(lst[i])" est en fait la même chose que "lst[i]", donc c'est un entier, pas un
                    tuple, d'où le fait que tu ne peut pas le concaténer avec sub.
            """

    return result

def permut(lst,n=None):

    n = len(lst) if n == None else n

    if  n == 0: # cas de base
        lst_v = [ () ]
        return lst_v        # FZ: ok, bien (nota: le cas n==0 suffit)

        """ FZ: il n'y a qu'un seul cas de base, en fait """
##    if n == 1: # 2eme cas de base
##        result = []
##        for v in lst:
##            result.append((v,))
##        return result

    else: # cas recursif

        result = []
        for i in range(n):

            cut = lst[:]
            del cut[i]

            sub_perms = permut(cut)
            """ FZ: ton erreur est dna la ligne ci-dessus: tu doit passer n-1 en second argument
                    (voir l'indice de mon commentaire sur la version 1)
            """

            for sub in sub_perms:

                combined = (lst[i],) + sub
                """ FZ: ...
                    Indice: "régner"
                """
                result.append(tuple(combined))

        return result

#"""









def tests():

    from itertools import permutations

    TESTS = (
        [2,3,5],
        [],
        [1],
        [2,2,3],
        [1,2,3,4,5],
        [1,2,1,3,1],
    )
    for lst in TESTS:
        exp = list(permutations(lst))
        act = permut(lst[:])
        assert act==exp, "permut({}): {} should be {}".format(lst,act,exp)
    else:
        print('ok')


    """
    On veut maintenant implanter une variation de la fonction permut, qui permet
    de calculer toutes les permutations de N éléments pris dans l'argument lst:

        permut([2,3,5], 2) == [ (2,3), (2,5), (3,2), (3,5), (5,2), (5,3) ]

    On veut faire cela en réutilisant la fonction précédente, et elle doit toujours
    fonctionner pour le cas où la valeur de N n'est pas donnée lors de l'appel
    de la fonction.

    1) Ajouter "N" en tant qu'argument par défaut à votre fonction. La valeur par
       défaut DOIT être None

    2) Ajouter une instruction au tout début de la fonction qui met à jour la
       valeur de N si sa valeur est None pour lui donner la valeur correcte (à
       vous de trouver ce qu'elle est sensée être).
       Vérifiez que votre fonction passe toujours la première section de tests
       à ce stade.

    A ce stade, votre fonction doit être encore légèrement modifiée pour pouvoir
    passer les tests. Analysez ce qui se passe lors des appels pour trouver les
    2 modifications à apporter à votre fonction.

    CONSEIL: à ce stade, vous pouvez copier la boucle de tests ci-dessous juste
    après la définition de la variable TESTS, de manière à ce que vous puissiez
    plus facilement utiliser le mode de débogage (ainsi, vous ne ferez pas les
    tests de la première partie en premier).

    3) Avec l'introduction de N, le cas de base peut se présenter à d'autres
       moments: lesquels? modifier la condition en conséquence.

    4) A ce stade, il ne reste qu'à ajouter 2 (ou 3) caractères quelque-part
       dans votre fonction pour qu'elle permette de faire ce qu'on veut...
       A vous de jouer.
    """

    for lst in TESTS:
        for n in range(1,len(lst)+1):
            exp = list(permutations(lst, n))
            act = permut(lst[:], n)
            assert act==exp, "permut({}, {}): {} should be {}".format(lst,n,act,exp)
    else:
        print('ok')


tests()


