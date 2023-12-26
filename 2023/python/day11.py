#! /usr/bin/python3.10

import re
import sys


def calc_distance(paires, prt2):
    result = 0
    expansion = 10**6-1 if prt2 else 1
    for i, (r, c) in enumerate(paires):
        for j in range(i, len(paires)):
            r2, c2 = paires[j]
            dij = abs(r2-r)+abs(c2-c)
            for er in found_row:
                if min(r, r2) <= er <= max(r, r2):
                    dij += expansion
            for ec in found_column:
                if min(c, c2) <= ec <= max(c, c2):
                    dij += expansion
            result += dij

    return result


found_row = set()
found_column = set()
galaxies = []
image = []

with open(sys.argv[1], 'r') as file:
    file_content = file.read().strip()
    lines = file_content.split('\n')

for index, line in enumerate(lines):
    if '#' not in line:
        found_row.add(index)
    else:
        indices = [index.start() for index in re.finditer(pattern='#', string=line)]
        for indice in indices:
            galaxies.append((index, indice))

    image.append([c for c in line])

size_col = len(image)
size_row = len(image[0])

for index_col in range(size_row):
    empty = True
    for line in image:
        if line[index_col] == '#':
            empty = False

    if empty:
        found_column.add(index_col)

print('first star: ', calc_distance(galaxies, False))
print('second star: ', calc_distance(galaxies, True))
