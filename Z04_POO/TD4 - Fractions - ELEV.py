"""
Une fois votre classe implantée, ajouter la méthode __repr__, qui renvoie une
chaîné de caractères représentant l'instance, sous la forme:
        Fraction(numérateur, dénominateur)

    ex:  4/13   ->   "Fraction(4, 13)"
"""

class Fraction:
    def __init__(self,x,y=1) -> None:
        if x > 0 and y > 0 or x < 0 and y < 0:        
            self.num   =   abs(x)
            self.denom =   abs(y)
        else:
            self.num   = - abs(x)
            self.denom =   abs(y)

    def __repr__(self) -> str:
        return f"Fraction({self.num},{self.denom})"


    def add(self:"Fraction",other:"Fraction") -> "Fraction":
        """additionne Fraction self 
        et Fraction other"""
        a = self.num
        b = self.denom
        c = other.num
        d = other.denom
        print(a,b,c,d)
        
        resultat = Fraction(a*d + c*b, b*d)
        print(resultat)
        print(pgdc(resultat.num, resultat.denom))
        return pgdc(resultat.num, resultat.denom)


    def sub(self:"Fraction",other:"Fraction") -> "Fraction":
        """soustrait Fraction self 
        et Fraction other"""
        a = self.num
        b = self.denom
        c = other.num
        d = other.denom
        
        resultat = Fraction(a*d - c*b, b*d)
        return pgdc(resultat.num, resultat.denom)

    def mul(self:"Fraction",other:"Fraction") -> "Fraction":
        """multiplie Fraction self 
        et Fraction other"""
        a = self.num
        b = self.denom
        c = other.num
        d = other.denom
        
        resultat = Fraction(a*c, b*d)
        return pgdc(resultat.num, resultat.denom)

    def div(self:"Fraction",other:"Fraction") -> "Fraction":
        """divise Fraction self et 
        Fraction other"""
        a = self.num
        b = self.denom
        c = other.num
        d = other.denom
        
        resultat = Fraction(a*d, b*c)
        return pgdc(resultat.num, resultat.denom)

# Gabriel 
def pgdc(a,b):
    if b == 0: 
        return abs(a) 
    elif b != 0:
        return pgdc(abs(b),abs(a%b))

# ITERATIVE
# def pgdc(a:int,b:int) -> Fraction:

#     """trouve les diviseur comment dans 
#     le but de simplifier une fraction
    
#     a est le numerateur 
#     b est le denominateur 
#     """

#     def diviseur(a:int) -> list:
#         """trouver tout les diviseur
#         de a et les mettrent dans une
#         list"""
#         lst = []
#         for i in range(a,0,-1):
#             if a%i == 0:
#                 lst.append(i)
#         return lst
    
#     def comparer(a:list,b:list) -> int:
#         """renvoyer le diviseur comment le plus haut """

#         """defini la list la plus courte entre a et b"""
#         if len(a)<len(b):
#             petit,grand = a,b
#         else:
#             petit,grand = b,a

#         """passer a travers tout les diviseurs jusqu'a
#         en trouver 1 de commun avec l'autre liste et 
#         va le renvoyer """
#         for diviseur in petit:
#             if diviseur in grand:
#                 return diviseur

#     negatif = False
#     """a ou b sont negatif donc on retient un - """
#     if a < 0 or b < 0:
#         negatif = True
#     """si a et b sont negatif alors la fraction est positive"""
#     if a < 0 and b < 0:
#         negatif = False

#     div_a = diviseur(abs(a))
#     div_b = diviseur(abs(b))
#     print("les diviseurs de {} sont {}".format(a,div_a))
#     print("les diviseurs de {} sont {}".format(b,div_b))

#     diviseur_commun = comparer(div_a,div_b)
#     print("le diviseur commun de a est b est {}".format(diviseur_commun))

#     """simplifier a et b par le diviseur commun"""
#     a_simp = a//diviseur_commun
#     b_simp = b//diviseur_commun
#     print("{}/{} ont été simplifier en {}/{}".format(a,b,a_simp,b_simp))
    
#     """la fraction est negative ou pas"""
#     if negatif:
#         return Fraction(-a_simp,b_simp)
#     else:
#         return Fraction(a_simp,b_simp)

# RECURSIVE
# def pgdc(a:int,b:int):
#     a = abs(a)
#     b = abs(b)
#     # print(f"{a=},{b=}")
#     if b == 0:
#         return a
#     else:
#         return pgdc(b,a%b)


# --------------------
fraction = Fraction(13)
# print(fraction)
# --------------------
f1 = Fraction(1,4)
f2 = Fraction(15,7)
f3 = Fraction(5,3)
f4 = Fraction(4)

# print(f1.add(f2))
# print(Fraction(f1.add(f2)))
# result = f1.add(f2)
# if isinstance(result,int):
#     result = Fraction(result)
# print(result)
# result = result.mul(f3)
# print(result)
# result = (f1.add(f2)).mul(f3).sub(f4)
# print(result)
# --------------------
# print(Fraction(5,4).add(Fraction(3,2)))
# --------------------
fraction_test = Fraction(16,4)
pgdc(fraction_test.num,fraction_test.denom)
# --------------------








#------------------------------------------------------------



def Test(func):
    print('\n\n'+func.__name__)
    func()
    print(func.__name__ + ': ok')



