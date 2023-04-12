import random

"""
Module: sudoku.py Un programme pour manipuler des grilles de sudoku.

Les variables grille_x peuvent vous servir à tester votre programme.
Elles représentent toutes des grilles de Sudoku valides à divers
stades d'avancement: grille_0 est vide, grille_1 semi-remplie et
grille_2 entièrement remplie.
"""

grille_0 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

grille_1 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 2, 0, 0, 5, 0, 7, 6, 0],
    [0, 6, 0, 0, 0, 0, 0, 0, 3],
    [5, 0, 0, 0, 0, 0, 2, 0, 7],
    [0, 3, 0, 0, 1, 0, 0, 0, 0],
    [2, 0, 0, 4, 0, 0, 0, 3, 0],
    [0, 0, 0, 6, 0, 0, 0, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 2, 7, 0, 0, 4, 0],
]

grille_2 = [
    [6, 2, 5, 8, 4, 3, 7, 9, 1],
    [7, 9, 1, 2, 6, 5, 4, 8, 3],
    [4, 8, 3, 9, 7, 1, 6, 2, 5],
    [8, 1, 4, 5, 9, 7, 2, 3, 6],
    [2, 3, 6, 1, 8, 4, 9, 5, 7],
    [9, 5, 7, 3, 2, 6, 8, 1, 4],
    [5, 6, 9, 4, 3, 2, 1, 7, 8],
    [3, 4, 2, 7, 1, 8, 5, 6, 9],
    [1, 7, 8, 6, 5, 9, 3, 4, 2],
]

grille_False = [
    [6, 2, 5, 8, 4, 3, 7, 9, 1],
    [7, 2, 1, 2, 6, 5, 4, 8, 3],
    [4, 8, 3, 9, 7, 1, 6, 2, 5],
    [8, 1, 4, 5, 9, 7, 2, 3, 6],
    [2, 3, 6, 1, 8, 4, 9, 5, 7],
    [9, 5, 7, 3, 2, 6, 8, 1, 4],
    [5, 6, 9, 4, 3, 2, 1, 7, 8],
    [3, 4, 2, 7, 1, 8, 5, 6, 9],
    [1, 7, 8, 6, 5, 9, 3, 4, 2],
]

grille_False_0 = [
    [0, 2, 5, 8, 4, 3, 7, 9, 1],
    [7, 9, 1, 2, 6, 5, 4, 8, 3],
    [4, 8, 3, 9, 7, 1, 6, 2, 5],
    [8, 1, 4, 5, 9, 7, 2, 3, 6],
    [2, 3, 6, 1, 8, 4, 9, 5, 7],
    [9, 5, 7, 3, 2, 6, 8, 1, 4],
    [5, 6, 9, 4, 3, 2, 1, 7, 8],
    [3, 4, 2, 7, 1, 8, 5, 6, 9],
    [1, 7, 8, 6, 5, 9, 3, 4, 2],
]

"""
Les deux fonctions ci-dessous sont données à titre d'exemple.  Le
reste est à programmer à la suite de ces fonctions.
"""


def afficher(x):
    """
    Affiche une grille de sudoku g de taille 9x9 sur le terminal.
    """
    ligne0 = "╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗"
    ligne1 = "║ . │ . │ . ║ . │ . │ . ║ . │ . │ . ║"
    ligne2 = "╟───┼───┼───╫───┼───┼───╫───┼───┼───╢"
    ligne3 = "╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣"
    ligne4 = "╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝"

    valeurs = [[""]+[" 1234567890"[case] for case in ligne] for ligne in x]

    print(ligne0)
    for ligne in range(1, 9+1):
        print("".join(n+s for (n, s) in zip(valeurs[ligne-1], ligne1.split("."))))
        print([ligne2, ligne3, ligne4][(ligne % 9 == 0) + (ligne % 3 == 0)])


###############################################################################
#   PARTIE I:

######################################
def ligne(x, i):
    """
    Renvoie la ligne i de la grille de sudoku x
    """
    return x[i-1]

# return la ligne de rang 1-9
# print(ligne(grille_1, 1))
######################################
######################################


def unique(x):
    """
    Renvoie False si on a 2 élément identique
    et True si tout les elements sont uniniques
    (ne prend pas en compte les 0)
    """
    for i in range(len(x)):
        if x[i] in x[i+1:] and x[i] != 0:
            return False
    return True

# print(unique([1, 2, 3, 4, 5, 6, 7, 8, 9]))
# print(unique([0, 0, 0, 0, 0, 0, 0, 2, 1]))
# print(unique([1, 2, 3, 4, 5, 6, 7, 9, 9]))
######################################
######################################


