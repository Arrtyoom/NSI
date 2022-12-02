




class Maillon:
    """ Représente un maillon d'une liste chaînée. Chaque maillon porte une
        valeur et peut accéder au suivant dans la liste chaînée.

        Attributs:      valeur (int)
                        suivant (Maillon ou None)
    """

    def __init__(self, valeur, suivant=None):
        self.valeur = valeur
        self.suivant = suivant

    def ajoute_tete(self,v):
        return Maillon(v,self)

    def somme(self):
        if self.suivant is None:
            return self.valeur
        return self.valeur + self.suivant.somme()

    












""" Ajouter le code permettant de créer les objets suivants, avec ces noms de
variables:
        a : un maillon ayant pour valeur 33 et pas de suivant
        b : un maillon ayant pour valeur 5 et pas de suivant
        c : un maillon ayant pour valeur 4 et b comme suivant
        d : un maillon ayant pour valeur 2 et c comme suivant
        e : un maillon ayant pour valeur 1 et d comme suivant
"""
a = Maillon(33)
b = Maillon(5)
c = Maillon(4,b)
d = Maillon(2,c)
e = Maillon(1,d)



#  tests:
all_definitions = globals()

for var_name in 'a b c d e'.split():

    assert var_name in all_definitions, f"La variable {var_name!r} n'est pas définie"

    obj = all_definitions[var_name]

    """
    La variable obj ci-dessus contient l'objet que vous avez (normalement)
    défini plus haut.
    On veut maintenant ajouter à la place de cette exception un test pour
    vérifier que c'est bien une instance de la classe Maillon.

    1) Afficher dans la console l'aide concernant la fonction isinstance avec:
            help(isinstance)

    2) Lire ce qui est affiché dans la console pour vous aider à vous souvenir
       comment utiliser la fonction isinstance, puis supprimer cette excpetion
       et la remplacer par un test qui va vérifier que obj est bien une instance
       de la classe Maillon.
    """

    assert isinstance(obj,Maillon), "pas la bonne classe"



"""
En fait, les méthodes tete et queue de la classe Maillon n'ont pas d'utilité,
ici: on pourrait très bien accéder directement aux propriétés valeur et suivant.

1) Supprimer les deux méthodes et réécrire la méthode somme.

2) Ecrire un test permettant de vérifier que la somme en partant de e vaut 12
   (...et on n'oublie pas de supprimer cette exception...)
"""

assert e.somme() == 12, f"la somme n'est pas egale a 12 mais a {e.somme()}"



'''
On veut maintenant ajouter une méthode pour ajouter un maillon devant un autre.
L'interface souhaitée est la suivante:

    nom de méthode: "ajoute_tete"
    argument:       Valeur pour le nouveau maillon à placer devant l'actuel
    renvoie:        Le nouvel objet de la classe Maillon, pour lequel le suivant
                    est l'instance en cours.

1) Supprimer "raise Exception"
2) Ajouter la méthode "ajoute_tete" dans le code de la classe Maillon. Vérifier
   que les deux tests suivants passent.
'''

assert hasattr(Maillon, "ajoute_tete"), "la méthode 'ajoute_tete' n'est pas définie"

from inspect import signature
params = signature(Maillon.ajoute_tete).parameters
msg = ("Il manque quelque chose au niveau des arguments d'ajoute_tete..."
            if len(params) < ord('b')-0x60 else
       "Trop d'arguments pour ajoute_tete!" if len(params)>ord('!')-0x1f else "")

assert len(params)==ord('B')+ord('\n')-ord('J'), msg



"""
1) En travaillant à partir de l'instance e, c'est-à-dire SANS UTILISER VOUS-MÊMES
   LE CONSTRUCTEUR, créer maintent un maillon ayant la valeur 99 et e comme suivant,
   cet objet doit être assigner à la variable "last".

2) Ecrire un test permettant de s'assurer que la somme depuis le maillon last
vaut 111. Lancer le code et vérifier que vous n'avez pas fait de bêtises.
"""
last = e.ajoute_tete(99)
assert last.somme() == 111, f"la somme de last n'est pas egale a 111 mais {last.somme()}"

print('ok!')