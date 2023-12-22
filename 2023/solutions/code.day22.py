#! /usr/bin/python3.10

import sys
import re
from time import perf_counter
from parse import parse
from collections import defaultdict

total_start_time = perf_counter()
print()
print("=========================================")


def parse_input(input):
    parsed = set()
    for index, line in enumerate(input):
        xs, ys, zs, xe, ye, ze = parse("{:d},{:d},{:d}~{:d},{:d},{:d}", line).fixed
        parsed.add(tuple([int(xs), int(ys), int(zs), int(xe), int(ye), int(ze), index]))

    return sorted(parsed, key=lambda z: z[2])


def down(brick):
    return (
        brick[0],
        brick[1],
        brick[2] - 1,
        brick[3],
        brick[4],
        brick[5] - 1,
        brick[6],
    )


def positions(brick):
    for x in range(brick[0], brick[3] + 1):
        for y in range(brick[1], brick[4] + 1):
            for z in range(brick[2], brick[5] + 1):
                yield (x, y, z)


def get_bricks_after_fall(bricks):
    occupied = {}
    fallen = []

    for brick in bricks:
        # Tant que l'on peut encore descendre. Attention au sol !!
        while brick[2] > 0 and all(
            pos not in occupied for pos in positions(down(brick))
        ):
            brick = down(brick)

        for pos in positions(brick):
            occupied[pos] = brick
        fallen.append(brick)

    return fallen, occupied


def get_parents(bricks, occupied):
    above = defaultdict(set)
    below = defaultdict(set)
    for brick in bricks:
        inthisbrick = set(positions(brick))
        for pos in positions(down(brick)):
            if pos in occupied and pos not in inthisbrick:
                above[occupied[pos]].add(brick)
                below[brick].add(occupied[pos])

    return above, below


def solve_part1(fallen):
    res = 0
    for brick in fallen:
        isGood = True
        for parent in above[brick]:
            if len(below[parent]) == 1:
                isGood = False

        if isGood:
            res += 1

    return res


with open(sys.argv[1], "r") as file:
    file_content = file.read().strip()
    lines = file_content.split("\n")

start_time = perf_counter()

fallen, occupied = get_bricks_after_fall(parse_input(lines))
above, below = get_parents(fallen, occupied)

print("first star :", solve_part1(fallen))
print("Time:", round(perf_counter() - start_time, 4), "sec")
print()

start_time = perf_counter()
print("second star:")
print("Time:", round(perf_counter() - start_time, 4), "sec")
print()
print("Total time:", round(perf_counter() - total_start_time, 4), "sec")
print("=========================================")
