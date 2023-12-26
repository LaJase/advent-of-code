#! /usr/bin/python3.10

import sys

from math import gcd
from time import perf_counter
from queue import Queue


FLIP_FLOP = "ff"
ENTRY = "entry"
CONJUNCTION = "conj"
OUTPUTS = "outputs"
INPUTS = "inputs"
TYPE = "type"
STATE = "state"
LOW = "low"
HIGH = "high"


def parse_input(input):
    lines = input.split("\n")
    node_dict = {}
    for line in lines:
        node, outputs = line.split(" -> ")
        node = node.strip()
        node_type = ENTRY
        if node[0] == "%":
            node_type = FLIP_FLOP
            node = node[1:]
        elif node[0] == "&":
            node_type = CONJUNCTION
            node = node[1:]

        output_list = outputs.split(",")
        output_list = [out.strip() for out in output_list]

        # Creation du dictionnaire
        if node not in node_dict:
            node_dict[node] = {}

        node_dict[node][OUTPUTS] = output_list
        node_dict[node][TYPE] = node_type
        node_dict[node][STATE] = False

        for output in output_list:
            if output not in node_dict:
                node_dict[output] = {INPUTS: {}, STATE: False}

            if INPUTS not in node_dict[output]:
                node_dict[output][INPUTS] = {}

            node_dict[output][INPUTS][node] = False

    return node_dict


def find_rx_input(node_dict):
    # rx has on parent which is a conj
    parent_rx = ""
    nodes = {}
    for key in node_dict["rx"][INPUTS].keys():
        parent_rx = key

    for key in node_dict[parent_rx][INPUTS].keys():
        nodes[key] = 0

    return nodes


def lcm(xs):
    ans = 1
    for _, x in xs.items():
        ans = (x * ans) // gcd(x, ans)
    return ans


def solve_first(node_dict):
    fifo = Queue()

    high_push = 0
    low_push = 0
    signal_out = LOW

    for _ in range(1000):
        low_push += 1
        fifo.put(("broadcaster", LOW, ""))
        while not fifo.empty():
            node, signal, prev = fifo.get()
            node_info = node_dict[node]
            # print(node, signal, node_info)

            doSend = False
            if node_info[TYPE] == ENTRY:
                signal_out = LOW
                doSend = True

            elif node_info[TYPE] == FLIP_FLOP:
                if signal == LOW:
                    node_dict[node][STATE] = not node_dict[node][STATE]
                    signal_out = HIGH if node_dict[node][STATE] else LOW
                    doSend = True

            elif node_info[TYPE] == CONJUNCTION:
                if len(node_info[INPUTS]) == 1:
                    signal_out = HIGH if signal == LOW else LOW
                    doSend = True
                elif len(node_info[INPUTS]) > 1:
                    node_info[INPUTS][prev] = False if signal == LOW else True
                    signal_out = LOW
                    doSend = True
                    for _, isOn in node_info[INPUTS].items():
                        if not isOn:
                            signal_out = HIGH
                            break

            for out in node_dict[node][OUTPUTS]:
                if doSend:
                    # print("{} {} -> {}".format(node, signal_out, out))
                    if signal_out == HIGH:
                        high_push += 1
                    else:
                        low_push += 1

                    if OUTPUTS in node_dict[out]:
                        fifo.put((out, signal_out, node))

    return high_push * low_push


def solve_second(node_dict, parent_nodes):
    fifo = Queue()

    signal_out = LOW
    keepGoing = True
    cpt = 0

    while keepGoing:
        cpt += 1
        fifo.put(("broadcaster", LOW, ""))
        while not fifo.empty():
            node, signal, prev = fifo.get()
            node_info = node_dict[node]

            doSend = False
            if node_info[TYPE] == ENTRY:
                signal_out = LOW
                doSend = True

            elif node_info[TYPE] == FLIP_FLOP:
                if signal == LOW:
                    node_dict[node][STATE] = not node_dict[node][STATE]
                    signal_out = HIGH if node_dict[node][STATE] else LOW
                    doSend = True

            elif node_info[TYPE] == CONJUNCTION:
                if len(node_info[INPUTS]) == 1:
                    signal_out = HIGH if signal == LOW else LOW
                    doSend = True
                elif len(node_info[INPUTS]) > 1:
                    node_info[INPUTS][prev] = False if signal == LOW else True
                    signal_out = LOW
                    doSend = True
                    for _, isOn in node_info[INPUTS].items():
                        if not isOn:
                            signal_out = HIGH
                            break

            for out in node_dict[node][OUTPUTS]:
                if doSend:
                    if OUTPUTS in node_dict[out]:
                        if node in parent_nodes and signal_out == HIGH:
                            parent_nodes[node] = cpt

                        fifo.put((out, signal_out, node))

        keepGoing = not all([value > 0 for _, value in parent_nodes.items()])

    return lcm(parent_nodes)


if __name__ == "__main__":
    total_start_time = perf_counter()
    print()
    print("=========================================")
    with open(sys.argv[1], "r") as file:
        file_content = file.read().strip()

    start_time = perf_counter()
    print("first star :", solve_first(parse_input(file_content)))
    print("Time:", round(perf_counter() - start_time, 4), "sec")
    print()

    start_time = perf_counter()

    print(
        "second star:",
        solve_second(
            parse_input(file_content), find_rx_input(parse_input(file_content))
        ),
    )
    print("Time:", round(perf_counter() - start_time, 4), "sec")
    print()
    print("=========================================")
    print("Total time:", round(perf_counter() - total_start_time, 4), "sec")
