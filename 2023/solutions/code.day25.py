#! /usr/bin/python3.10

import sys
import networkx as nx

from time import perf_counter
from collections import defaultdict

total_start_time = perf_counter()
print()
print("=========================================")


def parse_input(input):
    parsed = defaultdict(set)
    for line in input:
        node, links = line.split(":")
        for el in links.split():
            parsed[node].add(el)
            parsed[el].add(node)

    return parsed


def solve_first(input):
    wirings = defaultdict(set)

    for line in input:
        node, links = line.split(":")
        for el in links.split():
            wirings[node].add(el)
            wirings[el].add(node)

    nxGraph = nx.DiGraph()
    for key, values in wirings.items():
        for val in values:
            nxGraph.add_edge(key, val, capacity=1.0)
            nxGraph.add_edge(val, key, capacity=1.0)

    x = list(wirings.keys())[0]
    for y in wirings.keys():
        if x != y:
            cut_value, partition = nx.minimum_cut(nxGraph, x, y)
            if cut_value == 3:
                return len(partition[0]) * len(partition[1])


with open(sys.argv[1], "r") as file:
    file_content = file.read().strip()
    lines = file_content.split("\n")


start_time = perf_counter()
print("first star :", solve_first(lines))
print("Time:", round(perf_counter() - start_time, 4), "sec")

print()
print("Total time:", round(perf_counter() - total_start_time, 4), "sec")
print("=========================================")
