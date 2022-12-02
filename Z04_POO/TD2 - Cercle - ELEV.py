from typing import List

from math import pi

class Cercle:
    def __init__(self,x,y,rayon:int) -> None:
        self.rayon = rayon
        self.x = x
        self.y = y
    
    def __repr__(self) -> str:
        return f"Cercle({self.rayon},{self.x},{self.y})"

    def perimetre(self):
        return 2*pi*self.rayon

    def aire(self):
        return pi*self.rayon**2

    def intersect(self,other:'Cercle') -> bool:

        #(x2-x1)**2 + (y2-y1)**2 est plus grand que (r1 + r2)**2,
        #les cercles ne se coupent pas 

        base_sq = ((other.x - self.x)**2 + (other.y - self.y)**2)
        rayon = (self.rayon + other.rayon)**2
        return base_sq <= rayon
        
    def filtrer(self,lst_cercles):
        cercles_filtrer = []
        for cercle in lst_cercles:
            if self.intersect(cercle):
                cercles_filtrer.append(cercle)
        return cercles_filtrer








cercle = Cercle(10,15,4.3)
lst_cercle = [Cercle(2,15,20),Cercle(2,20,25),Cercle(5,10,15)]
print(lst_cercle)
print(cercle.filtrer(lst_cercle))













#----------------------------------------------




def Test(title):
    def decorator(func):
        print('\n'+title)
        func()
        print('ok')
    return decorator




@Test("La classe Cercle est-elle définie?")
def _():
    assert 'Cercle' in globals(), "la classe Cercle n'est pas définie"
    assert isinstance(Cercle, type), "Cercle devrait être une classe..."



@Test("Peut-on créer des instances de la classe Cercle avec les bonnes infos?")
def _():
    c = Cercle(1,2,3)



@Test("Les attributs sont-ils définis et ont-ils les bonnes valeurs?")
def _():
    c = Cercle(1,2,3)

    attrs = 'x y rayon'.split()
    missings = ', '.join( attr for attr in attrs if not hasattr(c,attr) )
    assert not missings, "Les attributs suivants ne sont pas définis: "+missings

    for i in range(3):
        attr = attrs[i]
        val = getattr(c, attr)
        assert val == i+1, f"c.{attr}: {val} devrait être {i+1}"



print('''
-----------------------------------------------
Pour un cercle centré en (15,23) et de rayon 5:
''')

for meth in 'perimetre aire'.split():

    c    = Cercle(15,23,5)
    exps = {
        'perimetre': 31.41592653589793,
        'aire':      78.53981633974483,
    }

    func = getattr(c,meth, None)

    @Test(f'La méthode {meth} est-elle définie?')
    def _():
        assert func is not None, f"La méthode {meth} n'est pas définie"
        assert callable(func), f"{meth} est sensée être une méthode, pas une propriété..."

    @Test(f'La méthode {meth} fait-elle le bon calcul?')
    def _():
        val = func()
        exp = exps[meth]
        assert abs(val-exp)<1e-9, f"{meth}: {val} devrait être {exp}"




@Test("Random (Non, on ne hardcode pas les valeurs...)")
def _():
    from random import random, randrange as rand
    for _ in range(5):
        xs=[random()*rand(5,10) for _ in range(3)]
        c = Cercle(*xs)
        assert c.x == xs[0], "wrong c.x"
        assert c.y == xs[1], "wrong c.y"
        assert c.rayon == xs[2], "wrong c.rayon"
        assert c.perimetre() == xs[2]*2*pi, "wrong c.perimetre()"
        assert c.aire() == xs[2]**2*pi, "wrong c.aire()"



@Test("Question 3: définir sous votre classe une instance de Cercle assignée à la variable cercle")
def _():
    assert 'cercle' in globals(), "La variable cercle n'est pas définie"
    assert (cercle.x, cercle.y, cercle.rayon) == (10,15,4.3), "cercle n'est pas les bonnes valeurs d'attributs"


@Test("Q4: la méthode __repr__ est-elle définie?")
def _():
    assert '__repr__' in Cercle.__dict__, "la méthode __repr__ n'est pas définie"
    assert callable(Cercle.__repr__), "Cercle.__repr__ est sensée être une METHODE..."






@Test("la méthode __repr__ doit renvoyer une chaîne de caractères")
def _():
    val = cercle.__repr__()
    assert isinstance(val, str), f"{val!r} n'est pas une chaîne de caractères"


@Test("la méthode __repr__ devrait montrer toutes les infos concernant le cercle (coordonnées et rayon)")
def _():
    data = [
        ('x', 10),
        ('y', 15),
        ('rayon', 4.3),
    ]
    rep = cercle.__repr__()
    for attr,v in data:
        assert str(v) in rep, "la chaîne renvoyée par __repr__ ne contient pas la valeur de l'attribut {attr}"



@Test('BONUS: le résultat de __repr__ est-il évaluable...?')
def _():
    try:
        c = eval( cercle.__repr__() )
        print('OUI')
        if not isinstance(c,Cercle):
            print("... sauf que ce n'est pas une instance de Cercle")
    except:
        print('NON')






@Test("Q8: instersect")
def _():
    assert hasattr(Cercle, "intersect"), "la méthode intersect n'est pas définie"
    assert callable(Cercle.intersect), "Cercle.__repr__ est sensée être une METHODE..."

    from inspect import signature
    ps = signature(Cercle.intersect).parameters
    assert len(ps)==2, "nombre d'arguments incorrect pour la méthdoe intersect..."

    data = [
        (0,0,5,     1,7,3,      True),
        (0,0,2,     1,7,3,      False),
        (0,0,2.5,   3,4,2.55,   True),
        (9,9,2.4,   6,5,2.55,   False),
    ]
    for x1,y1,r1, x2,y2,r2, exp in data:
        c1 = Cercle(x1,y1,r1)
        c2 = Cercle(x2,y2,r2)
        assert getattr(Cercle,'intersect')(c1,c2) == exp,(
            f"Il y a pourtant intersection entre {c1} et {c2}"
                if exp else
            f"Il y n'a pourtant pas intersection entre {c1} et {c2}"
        )






@Test("Q9: trouver les cercles intersectant l'instance cercle")
def _():
    lst = [
        Cercle(5, 1, 1),   Cercle(10, 8, 4), Cercle(4, 4, 5),  Cercle(13, 1, 7),
        Cercle(11, 2, 15), Cercle(6, 16, 1), Cercle(1, 11, 9), Cercle(8, 0, 2),
        Cercle(12, 8, 0),  Cercle(2, 2, 12), Cercle(10, 0, 1), Cercle(13, 0, 1),
        Cercle(2, 4, 5),   Cercle(6, 7, 9),  Cercle(11, 9, 0)
    ]
    start_len = len(lst)

    # compléter la ligne suivante (et uniquement celle-ci!)
    cuts_cercle = cercle.filtrer(lst)

    exp = [
        Cercle(10, 8, 4),
        Cercle(11, 2, 15),
        Cercle(6, 16, 1),
        Cercle(1, 11, 9),
        Cercle(2, 2, 12),
        Cercle(6, 7, 9)
    ]
    assert str(cuts_cercle)==str(exp), f'{cuts_cercle} devrait être {exp}'
    assert len(lst) == start_len, "NON, on ne mute pas la liste passée en argument..."



