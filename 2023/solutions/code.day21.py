#! /usr/bin/python3.10

import sys

from time import perf_counter

total_start_time = perf_counter()
print()
print("=========================================")


def parse_input(input):
    tiles_pos = []
    start = (0, 0)
    for x, line in enumerate(input):
        for y, col in enumerate(line):
            if col == "#":
                tiles_pos.append((x, y))
            if col == "S":
                start = (x, y)

    return start, set(tiles_pos)


def solve_first(start, tiles_pos):
    plots = [start]
    for _ in range(64):
        current = []
        while plots:
            x, y = plots.pop()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                newX = x + dx
                newY = y + dy
                if (
                    (newX, newY) not in current
                    and (newX, newY) not in tiles_pos
                    and 0 <= newX < line_length
                    and 0 <= newY < col_length
                ):
                    current.append((newX, newY))

        plots = set(current)

    print(len(plots))


with open(sys.argv[1], "r") as file:
    file_content = file.read().strip()
    lines = file_content.split("\n")
    records = [[c for c in row] for row in lines]

line_length = len(records[0])
col_length = len(records)


start_time = perf_counter()
start, tiles_pos = parse_input(records)
print("first star :", solve_first(start, tiles_pos))
print("Time:", round(perf_counter() - start_time, 4), "sec")
print()

start_time = perf_counter()
print("second star:")
print("Time:", round(perf_counter() - start_time, 4), "sec")
print()
print("Total time:", round(perf_counter() - total_start_time, 4), "sec")
print("=========================================")
