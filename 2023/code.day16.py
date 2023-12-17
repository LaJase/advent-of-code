#! /usr/bin/python3.10

import sys
import copy
import time

print()
print("=========================================")
with open(sys.argv[1], "r") as file:
    file_content = file.read().strip()
    lines = file_content.split("\n")
    records = [[c for c in row] for row in lines]

line_number = len(records)
col_number = len(records[0])

assoc = {
    "|": {
        "right": {"move": [(0, 1), (0, -1)], "dest": "north"},
        "left": {"move": (0, -1), "dest": "south"},
    },
    "-": {
        "east": {"move": (-1, 0), "dest": "east"},
        "west": {"move": (1, 0), "dest": "west"},
    },
    "/": {
        "north": {"move": (1, 0), "dest": "west"},
        "east": {"move": (0, -1), "dest": "south"},
    },
    "\\": {
        "north": {"move": (-1, 0), "dest": "east"},
        "west": {"move": (0, -1), "dest": "south"},
    },
}


def follower(grid, pos, grid_length):
    for x, y in pos:
        grid[y][x] = "#"

    for i in range(grid_length):
        print("".join(grid[i]))


summerized = copy.deepcopy(records)

tiles = []
tiles.append((0, 0, "right"))
energized = set()
while len(tiles) > 0:
    # print(tiles)
    x, y, direction = tiles.pop()
    if 0 <= x < col_number and 0 <= y < line_number:
        energized.add((x, y))
        print()
        print(x, y, direction, records[y][x])

        if records[y][x] == "|":
            if direction == "right" or direction == "left":
                tiles.append((x, y + 1, "down"))
                tiles.append((x, y - 1, "up"))
            elif direction == "up":
                tiles.append((x, y - 1, "up"))
            elif direction == "down":
                tiles.append((x, y + 1, "down"))
        if records[y][x] == "-":
            if direction == "down" or direction == "up":
                tiles.append((x - 1, y, "left"))
                tiles.append((x + 1, y, "right"))
            elif direction == "right":
                tiles.append((x + 1, y, "right"))
            elif direction == "left":
                tiles.append((x - 1, y, "left"))
        if records[y][x] == "/":
            if direction == "down":
                tiles.append((x - 1, y, "left"))
            elif direction == "up":
                tiles.append((x + 1, y, "right"))
            elif direction == "right":
                tiles.append((x, y - 1, "up"))
            elif direction == "up":
                tiles.append((x + 1, y, "down"))
        if records[y][x] == "\\":
            if direction == "down":
                tiles.append((x + 1, y, "right"))
            elif direction == "up":
                tiles.append((x - 1, y, "left"))
            elif direction == "right":
                tiles.append((x, y + 1, "down"))
            elif direction == "left":
                tiles.append((x, y - 1, "up"))
        if records[y][x] == ".":
            if direction == "down":
                tiles.append((x, y + 1, "down"))
            elif direction == "up":
                tiles.append((x, y - 1, "up"))
            elif direction == "right":
                tiles.append((x + 1, y, "right"))
            elif direction == "left":
                tiles.append((x - 1, y, "left"))

        print(follower(summerized, energized, line_number))

    time.sleep(1)


print(energized)
print("first star :", len(energized))

print("second star:")
