# Créé par Elève, le 09/10/2022 en Python 3.7
"""
L'exercice ci-dessous contient deux parties. Dans les deux cas, il s'agit de
convertir une matrice d'adjacence en un dictionnaire de successeurs, la différence
reposant sur la façon de représenter les sommets dans le dictionnaire.
Le choix dépend du second argument, @etiquettes:
    - Cas 1: @etiquettes est une liste de chaînes de caractères, donnant les
             étiquettes de chaque noeud, dans le même ordre que pour la matrice,
             et le dictionnaire de successeurs doit alors contenir les étiquettes
             des noeuds plutôt que leur indice.
    - Cas 2: @etiquettes vaut None.
             Dans ce cas, les sommets sont représentés par leurs indices dans la
             matrice d'adjacence.


A faire:
    1) Lire le docstring et les exemples, bien comprendre le contexte et les
       données en jeu.

    2) Des commentaires sont rédigés dans la fonction, qui sont du pseudo-code
       décrivant la logique à utiliser pour implanter la fonction lorsqu'elle
       reçoit la liste d'étiquettes en argument.
       Implanter la fonction en suivant le pseudo-code fourni.

    3) Modifier le moins possible votre fonction de manière à gérer en plus le cas
       où les étiquettes ne sont pas fournies en argument.
"""



def mat_to_dict(matrice, etiquettes=None):
    """ Convertit une matrice d'adjacence représentant un graphe non pondéré
        en dictionnaire de listes de successeurs.

        @matrice:    une liste de listes d'entiers de dimensions NxN
        @etiquettes: liste ordonnée des étiquettes correspondant à chaque sommet.
                     (raffinement: Si etiquette vaut None, utiliser l'index du
                                   sommmet comme étiquette).
        @return:     dictionnaire de listes donnant les voisins d'un noeud.
                     (raffinement: trier les listes avant de renvoyer le dictionnaire ;
                                   avant de vous lancer dedans, réfléchissez à ce que
                                   vous avez déjà fait...)

        exemple:
            Arguments:
                matrice:                etiquetttes:
                [[0, 1, 0],             ['A', 'B', 'C']
                 [0, 0, 1],
                 [0, 1, 1]],

            Sortie:
                avec étiquettes:            sans étiquettes:
                 {'A': ['B'],               {0: [1],
                  'B': ['C'],                1: [2],
                  'C': ['B','C']}            2: [1,2]}
    """
    # Pseudo-code pour la partie "sans" etiquettes:

    # Définir la structure de données "de base" à retourner, vide
    # Ajouter tous les noeuds avec leur liste de successeurs "de base" (vide)
    #
    # Pour chaque ligne de la matrice:
    #     Pour chaque élément de la ligne:
    #         Si un successeur existe:
    #             Définir les deux labels à utiliser (noeud en cours et successeur)
    #             Mettre à jour le dictionnaire
    #         Fin Si
    #     Fin Pour
    # Fin Pour
    # Renvoyer le résultat

    if etiquettes == None:
        #etiquettes = [i for i in range(len(matrice))]
        etiquettes = list(range(len(matrice)))


    dct = {}
    for i in etiquettes:
        dct[i] = []

    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if matrice[i][j] == 1:
                noeud = etiquettes[i]
                successeurs = etiquettes[j]
                dct[noeud].append(successeurs)

    return dct













def tests():
    def assert_equal(act,exp,msg=''):
        msg += ': '*bool(msg) + "{} should equal {}".format(act,exp)
        assert exp==act, msg

    TESTS = [
        ([[0, 0, 1, 1],
          [0, 0, 1, 1],
          [0, 1, 1, 0],
          [0, 0, 1, 0]], ['A', 'B', 'C', 'D'],
          {'D': ['C'], 'B': ['C', 'D'], 'A': ['C', 'D'], 'C': ['B', 'C']},
          {0: [2, 3], 1: [2, 3], 2: [1, 2], 3: [2]}),

        ([[1, 0, 0, 0, 0, 1],
          [1, 0, 1, 0, 0, 1],
          [1, 0, 0, 1, 1, 0],
          [0, 0, 0, 0, 0, 0],
          [1, 1, 0, 1, 1, 1],
          [0, 0, 1, 0, 1, 1]],
         ['A', 'B', 'C', 'D', 'E', 'F'],
         {'C': ['A', 'D', 'E'], 'D': [], 'A': ['A', 'F'], 'F': ['C', 'E', 'F'], 'B': ['A', 'C', 'F'], 'E': ['A', 'B', 'D', 'E', 'F']},
         {0: [0, 5], 1: [0, 2, 5], 2: [0, 3, 4], 3: [], 4: [0, 1, 3, 4, 5], 5: [2, 4, 5]}),

         ([[0, 1, 0, 0, 0],
           [1, 0, 1, 1, 0],
           [0, 1, 0, 0, 1],
           [0, 1, 0, 0, 0],
           [0, 0, 1, 0, 0]],
          ['A', 'B', 'C', 'D', 'E'],
         {'C': ['B', 'E'], 'D': ['B'], 'E': ['C'], 'B': ['A', 'C', 'D'], 'A': ['B']},
         {0: [1], 1: [0, 2, 3], 2: [1, 4], 3: [1], 4: [2]}),
    ]


    for matrice,etiquettes,exp,_ in TESTS:
        act = mat_to_dict(matrice,etiquettes)

        # vérifie que les deux dictionnaires ont bien les mêmes clefs
        kA,kE = sorted(act), sorted(exp)
        assert_equal(kA, kE, "Les clefs des deux dictionnaires devraient être identiques")

        # cherche les listes de successeurs fausses:
        bad = [ '{}: {}!={}'.format(k,act[k],exp[k]) for k in etiquettes if sorted(act[k])!=sorted(exp[k]) ]
        assert_equal(bad, [], "listes de ces successeurs erronées")

    print('ok')





    for matrice,etiquettes,_,exp in TESTS:
        str_mat = "\n".join(', '.join(map(str,row)) for row in matrice)
        act = mat_to_dict(matrice)
        msg = "{}\nGestion sans étiquettes incorrecte:\n{}  should be\n{}".format(
                    str_mat, act, exp
                )
        assert_equal(act, exp, msg)
    print('ok sans étiquettes')


tests()


