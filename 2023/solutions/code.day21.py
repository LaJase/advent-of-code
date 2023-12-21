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
        current = set()
        while plots:
            x, y = plots.pop()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                newX = x + dx
                newY = y + dy
                if (newX % COL_LENGTH, newY % LINE_LENGTH) not in tiles_pos:
                    current.add((newX, newY))

        plots = set(current)

    return len(plots)


def solve_second(start, tiles_pos):
    factors = [0, 0, 0]
    nextfactor = 0
    goalsteps = 26501365
    plots = [start]

    for count in range(1, 1000):
        current = set()
        while plots:
            x, y = plots.pop()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                newX = x + dx
                newY = y + dy
                if (newX % COL_LENGTH, newY % LINE_LENGTH) not in tiles_pos:
                    current.add((newX, newY))

        plots = set(current)
        if count % COL_LENGTH == goalsteps % COL_LENGTH:
            factors[nextfactor] = len(plots)
            nextfactor += 1
            if nextfactor == 3:
                delta0, delta1, delta2 = (
                    factors[0],
                    factors[1] - factors[0],
                    factors[2] - 2 * factors[1] + factors[0],
                )
                return (
                    delta0
                    + delta1 * (goalsteps // COL_LENGTH)
                    + delta2
                    * ((goalsteps // COL_LENGTH) * ((goalsteps // COL_LENGTH) - 1) // 2)
                )


with open(sys.argv[1], "r") as file:
    file_content = file.read().strip()
    lines = file_content.split("\n")
    records = [[c for c in row] for row in lines]

LINE_LENGTH = len(records[0])
COL_LENGTH = len(records)


start_time = perf_counter()
start, tiles_pos = parse_input(records)
print("first star :", solve_first(start, tiles_pos))
print("Time:", round(perf_counter() - start_time, 4), "sec")
print()


start_time = perf_counter()
print("second star:", solve_second(start, tiles_pos))
print("Time:", round(perf_counter() - start_time, 4), "sec")
print()
print("Total time:", round(perf_counter() - total_start_time, 4), "sec")
print("=========================================")
