#! /usr/bin/python3.10

import sys

res = []
asso = [(2, 'twone'), (1, 'one'), (9, 'nine'), (8, 'eight'),  (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'),
        (6, 'six'), (7, 'seven')]

with open(sys.argv[1], 'r') as file:
    file_content = file.read().strip()
    lines = file_content.split('\n')

for prt2 in [False, True]:
    num = 0
    res.clear()
    for line in lines:
        if prt2:
            for digit, el in asso:
                line = line.replace(el, str(digit))

        first = next(c for c in line if c.isdigit())
        last = next(c for c in reversed(line) if c.isdigit())
        num = int(str(first) + str(last))
        res.append(num)

    if prt2:
        print('second star: ', sum(res))
    else:
        print('first star: ', sum(res))
