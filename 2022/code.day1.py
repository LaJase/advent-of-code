#! /usr/bin/python3.10

import sys

with open(sys.argv[1], 'r') as file:
    file_content = file.read().strip()
    lines = file_content.split('\n')

sum_elf = 0
res = []
for line in lines:
    if len(line) == 0:
        res.append(sum_elf)
        sum_elf = 0
        continue

    sum_elf += int(line)

print('first star: ', max(res))

res2 = []
for i in range(3):
    res2.append(max(res))
    res.remove(max(res))

print('second star: ', sum(res2))
