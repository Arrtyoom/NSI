# Créé par Elève, le 09/10/2022 en Python 3.7


def dict_to_mat(graphe):
    """ Convertit un dictionnaire de listes de successeurs représentant un graphe
        non pondéré en une matrice d'adjacence et une liste d'étiquettes.

        @graphe:     dictionnaire de listes de successeurs. L'ordre n'est garanti
                     ni pour pour le dictionnaire, ni pour les listes.
        @return:     un tuple (matrice,etiquettes), où matrice est la matrice
                     d'adjacence NxN et etiquettes est la liste des étiquettes de
                     tous les sommets.
                     Les étiquettes doivent être triées et les indices de la matrice
                     doivent correspondre avec cette liste.

        exemple:
             {'A': ['B'],
              'C': ['B','C'],
              'B': ['C'],
              }

           ( [[0, 1, 0],
              [0, 0, 1],
              [0, 1, 1]], ['A', 'B', 'C'])
    """
    # Pour créer une liste triée à partir d'un itérable, utiliser:
    #       liste_triée = sorted( itérable )

    #trouver etiquettes
    etiquettes = sorted(graphe.keys())

    #creation de la matrice
    M = [ [0] * len(etiquettes) for i in etiquettes]
    dct_idx = {etiquettes[i]:i for i in range(len(etiquettes))}

    #mise a jour de la matrice
    for noeud in graphe:
        for successeur in graphe[noeud]:
            i = dct_idx[noeud]
            j = dct_idx[successeur]
            M[i][j] = 1

    return M,etiquettes












def tests():

    def assert_equal(act,exp,msg=''):
        msg += ': '*bool(msg) + "{} should equal {}".format(act,exp)
        assert exp==act, msg

    TESTS = [           # (dict, matrice, etiquettes)
        (
         {'D': ['C'], 'B': ['C', 'D'], 'A': ['C', 'D'], 'C': ['B', 'C']},
          [[0, 0, 1, 1],
          [0, 0, 1, 1],
          [0, 1, 1, 0],
          [0, 0, 1, 0]],
          ['A', 'B', 'C', 'D'],
          ),


        (
         {'C': ['A', 'D', 'E'], 'D': [], 'A': ['A', 'F'], 'F': ['C', 'E', 'F'], 'B': ['A', 'C', 'F'], 'E': ['A', 'B', 'D', 'E', 'F']},
         [[1, 0, 0, 0, 0, 1],
          [1, 0, 1, 0, 0, 1],
          [1, 0, 0, 1, 1, 0],
          [0, 0, 0, 0, 0, 0],
          [1, 1, 0, 1, 1, 1],
          [0, 0, 1, 0, 1, 1]],
         ['A', 'B', 'C', 'D', 'E', 'F'],
        ),


         (
          {'C': ['B', 'Z'], 'D': ['B'], 'Z': ['C'], 'B': ['A', 'C', 'D'], 'A': ['B']},
          [[0, 1, 0, 0, 0],
           [1, 0, 1, 1, 0],
           [0, 1, 0, 0, 1],
           [0, 1, 0, 0, 0],
           [0, 0, 1, 0, 0]],
          ['A', 'B', 'C', 'D', 'Z'],
         ),
    ]


    for dct, exp_matrice, exp_etiquettes in TESTS:
        actual = dict_to_mat(dct)
        assert type(actual)==tuple and len(actual)==2, "output should be a tuple of size 2"
        M,etk = actual
        assert_equal(M, exp_matrice, 'matrice incorrecte')
        assert_equal(etk, exp_etiquettes, 'étiquettes incorrectes')
    print('ok')

tests()


