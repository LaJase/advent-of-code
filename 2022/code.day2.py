#! /usr/bin/python3.10

import sys

with open(sys.argv[1], 'r') as file:
    file_content = file.read().strip()
    lines = file_content.split('\n')

rules = {
    'X': {'p': 1, 'w': 'C', 'o': 'A'},
    'Y': {'p': 2, 'w': 'A', 'o': 'B'},
    'Z': {'p': 3, 'w': 'B', 'o': 'C'},
}

res = 0
for line in lines:
    print(line)
    him, me = line.split()
    res += rules[me]['p']
    if him == rules[me]['o']:
        res += 3
    if him == rules[me]['w']:
        res += 6
    print(res)

print(res)
