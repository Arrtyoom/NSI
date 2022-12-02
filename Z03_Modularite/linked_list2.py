from typing import NewType, List


LinkedList = NewType('LinkedList', tuple)



def creer_vide() -> LinkedList:
    """ Crée une liste chaînée vide... (oui, c'est une fonction qui ne sert pas
        à grand chose à 1ère vue... :p )
    """
    return None


def ajoute_tete(v:int, linked:LinkedList) -> LinkedList:
    """ ajoute_tete un maillon avec la valeur v à l'avant de la liste chaînée linked """
    return (v,linked)


def tete(linked:LinkedList) -> int:
    """ Renvoie la valeur portée par le maillon à la tête de la liste """
    return linked[0]


def queue(linked:LinkedList) -> LinkedList:
    """ Renvoie la queue du maillon en cours (=la liste chaînée sans le maillon de tête) """
    return linked[1]


def est_vide(linked:LinkedList) -> bool:
    """ Indique si la liste chaînée passée en argument est vide ou non """
    return linked == creer_vide()



#------------------------------



def to_linked_list(lst:List[int]) -> LinkedList:
    """ Convertit une liste d'entiers en liste chaînée:
            [1,22,34]  =>   1 -> 22 -> 34 -> None
        Le premier élément de la liste doit donc être la tête de la liste chaînée.
    """

    linked = creer_vide()
    for v in reversed(lst): ##for v in lst[::-1]:
        linked = ajoute_tete(v,linked)
    return linked




def taille(linked:LinkedList) -> int:
    """ Renvoie la taille de la liste chaînée (nombre de maillons):
            Ex:      a   <=>   1 -> 22 -> 34 -> None
                     taille(a) == 3
    """
    """
    longueur = 0
    if not est_vide(linked): # cas recursif
        longueur += 1
        return(taille(queue(linked)))
    return longueur
    """

    if est_vide(linked):
        return 0
    else:
        couper = queue(linked)
        regner = taille(couper)
        combiner = regner + 1
        return combiner








def somme(linked:LinkedList) -> int:
    """ Renvoie la somme des valeurs de la liste chaînée:
            Ex:      a   <=>   1 -> 22 -> 34 -> None
                     somme(a) == 57
    """

    """ version 0 
    S = 0
    copie = copy.deepcopy(linked)
    print(copie)

    #if est_vide(copie):
    #   return 0
    
    while type(copie[1]) == tuple:
         
        print("element",copie[0])
        S += copie[0] 
        print("somme",S)
        copie = queue(copie)

    return S + copie[0]
    """

    """version 1"""
    if est_vide(linked):
        return 0
    else:
        couper = queue(linked)
        regner = somme(couper)
        combiner = tete(linked) + regner
        return combiner
    
    











def get(linked:LinkedList, i:int) -> int:
    """ Renvoie la valeur du maillon à l'index i (indexation à 0):
            Ex: soit lkl la liste chaînée:    1 -> 22 -> 34 -> None
                get(lkl, 0) == 1
                get(lkl, 2) == 34
                get(lkl, 3) => Exception
    """

    """version 1
    """
    while i != 0:
        
        linked = queue(linked)
        i -= 1

        if tete(linked)==None:
            return Exception
    
    return tete(linked)



def to_list(a, lst):
    for i in range(taille(a)):
        lst.append(get(a,i))
    return lst



def concat(a:LinkedList, b:LinkedList) -> LinkedList:
    """ Concatène les deux listes chaînées a et b, en ajoutant b à la fin de a:

            a  <=>  1 -> 2 -> 3 -> None
            b  <=>  4 -> 5 -> None

            concat(a,b)  ==  1 -> 2 -> 3 -> 4 -> 5 -> None
    """

    #creer list vide
    #ajouter les valeurs en partant des dernieres valeurs de b puis celle de a 
    #retourner la list concatener 

	#Version Recursive

    if est_vide(a):
        return b
    else:
        couper   = queue(a)
        regner   = concat(couper)
        combiner = ajoute_tete( tete(a) , regner )
        return combiner
    
    """
	#Version Iterative

    lst = []
	
    to_list(a, lst)
    to_list(b, lst)

    c = creer_vide()
    for v in reversed(lst):
        c = ajoute_tete(v,c)
    
    return c
	"""