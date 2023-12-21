#! /usr/bin/python3.10

import sys

from time import perf_counter

total_start_time = perf_counter()
print()
print("=========================================")


def value_letter(letter):
    ans = 0
    value = ord(letter)
    if 97 <= value <= 122:
        ans = value - 96
    else:
        ans = value - 38

    return ans


def solve_first(input):
    ans = 0
    for line in input:
        first_half, second_half = line[: (len(line)) // 2], line[len(line) // 2 :]
        letter = set(set(first_half) & set(second_half)).pop()
        ans += value_letter(letter)

    return ans


def solve_second(input):
    inter = set()
    ans = 0
    for ind, line in enumerate(input):
        if len(inter) == 0:
            inter = set(line)
        else:
            inter = set(inter) & set(line) if inter != "" else line
        if (ind + 1) % 3 == 0:
            ans += value_letter(inter.pop())
            inter.clear()

            inter = set()

    return ans


with open(sys.argv[1], "r") as file:
    file_content = file.read().strip()
    lines = file_content.split("\n")


start_time = perf_counter()
print("first star :", solve_first(lines))
print("Time:", round(perf_counter() - start_time, 4), "sec")
print()

start_time = perf_counter()
print("second star:", solve_second(lines))
print("Time:", round(perf_counter() - start_time, 4), "sec")
print()
print("Total time:", round(perf_counter() - total_start_time, 4), "sec")
print("=========================================")
