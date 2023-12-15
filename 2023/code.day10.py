#! /usr/bin/python3.10

import sys

from shapely.geometry import Point, Polygon

result = 0
x = 0
y = 0
lines = []

assoc = {
    'F': {
        'south': {'move': (1, 0), 'dest': 'west'},
        'east': {'move': (0, 1), 'dest': 'north'},
    },
    '|': {
        'north': {'move': (0, 1), 'dest': 'north'},
        'south': {'move': (0, -1), 'dest': 'south'},
    },
    '-': {
        'east': {'move': (-1, 0), 'dest': 'east'},
        'west': {'move': (1, 0), 'dest': 'west'},
    },
    'L': {
        'north': {'move': (1, 0), 'dest': 'west'},
        'east': {'move': (0, -1), 'dest': 'south'},
    },
    'J': {
        'north': {'move': (-1, 0), 'dest': 'east'},
        'west': {'move': (0, -1), 'dest': 'south'},
    },
    '7': {
        'south': {'move': (-1, 0), 'dest': 'east'},
        'west': {'move': (0, 1), 'dest': 'north'},
    }
}

with open(sys.argv[1], 'r') as file:
    file_content = file.read().strip()
    lines = file_content.split('\n')

index = 0
for line in lines:
    if 'S' in line:
        y = index
        x = line.find('S')
    index += 1

elem = '|'
prev = 'south'

all_points = []
for x1 in range(1, len(lines[0]) - 1):
    for y1 in range(1, len(lines) - 1):
        all_points.append(tuple([x1, y1]))

print()
poly_coord = [tuple([x, y])]
while elem != 'S':
    dest_precised = assoc[elem][prev]['dest']
    move_x, move_y = assoc[elem][prev]['move']
    x, y = x + move_x, y + move_y
    tup = tuple([x, y])
    poly_coord.append(tup)
    if tup in all_points:
        all_points.remove(tup)

    elem = lines[y][x]
    prev = dest_precised

    result += 1

print('first star: ', result / 2)

# second star
poly = Polygon(poly_coord)
result_p2 = 0
for point in all_points:
    x, y = point
    if Point(x, y).within(poly):
        result_p2 += 1

print('second star: ', result_p2)
