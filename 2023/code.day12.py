#! /usr/bin/python3.10

import sys

print()
print('==================================')

keys_found = {}


def calc_possibilite(chaine, repartition, index, block_index, current_length):
    key = (index, block_index, current_length)
    if key in keys_found:
        # print('stop  ', chaine, repartition, index, block_index, current_length)
        return keys_found[key]
    if index == len(chaine):
        # Ca ou on termine par un point
        if block_index == len(repartition) and current_length == 0:
            # print('first  ', chaine, repartition, index, block_index, current_length)
            return 1
        # Cas ou on termine par un # car pas encore le temps d'incrementer
        elif block_index == len(repartition)-1 and repartition[block_index] == current_length:
            # print('second ', chaine, repartition, index, block_index, current_length)
            return 1
        else:
            return 0

    ans = 0
    for c in ['.', '#']:
        if chaine[index] == c or chaine[index] == '?':
            trans = chaine
            if chaine[index] == '?':
                trans = chaine.replace('?', c, 1)
            # cas d'une succession de '.'
            if c == '.' and current_length == 0:
                ans += calc_possibilite(trans, repartition, index+1, block_index, 0)
            # on viet de terminer un bloc
            elif c == '.' and current_length > 0 and block_index < len(repartition) and repartition[block_index] == current_length:
                ans += calc_possibilite(trans, repartition, index+1, block_index+1, 0)
            # On est dans un bloc
            elif c == '#':
                ans += calc_possibilite(trans, repartition, index+1, block_index, current_length+1)
    keys_found[key] = ans
    return ans


with open(sys.argv[1], 'r') as file:
    file_content = file.read().strip()
    lines = file_content.split('\n')

for part2 in [False, True]:
    res = 0
    for line in lines:
        keys_found.clear()
        chaine, repart = line.split()
        if part2:
            chaine = '?'.join([chaine, chaine, chaine, chaine, chaine])
            repart = ','.join([repart, repart, repart, repart, repart])
        repart = [int(c) for c in repart.split(',')]
        res += calc_possibilite(chaine, repart, 0, 0, 0)

    if part2:
        print('second star: ', res)
    else:
        print('first star: ', res)

print('==================================')
