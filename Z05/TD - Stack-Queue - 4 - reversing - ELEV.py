"""
Implantations des piles et files utilisées dans votre code:

    Nota: les deux structures peuvent être affichées dans la console
          en utilisant la fonction print.
"""

class Pile:
    """ Une Pile est représentée avec le "top" de la pile à droite """

    def __init__(self, iterable=()):  self._pile=list(iterable)

    def __repr__(self):   return "Pile({})".format(self._pile)

    def empile(self,v):  self._pile.append(v)

    def depile(self):    return self._pile.pop()

    def est_vide(self):  return len(self._pile) == 0



from collections import deque

class File:
    """ Une File est représentée avec la tête de la file à droite """

    def __init__(self, iterable=()):  self._q=deque(iterable)

    def __repr__(self):    return "File({})".format(list(self._q))

    def enfile(self,v):   self._q.appendleft(v)

    def defile(self):     return self._q.pop()

    def est_vide(self):   return len(self._q) == 0



#-----------------------------------------------



def reversing(pile: Pile, file: File) -> None:
    """ Mute la file et la pile de manière à ce qu'à la fin, le contenu de la
        file soit inversé alors que celui de la pile est le même qu'au départ.

        Contraintes: toute structure de données autre que la pile et la file
        est interdite. Vous n'avez le droit qu'à 2 autres variables en plus,
        stockant des entiers (une suffit, normalement).
    """
    n = 0
    
    while not file.est_vide():
        pile.empile(file.defile())
        n += 1
    
    while n > 0:
        file.enfile(pile.depile())
        n -= 1















def tests():
    TESTS = [
        ([0,1,2,3],[4,5]),
        ([0,1,2,3],[]),
        ([],[4,5]),
        ([5,4,3,2],[4,5,4,6,8,5]),
    ]

    for q,stk in TESTS:

        a,b = q[::-1],stk[:]
        stk = Pile(stk)
        q = File(q)

        print("------\nContenus avant l'appel:")
        print(stk)
        print(q)

        reversing(stk,q)

        print("\nAprès l'appel")
        print(stk)
        print(q)

        assert list(q._q) == a, "La file devrait avoir été inversée et contenir: "+str(a)
        assert stk._pile == b,  "La pile devrait toujours contenir: "+str(b)
    else:
        print('ok')


tests()


