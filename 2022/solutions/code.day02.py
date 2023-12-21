#! /usr/bin/python3.10

import sys
from time import perf_counter

total_start_time = perf_counter()
print()
print("=========================================")
with open(sys.argv[1], "r") as file:
    file_content = file.read().strip()
    lines = file_content.split("\n")


def solve_first():
    rules = {
        "X": {"p": 1, "w": "C", "o": "A"},
        "Y": {"p": 2, "w": "A", "o": "B"},
        "Z": {"p": 3, "w": "B", "o": "C"},
    }

    res = 0
    for line in lines:
        him, me = line.split()
        res += rules[me]["p"]
        if him == rules[me]["o"]:
            res += 3
        if him == rules[me]["w"]:
            res += 6

    return res


def solve_second():
    assoc = {
        "Y": {"A": 1, "B": 2, "C": 3, "points": 3},
        "Z": {"A": 2, "B": 3, "C": 1, "points": 6},
        "X": {"A": 3, "B": 1, "C": 2, "points": 0},
    }

    res = 0
    for line in lines:
        him, result = line.split()
        res += assoc[result]["points"]
        res += assoc[result][him]

    return res


start_time = perf_counter()
print("first star: ", solve_first())
print("Time:", round(perf_counter() - start_time, 4), "sec")
print()


print("second star: ", solve_second())
print("Time:", round(perf_counter() - start_time, 4), "sec")
print()
print("Total time:", round(perf_counter() - total_start_time, 4), "sec")
print("=========================================")
