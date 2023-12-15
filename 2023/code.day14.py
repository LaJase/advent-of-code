#! /usr/bin/python3.10

import sys
import copy

print()
print("==========================================")
with open(sys.argv[1], "r") as file:
    file_content = file.read().strip()
    lines = file_content.split("\n")
    records = [[c for c in row] for row in lines]


def rotation_sens_aiguilles_montre(matrice):
    lignes, colonnes = len(matrice), len(matrice[0])
    nouvelle_matrice = [[None] * lignes for _ in range(colonnes)]

    for i in range(colonnes):
        for j in range(lignes):
            nouvelle_matrice[i][j] = matrice[lignes - 1 - j][i]

    return nouvelle_matrice


def roll_execution(grid):
    line_numb = len(grid)
    col_numb = len(grid[0])
    for col_index in range(col_numb):
        for _ in range(line_numb):
            for line_index in range(line_numb):
                if line_index > 0:
                    if (
                        grid[line_index][col_index] == "O"
                        and grid[line_index - 1][col_index] == "."
                    ):
                        grid[line_index][col_index] = "."
                        grid[line_index - 1][col_index] = "O"

    return grid


def calcul_point(records):
    res = 0
    line_numb = len(records)
    col_numb = len(records[0])
    for r in range(line_numb):
        for c in range(col_numb):
            if records[r][c] == "O":
                res += len(records) - r

    return res


# First star
print("first star: ", calcul_point(roll_execution(copy.deepcopy(records))))

# second star
cycle = 0
isEquals = False
memoire = {}
while cycle < 1000000000 and not isEquals:
    cycle += 1
    for i in range(4):
        records = roll_execution(records)
        records = rotation_sens_aiguilles_montre(records)

    # Convertir la liste de listes en un tuple (type immuable)
    tuple_immuable = tuple(tuple(element) for element in records)

    # Calculer le hachage du tuple immuable
    hash_result = hash(tuple_immuable)

    if hash_result in memoire:
        longueur_cycle = cycle - memoire[hash_result]
        nombre_cycle_possibles = (1000000000 - cycle) // longueur_cycle
        cycle += nombre_cycle_possibles * longueur_cycle
    memoire[hash_result] = cycle

print("second star: ", calcul_point(records))
