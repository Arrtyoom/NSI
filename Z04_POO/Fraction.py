class Fraction:
    def __init__(self,x,y=1) -> None:
        if y < 0:
            x,y = -x,-y
        
        diviseur_commun = pgdc(x,y)

        self.num = x // diviseur_commun
        self.denom = y // diviseur_commun

        # self.num //= pgdc(self.num, self.denom)
        # self.denom //= pgdc(self.num, self.denom)

    def __repr__(self) -> str:
        return f"Fraction({self.num},{self.denom}"

    def __str__(self) -> str:
        return f"{self.num}/{self.denom}"

    # 4) a/b et c/d
    # add=(a*d)/(b*d)+(c*b)/(d*b)
    # sub=(a*d)/(b*d)-(c*b)/(d*b)
    # mult=(a*c)/(d*b)
    # div=(a*d)/(b*c)

    def add(self,other:"Fraction"):
        a,b = self.num, self.denom
        c,d = other.num, other.denom

        result = Fraction((a*d+c*b) , (b*d))

        return result

    def sub(self,other:"Fraction"):
        a,b = self.num, self.denom
        c,d = other.num, other.denom

        result = Fraction((a*d - c*b) , (b*d))

        return result

    def mul(self,other:"Fraction"):
        a,b = self.num, self.denom
        c,d = other.num, other.denom

        result = Fraction((a*c) , (d*b))

        return result

    def div(self,other:"Fraction"):
        a,b = self.num, self.denom
        c,d = other.num, other.denom

        result = Fraction((a*d) , (b*c))

        return result

def pgdc(a,b):
    if b == 0: 
        return abs(a) 
    elif b != 0:
        return pgdc(abs(b),abs(a%b))

#----------------------------------