def colonne(x, i):
    """
    Renvoie la colonne i de la grille de sudoku x
    """
    colo = []
    for j in x:
        colo.append(j[i-1])
    return colo

# return la colonne de rang 1-9
# print(colonne(grille_1, 1))
######################################
######################################


def region(x, i):
    """
    Renvoie la colonne i de la grille de sudoku x
    """
    re = []
    k = ((((i-1) % 3) * 3) + 2, (((i-1) // 3) * 3) + 2)
    for i in range(-1, 2):
        for j in range(-1, 2):
            re.append(x[(k[1] + j) - 1][(k[0] + i) - 1])
    return re

# return la region de rang 1-9
# print(region(grille_1, 1))
######################################
######################################


def ajouter(x, i, j, v):
    """
    ajoute la valeur vaux coordonées i, j
    de la grille x
    """
    x[i-1][j-1] = v

# change la grille de la ligne i de rang 1-9 et j de rang 1-9
# afficher(grille_1)
# ajouter(grille_1, 1, 1, 1)
# afficher(grille_1)
######################################
######################################


def verifier(x):
    """
    verifie que la grille de sodoku est correctement remplie
    renvoie True si si toutes les lignes, colonnes et
    régions de la grille sont valides
    et si la grille ne contient pas de 0, et False sinon
    """
    for o in range(1, 10):
        li = ligne(x, o)
        co = colonne(x, o)
        re = region(x, o)
        if 0 in li or 0 in co or 0 in re:
            return False
        if not unique(li) or not unique(co) or not unique(re):
            return False
    return True


# print(verifier(grille_1))
# print(verifier(grille_2))
# print(verifier(grille_False))
################################
################################


def jouer(x):
    """
    prend en entrée une grille et qui demande à l’utilisateur
    un triplet de valeurs(i, j, v) représentant une valeur
    à placer aux coordonnées(i, j) sur la grille
    """
    afficher(x)
    i = int(input("coordonnée en ligne du nombre a placer entre 1 et 9"))
    j = int(input("coordonnée en colonne du nombre a placer entre 1 et 9"))
    v = int(input("entré du nombre a placer"))
    ajouter(x, i, j, v)
    if verifier(x):
        print("Bravo!")
        afficher(x)
        return None
    jouer(x)

# jouer(grille_False_0)
# jouer(grille_1)
#################################################################
#################################################################
#   PARTIE II:


##############################
def solutions(x):
    """
    ressort toute les solutions possible
    d'une grille dans un dictionnaire
    par nombre de possibilité
    """
    Posibi = {i: [] for i in range(10)}
    for i in range(1, 10):
        for j in range(1, 10):
            if x[i-1][j-1] == 0:
                k = 3*((i-1)//3)+((j-1)//3)+1
                Temp = [o for o in range(1, 10)]
                for p in ligne(x, i):
                    try:
                        Temp.remove(p)
                    except ValueError:
                        pass
                for p in region(x, k):
                    try:
                        Temp.remove(p)
                    except ValueError:
                        pass
                for p in colonne(x, j):
                    try:
                        Temp.remove(p)
                    except ValueError:
                        pass
                Posibi[len(Temp)].append((i, j, Temp.copy()))
    return Posibi

# print(solutions(grille_1))
# print(solutions(grille_False_0))
##################################
##################################


def resoudre(x):
    """
    resout une grille
    """
    Posibi = solutions(x)
    liste = []
    for i in Posibi.keys():
        liste.extend(Posibi[i])
    if liste == []:
        return x
    if Posibi[0] != []:
        return False
    for v in liste[0][2]:
        ajouter(x, liste[0][0], liste[0][1], v)
        temp = resoudre(x)
        if not temp:
            ajouter(x, liste[0][0], liste[0][1], 0)
        else:
            return x
    return False


# afficher(resoudre(grille_1))


def generer(x):
    """
    genere une nouvelle grille
    a partir d'une grille vide
    """
    Posibi = solutions(x)
    liste = []
    for i in Posibi.keys():
        liste.extend(Posibi[i])
    if liste == []:
        return x
    if Posibi[0] != []:
        return False
    random.shuffle(liste[0][2])
    for v in liste[0][2]:
        ajouter(x, liste[0][0], liste[0][1], v)
        temp = resoudre(x)
        if not temp:
            ajouter(x, liste[0][0], liste[0][1], 0)
        else:
            return x
    return False

afficher(generer(grille_0))


def nouvelle():
    """
    Crée une nouvelle grille jouable
    """
    grille = [[0 for _ in range(9)] for _ in range(9)]
    generer(grille)
    for _ in range(64):
        ajouter(grille, random.randint(1, 9), random.randint(1, 9), 0)
    return grille

# afficher(nouvelle())
