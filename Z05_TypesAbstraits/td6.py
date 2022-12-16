# CLASS

class Stack:
    """ Une Stack est représentée avec le "top" de la pile à droite """

    def __init__(self, iterable=()):  self._pile=list(iterable)

    def __repr__(self):  return str(self._pile)

    def push(self,v):    self._pile.append(v)

    def pop(self):       return self._pile.pop()

    def is_empty(self):  return len(self._pile) == 0

# FUNCTION

def calcRPN(s:str) :
    """ Calculatrice Polonaise 
    
    maniere d'ecrire differament exemple : 
    2 * 3 => 2 3 *

    on met l'operateur a la fin (operateur acceptable + et *)

    @s : operation mathematique ecrite en ecriture polonaise
    @return : resultat de cette operation mathematique
    """
    pile = Stack()
    lst = s.split(' ')

    for char in lst :
        if char in '*+' : 

            # definition of a and b
            a = pile.pop() if not pile.is_empty() else None
            b = pile.pop() if not pile.is_empty() else None

            if a == None or b == None : return None

            if char == '*' : pile.push(a*b)
            if char == '+' : pile.push(a+b)

        else : pile.push( int(char) )

    return pile.pop()


def calcRPN(s:str) :
    """ Calculatrice Polonaise (TEST)
    
    maniere d'ecrire differament exemple : 
    2 * 3 => 2 3 *

    on met l'operateur a la fin (operateur acceptable +, *, - et /)

    @s : operation mathematique ecrite en ecriture polonaise
    @return : resultat de cette operation mathematique
    """
    pile = Stack()
    lst = s.split(' ')

    for char in lst :
        # if operand
        if char in '*+-/' : 

            # attribution of a and b
            a = pile.pop() if not pile.is_empty() else None
            b = pile.pop() if not pile.is_empty() else None

            # if not enough value return None
            if a == None or b == None : return None

            # make the math operation
            if char == '*' : pile.push(a*b)
            if char == '+' : pile.push(a+b)
            if char == '-' : pile.push(a-b)
            if char == '/' : pile.push(a/b)

        # if numerical value
        else : pile.push( int(char) )

    # check if the there's only the value we want left in the stack
    last = pile.pop()
    return last if pile.is_empty() else None

# PROGRAMME


















# TESTS

def tests(func):
    TESTS = [
        (6,     '2 3 *'), # exp, s
        (5,     '2 3 +'),
        (None,  '3 *'),
        (None,  '2 2 3 *'),
        (68,    '4 11 2 3 * + *'),
        (-6,    '2 -3 *'),
        (-19,   '11 2 -3 * + 4 * 1 -'),
    ]

    for exp, s in TESTS : 
        act = func(s)
        assert act==exp,"{}: {} should be {}".format(s,act,exp)
    else : print('ok : calc polonaise')
    

tests(calcRPN)