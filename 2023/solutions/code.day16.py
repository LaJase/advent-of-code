#! /usr/bin/python3.10

import sys
from collections import deque
from time import perf_counter

total_start_time = perf_counter()
with open(sys.argv[1], "r") as file:
    file_content = file.read().strip()
    lines = file_content.split("\n")
    records = [[c for c in row] for row in lines]

line_number = len(records)
col_number = len(records[0])

directions = {"E": (1, 0), "W": (-1, 0), "N": (0, -1), "S": (0, 1)}
right_mirror = {"E": "N", "W": "S", "N": "E", "S": "W"}
left_mirror = {"E": "S", "W": "N", "N": "W", "S": "E"}


def get_energized_tiles(grid, start_beam=(-1, 0, "E")):
    beam_queue = deque([start_beam])
    energized_tiles = set()
    beam_history = set()

    while beam_queue:
        x, y, direction = beam_queue.pop()
        if (x, y, direction) in beam_history:
            continue

        energized_tiles.add((x, y))
        beam_history.add((x, y, direction))

        dx, dy = directions[direction]
        next_x, next_y = x + dx, y + dy

        if next_x < 0 or next_x >= len(grid[0]) or next_y < 0 or next_y >= len(grid):
            continue

        match grid[next_y][next_x]:
            case ".":
                beam_queue.append((next_x, next_y, direction))
            case "|":
                if direction in ("N", "S"):
                    beam_queue.append((next_x, next_y, direction))
                else:
                    beam_queue.append((next_x, next_y, "N"))
                    beam_queue.append((next_x, next_y, "S"))
            case "-":
                if direction in ("E", "W"):
                    beam_queue.append((next_x, next_y, direction))
                else:
                    beam_queue.append((next_x, next_y, "E"))
                    beam_queue.append((next_x, next_y, "W"))
            case "/":
                beam_queue.append((next_x, next_y, right_mirror[direction]))
            case "\\":
                beam_queue.append((next_x, next_y, left_mirror[direction]))

    return len(energized_tiles) - 1


print()
print("=========================================")
start_time = perf_counter()
print("first star :", get_energized_tiles(records))
print("Time: ", perf_counter() - start_time)
print()

start_time = perf_counter()
energized_list = []
for i in range(len(records)):
    energized_list.append(get_energized_tiles(records, (i, -1, "S")))
    energized_list.append(get_energized_tiles(records, (i, len(records), "N")))
    energized_list.append(get_energized_tiles(records, (-1, i, "E")))
    energized_list.append(get_energized_tiles(records, (len(records[i]), i, "W")))

print("second star:", max(energized_list))
print("Time: ", perf_counter() - start_time)
print()
print("Total time:", round(perf_counter() - total_start_time, 4), "sec")
print("=========================================")