def assert_frac(act:Fraction, n:int, d:int, msg=""):
    """ n: expected numerator
        d: epxected denominator
    """
    assert isinstance(act, Fraction), "le résultat n'est pas une instance de Fraction: "+str(act)
    assert hasattr(act, 'num'), "le résultat n'a pas l'attribut \"num\""
    assert hasattr(act, 'denom'), "le résultat n'a pas l'attribut \"denom\""

    s = "Fraction({}, {}) devrait correspondre à {}/{}".format(act.num,act.denom,n,d)
    msg = msg+': '+s if msg else s
    assert act.num==n and act.denom==d, msg


def assert_no_error(func, msg="", excep=Exception):
    try:
        return func()
    except excep:
        msg = msg or "Aucune exception ne devrait être levée, mais a levé"

        assert False, msg + ': '+str(excep)


def assert_defined(name):
    assert name in globals(), "{} n'est pas définie...".format(name)


def assert_class(cls_name:str):
    assert_defined(cls_name)

    cls = globals()[cls_name]
    assert isinstance(cls, type), "{} n'est pas une classe...".format(cls_name)



def assert_method(cls, meth_name, inherit=False):
    if inherit:
        check = hasattr(cls, meth_name)
    else:
        check = meth_name in cls.__dict__

    assert check, "La méthode {} n'est pas définie sur la classe {}".format(
        meth_name, cls.__name__
    )

    assert callable(
        getattr(cls,meth_name)
    ), "{} est sensée être une méthode...".format(meth_name)



#------------------------------------------------------------



@Test
def q1_test_constructeur():

    assert_class('Fraction')

    assert_no_error(
        lambda: Fraction(4,5),
        "Impossible de créer une instance Fraction (4,5)"
    )

    TESTS=[
        (1,2, 1,2, ""),
        (-3,2, -3,2, ""),
        (3,-2, -3,2, "Gère les signes correctement"),
        (-17,-12, 17,12, "Gère les signes correctement"),
    ]
    for n,d,a,b,s in TESTS:
        assert_frac( Fraction(n,d), a, b, s )





@Test
def q2_test_repr():
    assert_method(Fraction, '__repr__')

    from random import sample

    n,d = sample([1,2,3,5,7,11,13,17,19], 2)
    f   = Fraction(n,d)
    rep = repr(f)

    checks = [
        ('Fraction', 'le nom de la classe devrait être présent dans sa représentation'),
        (str(n), 'le numérateur devrait apparaître dans la représentation'),
        (str(d), 'le dénominateur devrait apparaître dans la représentation'),
    ]

    for chunk,msg in checks:
        assert chunk in rep, msg




@Test
def q3_test_constructeur_avec_valeur_par_defaut():
    msg = "Le constructeur de Fraction devrait marcher avec un seul argument aussi"
    func = lambda: Fraction(42)
    act = assert_no_error(func, msg, TypeError)
    assert_frac(act, 42, 1)






@Test
def q5_test_maths():
    TESTS_MATHS=[
        ('add', [
            (1,2, 2,1, 5,2),
            (4,7, 3,5, 41,35),
            (1,2, -2,1, -3,2),
        ]),

        ('sub', [
            (1,2, 2,1, -3,2),
            (4,7, 3,5, -1,35),
            (1,2, -2,1, 5,2),
        ]),

        ('mul', [
            (1,2, 3,1, 3,2),
            (4,7, 3,-5, -12,35),
            (1,2, -3,1, -3,2),
        ]),

        ('div', [
            (1,2, 2,1, 1,4),
            (4,7, 3,-5, -20,21),
            (1,2, -2,1, -1,4),
        ]),
    ]
    for name,tests in TESTS_MATHS:
        assert hasattr(Fraction, name), "Méthode {} non définie".format(name)
        func = getattr(Fraction,name)
        for a,b, c,d, e,f in tests:
            f1 = Fraction(a,b)
            f2 = Fraction(c,d)
            ret = func(f1,f2)
            s = "({}/{}).{}({}/{})".format(a,b,name,c,d)
            assert_frac(ret, e,f, s)




@Test
def q6_test_result():
    assert_defined('result')
    assert_frac(result, -1, 84)






@Test
def q8_test_pgdc():
    assert_no_error((lambda:pgdc), "Fonction pgdc non définie")
    TESTS=[
        (11,19,1),
        (12,4,4),
        (5,75,5),
        (12,18,6),
        (-12,18,6),
        (12,-18,6),
        (-12,-18,6),
    ]
    for a,b,exp in TESTS:
        for a,b in ((a,b),(b,a)):
            act = pgdc(a,b)
            assert act==exp, "pgdc({},{}): {} should equal {}".format(a,b,act,exp)




@Test
def q9_test_Fraction_avec_pgdc():

    TESTS=[
        (1,2, 1,2),
        (-3,2, -3,2),
        (3,-2, -3,2),
        (17,12, 17,12),
        (16,32, 1,2),
        (-16,-32, 1,2),
        (-16,32, -1,2),
        (16,-32, -1,2),
        (355479819818010,-165890582581738, -15,7),
    ]
    for n,d,nn,dd in TESTS:
        assert_frac(Fraction(n,d), nn,dd)




@Test
def q10_test_big():
    a = Fraction(17, 817881771921773217717717)
    b = Fraction(2900907499261523127009477952858308, 365843487434343437)
    m = a.mul(b)

    print("({}/{}).mul({}/{}):".format(a.num,a.denom, b.num,b.denom))
    assert_frac(m, 60296523508, 365843487434343437)





