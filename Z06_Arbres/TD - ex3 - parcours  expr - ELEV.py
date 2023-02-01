from collections import deque

class Queue:
    """ Une Queue est représentée avec la tête de la file à droite.
        Interface disponible:
            q = Queue()
            q.enqueue(v)
            v = q.dequeue()
            q.is_empty()

        (possibilité d'afficher le contenu de la file avec str(q), mais
         uniquement là pour un éventuel débogage)
    """
    def __init__(self,iterable=()): self._q=deque(iterable)
    def __str__(self):   return str(self._q)
    def enqueue(self,v): self._q.appendleft(v)
    def dequeue(self):   return self._q.pop()
    def is_empty(self):  return len(self._q) == 0


class Stack:
    """ Une Stack est représentée avec le "top" de la pile à droite
    Interface disponible:
            pile = Stack()
            pile.push(v)
            v = pile.pop()
            pile.is_empty()

        (possibilité d'afficher le contenu de la pile avec str(pile), mais
         uniquement là pour un éventuel débogage)
    """
    def __init__(self,iterable=()): self._pile=list(iterable)
    def __str__(self):  return str(self._pile)
    def push(self,v):   self._pile.append(v)
    def pop(self):      return self._pile.pop()
    def is_empty(self): return len(self._pile) == 0





class Node:

    #---------------------------------------------------------
    # Interdiction de toucher à la partie du code de la
    # classe située entre les deux "barres" horizontales... :p

    def __init__(self, v:str, l=None, r=None):
        self.value = v
        self.left  = l
        self.right = r

    def __len__(self):
        return 1 + sum(len(child) for child in (self.left, self.right) if child)

    def __repr__(self):
        lst = [repr(x) for x in (self.value, self.left, self.right)]
        return "Node({})".format(', '.join(lst))

    #---------------------------------------------------------

    # Ajoutez vos méthodes ci-dessous

    def prefixe(self):

        if self.value is None:
            return ""

        return str(self.value
                   + ((" " + self.left.prefixe()) if self.left is not None else "")
                   + ((" " + self.right.prefixe()) if self.right is not None else "")
                   )

        # msg = str(self.value)
        # for enfant in (self.left, self.right):
        #     if enfant is not None: msg += " " + str(enfant.prefixe())
        # return msg

    def infixe(self):

        if self.value is None:
            return ""

        return str(((self.left.prefixe() + " ") if self.left is not None else "")
                   + self.value
                   + ((" " + self.right.prefixe()) if self.right is not None else "")
                   )

    def suffixe(self):

        if self.value is None:
            return ""

        return str((self.left.prefixe() if self.left is not None else "")
                   + (self.right.prefixe() if self.right is not None else "")
                   + self.value
                   )

    #
    # def infixe(self):
    #     if self.value is None:
    #         return ""
    #
    #     msg = ""
    #     if self.left is not None: msg += str(self.left.suffixe()) + " "
    #     msg += str(self.value)
    #     if self.right is not None: msg += " " + str(self.right.suffixe())
    #     return msg
    #
    # def suffixe(self):
    #     if self.value is None:
    #         return " "
    #
    #     msg = ""
    #     for enfant in (self.left, self.right):
    #         if enfant is not None: msg += " " + str(enfant.prefixe())
    #
    #     return msg











# --------------------------------------------------------------------------
#                                  TESTS
# --------------------------------------------------------------------------


def tests_to_tree():

    def tell(what):
        print("""\
-----------------
Teste: {}
        """.format(what))

    def assert_equal(act,exp,msg=''):
        msg += ': '*bool(msg) + "{} should equal {}".format(repr(act),repr(exp))
        assert exp==act, msg

    def assert_tree(act,exp):
        lA, lE = len(act), len(exp)
        assert_equal(lA,lE, "les deux arbres devraient contenir le même nombre de noeuds")
        exp==act        # lève une erreur si faux, voir Node.__eq__


    TESTS=[

('0', 0, Node('0')),

('-42', -42, Node('-42')),

('* + 2 3 5', 25,
    Node('*',
         Node('+',
              Node('2'),
              Node('3')),
         Node('5')) ),


('* 5 + 2 3', 25,
    Node('*',
         Node('5'),
         Node('+',
              Node('2'),
              Node('3'))) ),


('- / 1 2 / * 3 1 2', -1,
    Node('-',
         Node('/',
              Node('1'),
              Node('2')),
         Node('/',
              Node('*',
                   Node('3'),
                   Node('1')),
              Node('2'))) ),


('/ 25 -2.5', -10,
    Node('/', Node('25'),
              Node('-2.5') ) ),


('/ 7 - + 2 5 -2', 0.7777777777777778,
    Node('/', Node('7'),
              Node('-', Node('+', Node('2'),
                                  Node('5') ),
                        Node('-2') ) ) )
]



    TREE_TO_STR = {
        "prefixe": [ '0',
                    '-42',
                    '* + 2 3 5',
                    '* 5 + 2 3',
                    '- / 1 2 / * 3 1 2',
                    '/ 25 -2.5', '/ 7 - + 2 5 -2'],

        "suffixe": ['0',
                    '-42',
                    '2 3 + 5 *',
                    '5 2 3 + *',
                    '1 2 / 3 1 * 2 / -',
                    '25 -2.5 /', '7 2 5 + -2 - /'],

        "infixe": [  '0',
                    '-42',
                    '( ( 2 + 3 ) * 5 )',
                    '( 5 * ( 2 + 3 ) )',
                    '( ( 1 / 2 ) - ( ( 3 * 1 ) / 2 ) )',
                    '( 25 / -2.5 )', '( 7 / ( ( 2 + 5 ) - -2 ) )'],
    }



    for method_name in 'prefixe suffixe infixe'.split():

        if not hasattr(Node, method_name):
            raise Exception(method_name+" n'est pas encore implantée")

        expecteds = TREE_TO_STR[method_name]

        tell(method_name)
        for (_s,_n,tree),exp in zip(TESTS, expecteds):
            print("\n\nTest sur l'arbre ci-dessous")
            print(tree)
            act = getattr(tree, method_name)()
            assert_equal(act, exp)
        print(method_name+' ok')

    print('\n"Tree to str" -> ok')


    for s,exp,tree in TESTS:
        tell("evalue {}: devrait renvoyer {}".format(repr(s),exp))
        act = tree.evalue()
        assert_equal(act,exp)
    else:
        print('ok')

    print("\n*****\nDone!\n*****")

tests_to_tree()


