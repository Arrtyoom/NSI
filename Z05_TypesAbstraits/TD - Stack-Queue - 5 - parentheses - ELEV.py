"""
Implantations de piles et files utilisables dans votre code:
"""

class Stack:
    """ Une Stack est représentée avec le "top" de la pile à droite """

    def __init__(self, iterable=()):  self._pile=list(iterable)

    def __repr__(self):  return str(self._pile)

    def push(self,v):    self._pile.append(v)

    def pop(self):       return self._pile.pop()

    def is_empty(self):  return len(self._pile) == 0



from collections import deque

class Queue:
    """ Une Queue est représentée avec la tête de la file à droite """

    def __init__(self, iterable=()):  self._q=deque(iterable)

    def __repr__(self):   return str(self._q)

    def enqueue(self,v):  self._q.appendleft(v)

    def dequeue(self):    return self._q.pop()

    def is_empty(self):   return len(self._q) == 0







def valid_parentheses(s: str) -> bool:
    """ Prend une chaîne de caractères ne contenant que des parenthèses"(" et ")",
        et indique si le parenthésage est correct ou non.
    """

    # Proto code :

    # Fonction valid_parentheses(expr:str) -> bool:
    # Créer une pile vide
    # Pour Chaque caractère d’expr:
    # Si c'est une parenthèse ouvrante:
    # Stocker le caractère dans la pile
    # Ou Si c'est une parenthèse fermante:
    # Si le caractère au top de la pile n'est pas une parenthèse ouvrante:
    # renvoie Faux
    # Sinon:
    # renvoie Vrai
    # Fin Si
    # Fin Si
    # Fin Pour
    # Renvoyer ...
    # Fin Fonction

    # Code pour la Q5

    pile = Stack()
    for charac in s:
        # controle si le charactere est une parenthese ouvrante ou fermante
        if charac == '(': pile.push( charac )
        if charac == ')': 
            # si la parenthes est fermante on verifie si la pile n'est pas sois vide ou sois ai la mauvaise parenthese
            if pile.is_empty(): return False
            
            dernier_charac = pile.pop()
            if dernier_charac != '(': return False

    # si la parenthese n'est pas vide a la fin alors ca renvoie faux 
    if pile.is_empty() : return True 
    else : return False












def valid_more_parentheses(s: str) -> bool:
    """ Prend une expression mathématique et valide les parenthèses/crochets
        accolades qu'elle contient.
        @s: expression mathématique (nombres parenthèses, espaces, opérateurs)
        @return: vrai si les parenthèses sont correctement associées.
    """
    pile = Stack()
    # open_p  = ['(','[','{']
    # close_p = [')',']','}']
        
    

    for charac in s : 

        if charac in ['(','[','{'] : pile.push(charac)

        if charac == ')' : 
            if pile.is_empty(): return False 
            dernier_charac = pile.pop()
            if dernier_charac != '(' : return False
        
        if charac == ']' : 
            if pile.is_empty(): return False 
            dernier_charac = pile.pop()
            if dernier_charac != '[' : return False
        
        if charac == '}' : 
            if pile.is_empty(): return False 
            dernier_charac = pile.pop()
            if dernier_charac != '{' : return False

        else : continue

    if pile.is_empty() : return True
    else : return False         
        














def tests(func):
    TESTS=[
        (True,  '()'),
        (False, ')()'),
        (False, ')'),
        (False, '(((('),
        (False, '(((())'),
        (True,  '(()())'),
        (True,  '(()((())())())'),
        (True,  '(((((()())))))'),
        (False, ')('),
        (False, '(()())('),
        (False, '((()())('),
        (False, "()())()"),
        (False, "(((()()()"),
        (False, "())(((())))"),
        (False, "(((()()))((())))))()))"),
    ]

    for exp, s in TESTS:
        act = func(s)
        assert act==exp, "{}: {} devrait être {}".format(s,act,exp)
    else:
        print('ok')

tests(valid_parentheses)










valids=(
    "[X I{({J61C [w d mIeK](){}I208b}c([b4ng2Z7h()])N)}]",
    "{79x[({ o{xf}{}([])(())})5xslz [{ 5}]BN]}",
    "MT{}yBkm   ",
    "[{({t[]})}Nguy( tqG)[{}MO iTN]]AA",
    "[{7MS4 {}}(68ns XlMM){X }[3H]]",
    "([ojRa]hi[]14Bbdh{2 }()[](10rT3r ))",
    "6oyxurS0yeuan{}T iyw3{Sao t}[uQsV{}]",
    "{[{[[]]}]}",
    "(x ())c {{}} t W",
    "{{}}PJ0x",
    "({(Ymi{}()){{{}}}})  FD7[u L]{[D wX]}7p",
    "{{}}vU ()",
    "((H54Q{}[]{}6 1))",
    "N 8 n[[  h1H{}  CCU(  8)U[]XK{({})}]] E21if",
    "{(mXv )}()pe",
    "U[{ 2LO()}]9Z([{ Hz}])(SlEZE7m{}{}[[]]T{}A)",
    "[(({L Fj()fM}))E1  ul TNJ{}UUBR(()())fn4cv X ]",
    "[(()qLM)]{H{[]}fy65UsY[]}Mqlx({()}) Fc ",
    "J mPzujRGI(A)",
    "[[{t ebnJxLFys{}d7HcgBpTVN1vyy4aDRhXqNaWR}wC n]]FZ mCRI",
    "j[m3 G ()[]]",
    "BEpJ[ []] GIL{}",
    "(([])[]wOS J)fUc2[][[A]]([])",
    "(h iVu)",
    "(([]()([]){}[]{Ic}yPK))",
    "[[[]Y9YlNIlitM]V6]7LU [(())]tgf{8qu }D{GKB 8C}",
    "{8 e()B}({}) r(){}{}A",
    "hK",
    "K[][]7O",
    "{{}}",
    "Nq   V  b{[()]rto8}pPC[]TWTXK{()}",
    "({} i)",
    "{}",
    "((KV5 D)[]OJJgJ 1 0{GR  UAbS})",
    "CL su [SC 37D{}]()N CGi",
    "[{{}}](o2u) suats[[i ]Z]OM A[()]",
    "(x  n{(Qr ualY JJ)})({})x( ()([])5 z)",
    "(ql2j 6{})[[]]6{}z D[][[]]  7",
    "jQD{5 4[G{}6z](7  BiZVx(wz0))}",
    "(T ((9 OE)){{}}rh)(psuk{}16VPGp6x)A",
)

not_valids =(
    "(",
	")",
	")(",
	"))((",
	")()(",
	"(()",
	"))",
	"())",
	"(()",
	"()()())",
	"()())",
	")))))))))",
	"((((((((",
	"(}",
    "([)]",
    "{([})]",
	"{]",
	"{{))",
	"{(})",
	"{{))",
	"({",
	"[",
	"]",
    "jQD{5 4[G{]}6z(7  BiZVx(wz0))}",
    "(T ((9 OE)){{}}rh)psuk{ff(vd}16VPGp6x)A",
)

def tests_more(data, exp):
    for s in data:
        act = valid_more_parentheses(s)
        assert act==exp, "{}: {} devrait être {}".format(s,act,exp)
    else:
        print('ok')

tests_more(valids, True)
tests_more(not_valids, False)
tests(valid_more_parentheses)

