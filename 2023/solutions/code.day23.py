#! /usr/bin/python3.10

import sys

from time import perf_counter
from copy import deepcopy

sys.setrecursionlimit(3000)

total_start_time = perf_counter()
print()
print("=========================================")

SLOPES = ["<", ">", "^", "v"]


def parse_input(lines):
    records = [[c for c in row] for row in lines]
    start = (records[0].index("."), 0)
    end = (records[len(records) - 1].index("."), len(records) - 1)

    return records, start, end


PATH_LENGTH = set()


def show_grid(grid, pos):
    grid_print = deepcopy(grid)
    for x, y in pos:
        grid_print[y][x] = "O"

    for row in grid_print:
        print("".join(row))

    print()


def longest_path(grid, end, current, memory, dir):
    if current in memory:
        return

    memory.add(current)

    if current == end:
        memory.remove(end)
        PATH_LENGTH.add(len(memory))
        return

    x, y = current
    for dirindex, (dx, dy) in enumerate([(-1, 0), (1, 0), (0, -1), (0, 1)]):
        newX = x + dx
        newY = y + dy

        if not (0 <= newX < len(grid[0]) and 0 <= newY < len(grid)):
            continue

        if grid[y][x] in SLOPES:
            if dirindex != dir or SLOPES.index(grid[y][x]) != dirindex:
                continue

        if grid[newY][newX] != "#" or (grid[y][x] in SLOPES and dirindex != dir):
            longest_path(grid, end, (newX, newY), memory, dirindex)

    memory.remove(current)


def solve_first(grid, start, end):
    longest_path(grid, end, start, set(), 0)

    return max(PATH_LENGTH)


def solve_second():
    print("first")


with open(sys.argv[1], "r") as file:
    file_content = file.read().strip()
    lines = file_content.split("\n")
    grid, start, end = parse_input(lines)


start_time = perf_counter()
print("first star :", solve_first(grid, start, end))
print("Time:", round(perf_counter() - start_time, 4), "sec")
print()

start_time = perf_counter()
print("second star:")
print("Time:", round(perf_counter() - start_time, 4), "sec")
print()
print("Total time:", round(perf_counter() - total_start_time, 4), "sec")
print("=========================================")
