#! /usr/bin/python3.10

import re
from math import gcd


def convertir_en_dictionnaire(chaine):
    result = {'L': {}, 'R': {}}
    starts = []

    for element in chaine:
        match = re.match(r'(\w+) = \((\w+), (\w+)\)', element)
        if match:
            left, right1, right2 = match.groups()
            result['L'][left] = right1
            result['R'][left] = right2

            if left.endswith('A'):
                starts.append(left)

    return result, starts


def searchStepForValue(input, dict, instr):
    step = 0
    while not input.endswith('Z'):
        inst_index = step % len(instr)
        input = dict[instr[inst_index]][input]
        step += 1

    return step


def lcm(xs):
    ans = 1
    for x in xs:
        ans = (x*ans)//gcd(x, ans)
    return ans


def firstStar():
    with open("input-1.txt", 'r') as file:
        instructions = list(file.readline().strip())
        file.readline()
        nodes_desc = [line.strip() for line in file.readlines()]

    node_dict, _ = convertir_en_dictionnaire(nodes_desc)
    result = searchStepForValue('AAA', node_dict, instructions)
    print(result)


def secondStar():
    with open("input-1.txt", 'r') as file:
        instructions = list(file.readline().strip())
        file.readline()
        nodes_desc = [line.strip() for line in file.readlines()]

    node_dict, nodes = convertir_en_dictionnaire(nodes_desc)

    nodes = set(nodes)
    for key, _ in node_dict.items():
        if key.endswith('A'):
            nodes.add(key)

    print(nodes)

    results = []
    for node in nodes:
        results.append(searchStepForValue(node, node_dict, instructions))

    print(lcm(results))


print()
firstStar()
secondStar()
