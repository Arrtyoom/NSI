# Créé par Elève, le 09/10/2022 en Python 3.7

"""
Lire les spécifications de la fonction et jeter un oeil aux données dans les tests.


1) Représenter le graphe correspondant à la liste d'adjacence donnée dans
   l'exemple du docstring.

2) Représenter en vis-à-vis les deux structures de données du docstring, et
   mettre en évidence à quelle valeur dans la matrice d'adjacence correspond
   chaque valeur provenant de la liste d'adjacence (utiliser des couleurs).

4) Pourquoi la matrice d'adjacence ne contient que des 0 et des 1? qu'est-ce que
   cela implique sur le type de graphe en jeu?

5) Implantation de la fonction:
    A partir de cette question, vous pouvez essayer de rédiger le code sans lire
    les sous-questions suivantes, ou de vous en aider.

    a) Quelle est le type de la structure de données renvoyée (en termes de code)?

    b) Que peut-on dire des dimensions de la structure renvoyée?

    Une stratégie d'implantation de type: "préparation, modification, renvoi"
    est particulièrement appropriée, pour cette fonction.

    c) Que faut-il faire pour la "préparation"?

    d) Que faut-il faire pour l'étape "modification"? Combien de boucles
       nécessaires? Quels types de boucles? sur quelle(s) structure(s) de données?

Implanter la fonction.
"""



def list_to_mat(lst):
    """ Convertit une "liste de listes de successeurs" représentant un graphe
        non pondéré en une matrice d'adjacence.
        Dans la liste donnée en argument, les sommets sont identifiés par des
        nombres qui correspondent à leur indice dans la liste "lst".

        @lst:    Liste de listes d'entiers, les entiers représentant les indices
                 des successeurs du sommet correspondant à l'index en cours.
        @return: matrice d'adjacence NxN indiquant quels sont les voisins.

        exemple:
            list_to_mat([
               [1],     # sommet d'index/étiquette 0
               [1,2],   # sommet d'index/étiquette 1
               [2],     # sommet d'index/étiquette 2
            ])
            renvoie: [
               [0, 1, 0],
               [0, 1, 1],
               [0, 0, 1],
            ]
    """

    #creation d'une matrice vide
    taille = len(lst)
    M = [ [0] * taille for i in range(taille)]

    #mise a jour de la matrice vide
    for i in range(taille):
        for j in lst[i]:
            M[i][j] = 1

    return M










def tests():

    def assert_equal(act,exp,msg=''):
        msg += ': '*bool(msg) + "{} should equal {}".format(act,exp)
        assert exp==act, msg

    TESTS = [           # (matrice, graphe)
        ([[0, 0, 1, 1],
          [0, 0, 1, 1],
          [0, 1, 1, 0],
          [0, 0, 1, 0]],
          [[2, 3], [2, 3], [1, 2], [2]]),

        ([[1, 0, 0, 0, 0, 1],
          [1, 0, 1, 0, 0, 1],
          [1, 0, 0, 1, 1, 0],
          [0, 0, 0, 0, 0, 0],
          [1, 1, 0, 1, 1, 1],
          [0, 0, 1, 0, 1, 1]],
         [[0, 5], [0, 2, 5], [0, 3, 4], [], [0, 1, 3, 4, 5], [2, 4, 5]]),

         ([[0, 1, 0, 0, 0],
           [1, 0, 1, 1, 0],
           [0, 1, 0, 0, 1],
           [0, 1, 0, 0, 0],
           [0, 0, 1, 0, 0]],
         [[1], [0, 2, 3], [1, 4], [1], [2]]),
    ]

    all_good = True
    for matrice,graphe in TESTS:
        act = list_to_mat(graphe)
        assert_equal(act,matrice, 'matrice incorrecte')
    else:
        print('ok')

tests()

