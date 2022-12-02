

def extract_sibbling_chars(lst):
    """ Filtrer la liste "lst" pour ne renvoyer que les chaînes qui comportent
        au moins deux caractères consécutifs identiques. Exemple:

            Si:                     lst = ['aa','','aA', '', 'n', '.JD!!ac']
            La fonction renvoie:    ['aa', '.JD!!ac']

        @lst:    liste de chaînes de caractères
        @return: v. ci-dessus...
    """
    # premières questions à vous poser:
    #   1) combien de niveaux de boucles ?
    #       2 niveau de boucles
    #   2) quels types de boucles ? (for/for+range/while)
    #       for et for range

    def verif(lst):
        for i in range(1,len(lst)):
            if lst[i]==lst[i-1]:
                return True
        return False

    result = []
    for v in lst:
        if verif(list(v)):
            result.append(v)
    return result

"""
FZ: c'est pas mal. La construction générale est bonne.
    La sous-fonction est une bonne idée, mais tu n'as pas besoin de convertir le mot en liste.
    Tu peux très bien indexer la chaîne de caractères.
    Nota: attention aux noms de variables..... "v" pour un "mot"? un "word"? une "string"? une
    "chaîne de caractères"? Et "lst" -> "mot" dans la sous-fonction
"""













def tests():
    TESTS = [
        (['abcddef', 'aabcd', '01234', 'abcdd', 'abcdefa', '0012'],    # lst
         ['abcddef', 'aabcd', 'abcdd', '0012'] ),                      # expected

        (['aaaa', 'oops?', 'ksjfhg!!'],
         ['aaaa', 'oops?', 'ksjfhg!!']),

        (['aa','','aA', '', 'n'],
         ['aa']),

        (['n', 'azeryuiop','123654789'],
         []),

        ([],
         []),
    ]
    for lst,exp in TESTS:
        actual = extract_sibbling_chars(lst[:])
        print("\n-----\ninputs: {}\nexpected: {}\nactual: {}".format(lst,exp,actual))
        assert exp==actual

    print('ok')

tests()

