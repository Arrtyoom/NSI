


def extract_by_length(lst, n):
    """ Filtrer la liste "lst" pour ne renvoyer que les chaînes de caractères
        de longueur "n".

        @lst:    liste de chaînes de caractères
        @n:      longueur des chaînes à extraire (n>=0)
        @return: une nouvelle liste ne contenant que les chaînes de longueur
                 voulue, en respectant l'ordre initial
    """

    """
    result = []

    for v in lst:

        if len(v) == n:
            result.append(v)

    return result
    """

    # Redéclarer la fonction ici et le faire maintenant en utilisant une
    # "list comprehension" (= "en une seule ligne").
    #
    # Dans une liste compréhension, les conditions sont écrites tout à la fin.
    # Exemple:
    #
    #   arr = []
    #   for value in list_of_numbers:
    #       if check(value):        # nota: check(value) renvoie un booléen
    #           arr.append(value*2)
    #   return arr
    #
    # Devient, en list compréhension:
    #
    #   return [ value*2 for value in list_of_number if check(value) ]
    #

    return [v for v in lst if len(v)==n]




def tests():
    TESTS = [
        ( ['un','deux','trois','quatre','cinq','six','sept','huit','neuf','dix'],
          ( (3, ['six','dix']),
            (4, ['deux','cinq','sept','huit','neuf']),
            (5, ['trois']))
        ),

        (['','','kjhg',''],
         ( (3,[]),
           (0,['','','']),
           (4, ['kjhg']))
        ),

        ([],
         ((110, []),)
        )
    ]
    for lst,batches in TESTS:
        for size,exp in batches:
            actual = extract_by_length(lst[:],size)
            print("\n-----\ninputs: {}, {}\nexpected: {}\nactual: {}".format(lst,size,exp,actual))
            assert exp==actual
    print('ok')
tests()


