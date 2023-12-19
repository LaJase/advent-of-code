#! /usr/bin/python3.10

import sys
from time import perf_counter

total_start_time = perf_counter()
print()
print("=========================================")
with open(sys.argv[1], "r") as file:
    file_content = file.read().strip()
    lines = file_content.split("\n")

sum_elf = 0
res = []
for line in lines:
    if len(line) == 0:
        res.append(sum_elf)
        sum_elf = 0
        continue

    sum_elf += int(line)

start_time = perf_counter()
print("first star: ", max(res))
print("Time:", round(perf_counter() - start_time, 4), "sec")
print()

start_time = perf_counter()
res2 = []
for i in range(3):
    res2.append(max(res))
    res.remove(max(res))

print("second star: ", sum(res2))
print("Time:", round(perf_counter() - start_time, 4), "sec")
print()
print("Total time:", round(perf_counter() - total_start_time, 4), "sec")
print("=========================================")
