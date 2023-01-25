
def insere(arr: [int], v: int) -> None:
    """ Insère la valeur @v dans le tas minima @arr.

        @arr: list d'entiers. Il est garanti que l'état initial correspond à
              un tas minimal valide.
        @v:   Valeur à insérer dans le tas minimal

        @return: rien. Mais garantit qu'arr est toujours un tas minimal à
                 la fin de la procédure.
    """
    # Fonction insère(arr,v):
    #     Ajouter le nouvel élément tout à la fin de arr
    #     i = position du noeud en cours
    #     Répéter:
    #         j = index du noeud parent du noeud en cours
    #         Si i==0 ou arr[j]<=arr[i]
    #             Arrêter la boucle
    #         Fin Si
    #         Echanger le parent et l'enfant
    #         Mettre à jour i
    #     Fin Répéter
    # Fin Fonction

    print(arr, v)
    arr.append(v)
    i = len(arr) - 1
    while True:
        j = (i - 1) // 2
        print(arr, v, i, j)
        if i == 0 or arr[j] <= arr[i]:
            print("finish")
            break
        arr[j], arr[i] = arr[i], arr[j]
        i = j












def tests():

    def assert_equal(act,exp,msg=''):
        msg += ': '*bool(msg) + "{} should equal {}".format(act,exp)
        assert exp==act, msg


    TESTS = [

        ([], -93, [-93]),
        ([25], 15, [15, 25]),
        ([31], -37, [-37, 31]),

        ([-21, -5], 56, [-21, -5, 56]),
        ([5, 21], -29, [-29, 21, 5]),

        ([-46, -21, -44, -8, 35, 8, -5, 33], -25,
            [-46, -25, -44, -21, 35, 8, -5, 33, -8]),

        ([-37, -19, -11, 67, -7, 52, 83], 23,
            [-37, -19, -11, 23, -7, 52, 83, 67]),

        ([-46, -45, 66, 63, 98, 78, 72], -2,
            [-46, -45, 66, -2, 98, 78, 72, 63]),

        ([-50, -47, -42, -2, 12, 35, -35, 95, -1, 47], -94,    # to root
            [-94, -50, -42, -2, -47, 35, -35, 95, -1, 47, 12]),


        ([-47, 2, -41, 10, 15, -18, -26, 54, 40, 28], 10,
            [-47, 2, -41, 10, 10, -18, -26, 54, 40, 28, 15]),

        ([-37, -14, -6, 24, -9, 5, 1, 43, 95, 73], 69,         # no move
            [-37, -14, -6, 24, -9, 5, 1, 43, 95, 73, 69]),

        ([-38, -31, -28, -26, -28, -17, 9, -14, -14, -8, 40, -10, 9, 27, 36, 62, 97, 70, 25, 33, 74, 97, 47, -5, 24, 54, 49, 95, 99, 50, 82], -26,
            [-38, -31, -28, -26, -28, -17, 9, -26, -14, -8, 40, -10, 9, 27, 36, -14, 97, 70, 25, 33, 74, 97, 47, -5, 24, 54, 49, 95, 99, 50, 82, 62]),

        ([-48, -38, -47, -20, -28, -14, 4, 56, 24, 32, 11, 72, -12, 22, 18, 77, 83, 74, 43, 66, 80, 50, 26, 93, 95, 97, 41, 35, 53, 35, 47, 84], 39,
            [-48, -38, -47, -20, -28, -14, 4, 39, 24, 32, 11, 72, -12, 22, 18, 56, 83, 74, 43, 66, 80, 50, 26, 93, 95, 97, 41, 35, 53, 35, 47, 84, 77]),
    ]
    for a,v,exp in TESTS:
        msg = "Inserting {} in {}".format(v, a)
        insere(a,v)
        assert_equal(a,exp, msg)
    else:
        print('ok')


tests()

