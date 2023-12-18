#! /usr/bin/python3.10

import sys

from re import search
from time import perf_counter
from shapely.geometry import Polygon

total_start_time = perf_counter()
print()
print("=========================================")
with open(sys.argv[1], "r") as file:
    file_content = file.read().strip()
    lines = file_content.split("\n")
    records = [row.split() for row in lines]


def calc_nb_point(input):
    current = (0, 0)
    pos = []
    pos.append((0, 0))
    moves = {"L": (-1, 0), "R": (1, 0), "U": (0, -1), "D": (0, 1)}
    for dir, length in input:
        new_x = current[0] + moves[dir][0] * int(length)
        new_y = current[1] + moves[dir][1] * int(length)
        current = (new_x, new_y)
        if current not in pos:
            pos.append(current)

    poly = Polygon(pos)
    return poly.area + poly.length / 2 + 1


def reorg_input(input_to_reorg):
    dir_tab = ["R", "D", "L", "U"]
    reorg = []
    for line in input_to_reorg:
        resultat = search(r"\((.*?)\)", line)
        if resultat:
            contenu_entre_parentheses = resultat.group(1)
            nombre_decimal = int(contenu_entre_parentheses[1:-1], 16)
            dir = dir_tab[int(contenu_entre_parentheses[-1])]
            reorg.append([dir, nombre_decimal])

    return reorg


start_time = perf_counter()
print("first star: ", calc_nb_point([[d, leng] for d, leng, _ in records]))
print("Time:", round(perf_counter() - start_time, 4), "sec")
print()


start_time = perf_counter()
print("second star:", calc_nb_point(reorg_input(lines)))
print("Time:", round(perf_counter() - start_time, 4), "sec")
print()
print("Total time:", round(perf_counter() - total_start_time, 4), "sec")
print("=========================================")
