# Créé par Elève, le 12/09/2022 en Python 3.7
"""
Contexte:
---------

    On dispose d'une fonction recevant:
        * un tableau 2D, "maze", représentant un labyrinthe.
        * une position verticale x (indice de la rangée de maze à considérer)
        * une position horizontale y (indice de la colonne de maze à considérer)

    Sachant qu'on peut se déplacer horizontalement et verticalement dans le
    labyrinthe, le but de cette fonction est de donner le nombre de positions
    voisine de (x,y) (les arguments) dans maze.

    Le labyrinthe "maze" est composé de 0 et de 1:
        - 0 est un "mur": on ne peut pas y marcher
        - 1  est un emplacement libre
        - on ne peut pas sortir du labyrinthe (=sortir du tableau 2D)
        - les coordonnées sont données dans le sens d'indexation du tableau 2D:
                             (x,y) <=> maze[x][y]
        - la position passée en argument de la fonction, (x,y), est toujours sur
          un 1 dans maze.

    Exemples: voir la fonction de test.

(Aides et/ou améliorations possibles présentes à la fin du fhichier)
"""

from typing import Any

def is_inside(maze:Any ,i:int, j:int) -> bool :
    """Verifie si les coordonées (i,j) sont dans le labyrinthe ou pas"""
    #return x > 0 and x+1 < len(maze) and y > 0 and y+1 < len(maze[x])
    return 0 <= i < len(maze) and 0 <= j < len(maze[i])

def is_inside2(maze:Any ,i:int, j:int) -> bool :
    """Verifie si les coordonées (i,j) sont dans le labyrinthe ou pas"""
    return 0 < i < len(maze)-1 and 0 < j < len(maze[i])-1

def compte_voisins_libres(maze, x, y):
    """ Compte le nombre de voisins libres de la position (x,y) dans "maze" (<=>
    maze[x][y]). Une case voisine est une case jouxtant directement la
    position actuelle (haut, bas, droite, gauche).
    Un voisin est libre si la cellule corresondant contient la valeur 1.

    @maze: Tableau 2D rectangulaire (dimensions AxB, avec A et B > 0)
    @x,@y: Entiers indiquant les coordonnées du point d'origine dans "maze".
           La position d'origine est toujours sur un 1.
    @return: le nombre de voisins libres de la position actuelle (entier).
    """

    #----------------------------
    #version 6
    return maze[x-1][y] + maze[x+1][y] + maze[x][y-1] + maze[x][y+1] if is_inside2(maze,x,y) else False

    """
    #----------------------------
    #version 5

    somme,voisins = 0,[(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
    for i,j in voisins:
        somme += maze[i][j] if is_inside(maze,i,j) else 0
    return somme

    #----------------------------
    #version 4

    somme = 0

    somme += maze[x+1][y] if x < len(maze) - 1 else 0
    somme += maze[x-1][y] if x > 0 else 0
    somme += maze[x][y+1] if y < len(maze[x]) - 1 else 0
    somme += maze[x][y-1] if y > 0 else 0

    return somme

    #----------------------------
    #version 3

    def is_inside(maze,i,j):

        somme = 0
        long_max_x,long_max_y = len(maze) - 1, len(maze[0]) - 1
        #print(long_max_x,long_max_y)

        if x < long_max_x:
            #print(x,y)
            somme += maze[x+1][y]
            #print(somme)

        if x > 0:
            #print(x,y)
            somme += maze[x-1][y]
            #print(somme)

        if y < long_max_y:
            #print(x,y)
            somme += maze[x][y+1]
            #print(somme)

        if y > 0:
            #print(x,y)
            somme += maze[x][y-1]
            #print(somme)

        return somme

    somme = is_inside(maze,x,y)

    return somme

    #----------------------------
    #version 2

    somme = 0
    long_max_x,long_max_y = len(maze) - 1,len(maze[0]) - 1
    #print(long_max_x,long_max_y)

    if x < long_max_x:
        #print(x,y)
        somme += maze[x+1][y]
        #print(somme)

    if x > 0:
        #print(x,y)
        somme += maze[x-1][y]
        #print(somme)

    if y < long_max_y:
        #print(x,y)
        somme += maze[x][y+1]
        #print(somme)

    if y > 0:
        #print(x,y)
        somme += maze[x][y-1]
        #print(somme)

    return somme


    #---------------------------
    #version 1

    return maze[x-1][y] + maze[x+1][y] + maze[x][y-1] + maze[x][y+1]
    """
    ...





def run_tests():

    MAZE = [                     #x:
        [1,0,0,1,0,1,0,1,0,0,1], #0
        [0,0,1,0,0,0,0,0,1,0,0], #1
        [0,1,1,1,0,0,1,1,1,1,0], #2
        [0,0,0,1,0,0,0,1,1,0,1], #3
        [1,1,0,0,0,1,0,1,1,0,0], #4
        [0,0,0,1,0,0,1,0,0,1,0], #5
        [0,0,0,0,0,1,0,1,0,0,0], #6
        [1,0,0,1,0,0,0,0,0,0,1], #7
    # y: 0 1 2 3 4 5 6 7 8 9 0  <- ce dernier "0" est en fait un "10"
    ]


    TESTS = [
        (5,3,0),    # (x,y,résultat)
        (2,6,1),
        (1,2,1),
        (4,1,1),
        (5,6,0),
        (3,7,3),
        (2,8,4),
        (7,3,0),
        (0,3,0),
        (0,0,0),
        (7,10,0),
        (2,3,2)
    ]



    def check(maze, x, y, expected, loud=True):         # Fonction utilisée pour tester votre... fonction

        # crée un copie de maze, à envoyer à votre fonction
        copyMaze = [r[:] for r in maze]

        # calcul de votre résultat:
        actual = compte_voisins_libres(copyMaze, x, y)

        # construction du message puis affichage (si loud==True)
        msg = "\n\n\n{}\nposition: x,y = {},{}\nAttendu: {} voisins / trouvés: {}".format(
                    '\n'.join(map(str,maze)),x,y,n,actual
              )
        if loud or expected!=actual:
            print(msg)

        # teste votre résultat:
        assert expected==actual



    for x,y,n in TESTS:
        check(MAZE, x, y, n)
    print("OK!!\n\n")


run_tests()


"""
AIDES:
------

1) la première question à se poser est: sachant que vous êtes en maze[x][y],
   à quels paires d'indices/coordonnées se trouvent les "voisins" dans le
   labyrinthe?

2) hint: le code peut être écrit uniquement avec des conditions (mais c'est
   moche... Très moche...)

3) Python vous tend un piège ici... Lequel? Comment l'éviter? (nota: il y a au
   moins un test dédié à ce type de cas)

4) Si vous avez utilisé de simples (et moches ;p ) conditions, vous pouvez essayer
   de généraliser le code.
   Principe: on regarde dans une direction donnée pour voir si la case en question
   est libre. On doit faire la même chose dans 4 directions différentes.
   Cela appelle à utiliser quel type de "structure de contrôle" dans le code?
"""


