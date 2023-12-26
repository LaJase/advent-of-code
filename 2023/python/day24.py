#! /usr/bin/python3.10

import sys

from time import perf_counter
from parse import parse
from z3 import Int, Solver

total_start_time = perf_counter()
print()
print("=========================================")


def parse_input(input):
    parsed = set()
    for line in input:
        px, py, pz, vx, vy, vz = parse(
            "{:d}, {:d}, {:d} @ {:d}, {:d}, {:d}", line
        ).fixed
        parsed.add((int(px), int(py), int(pz), int(vx), int(vy), int(vz)))

    return parsed


PLAN = (200000000000000, 400000000000000)
# PLAN = (7, 27)


def intersection(hailA_pos, hailA_speed, hailB_pos, hailB_speed):
    rxs = hailA_speed[0] * hailB_speed[1] - hailA_speed[1] * hailB_speed[0]
    if rxs == 0:
        return False

    diff_pos = [i - j for i, j in zip(hailB_pos, hailA_pos)]
    t = (diff_pos[0] * hailB_speed[1] - diff_pos[1] * hailB_speed[0]) / rxs
    u = (diff_pos[0] * hailA_speed[1] - diff_pos[1] * hailA_speed[0]) / rxs

    if t < 0 or u < 0:
        return False

    intersection = [pi + t * ri for pi, ri in zip(hailA_pos, hailA_speed)]

    if PLAN[0] <= intersection[0] <= PLAN[1] and PLAN[0] <= intersection[1] <= PLAN[1]:
        return True

    return False


def solve_first(hails):
    ans = 0
    while hails:
        hail = hails.pop()
        pos_hail, vit_hail = (hail[0], hail[1]), (hail[3], hail[4])
        for hail_comp in hails:
            pos_hail_comp, vit_hail_comp = (
                (hail_comp[0], hail_comp[1]),
                (hail_comp[3], hail_comp[4]),
            )
            xinter = intersection(pos_hail, vit_hail, pos_hail_comp, vit_hail_comp)
            if xinter:
                ans += 1
    return ans


def solve_second(hails):
    x, y, z, vx, vy, vz = Int("x"), Int("y"), Int("z"), Int("vx"), Int("vy"), Int("vz")
    var = [Int(f"T{i}") for i in range(3)]
    z3solver = Solver()

    for i in range(3):
        hail = hails.pop()
        z3solver.add(x + var[i] * vx - hail[0] - var[i] * hail[3] == 0)
        z3solver.add(y + var[i] * vy - hail[1] - var[i] * hail[4] == 0)
        z3solver.add(z + var[i] * vz - hail[2] - var[i] * hail[5] == 0)

    # solve all the equations
    z3solver.check()

    # Get all the values found
    values = z3solver.model()

    return values.eval(x + y + z)


with open(sys.argv[1], "r") as file:
    file_content = file.read().strip()
    lines = file_content.split("\n")


start_time = perf_counter()
print("first star :", solve_first(parse_input(lines)))
print("Time:", round(perf_counter() - start_time, 4), "sec")
print()

start_time = perf_counter()
print("second star:", solve_second(parse_input(lines)))
print("Time:", round(perf_counter() - start_time, 4), "sec")
print()
print("Total time:", round(perf_counter() - total_start_time, 4), "sec")
print("=========================================")
