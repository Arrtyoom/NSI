"""
Implantations des piles et files utilisées dans votre code:

    Nota: les deux structures peuvent être affichées dans la console
          en utilisant la fonction print.
"""


class Pile:
    """ Une Pile est représentée avec le "top" de la pile à droite """

    def __init__(self, iterable=()):  self._pile = list(iterable)

    def __repr__(self):  return "Pile({})".format(self._pile)

    def empile(self, v):  self._pile.append(v)

    def depile(self):    return self._pile.pop()

    def est_vide(self):  return len(self._pile) == 0


from collections import deque


class File:
    """ Une File est représentée avec la tête de la file à droite """

    def __init__(self, iterable=()):  self._q = deque(iterable)

    def __repr__(self):   return "File({})".format(list(self._q))

    def enfile(self, v):   self._q.appendleft(v)

    def defile(self):     return self._q.pop()

    def est_vide(self):   return len(self._q) == 0


print("""
VERSION 1:
----------
""")


def calcRPN(s: str) -> int:
    """ évalue une expression écrite en notation polonaise inverse
        (opérateurs: + ou *)
    """
    pile = Pile()
    lst = s.split(' ')

    for char in lst:
        if char in '*+':
            a = pile.depile() if not pile.est_vide() else None
            b = pile.depile() if not pile.est_vide() else None

            if a is None or b is None: return None

            if char == '*': pile.empile(a * b)
            if char == '+': pile.empile(a + b)

        else: pile.empile(int(char))
    return pile.depile()


def tests():
    TESTS = [
        ("1 2 3 * + 4 *", 28),
        ("4 11 2 3 * + *", 68),
        ("3 6 + 2 4 * *", 72),
        ("42", 42),
    ]

    for s, exp in TESTS:
        act = calcRPN(s)
        assert exp == act, "{}: {} should be {}".format(s, act, exp)
    print('ok')


tests()

print("""
VERSION 2:
----------
""")


def calcRPN(s: str) -> float:
    """ évalue une expression écrite en notation polonaise inverse
        (opérateurs: +, *, - ou / (true division) ; les nombres en entrée
        sont des entiers quelconques)
    """
    pile = Pile()
    lst = s.split(' ')

    for char in lst:
        if char in '*+-/':
            b = pile.depile() if not pile.est_vide() else None
            a = pile.depile() if not pile.est_vide() else None

            if a is None or b is None: return None

            if char == '*': pile.empile(a * b)
            if char == '+': pile.empile(a + b)
            if char == '-': pile.empile(a - b)
            if char == '/': pile.empile(a / b)

        else: pile.empile(int(char))
    return pile.depile()


def tests():
    TESTS = [
        ("1 2 3 * + 4 *", 28),
        ("11 2 3 * + 4 *", 68),
        ("3 6 + 2 4 * *", 72),
        ("4 9 -", -5),
        ("5 4 /", 1.25),
        ("11 2 -3 * + 4 * 1 -", 19),
        ("133 1 2 3 * + / 4 *", 76),
        ("42", 42),
    ]

    for s, exp in TESTS:
        act = calcRPN(s)
        assert exp == act, "{}: {} should be {}".format(s, act, exp)
    print('ok')


tests()
