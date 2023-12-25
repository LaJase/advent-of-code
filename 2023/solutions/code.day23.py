#! /usr/bin/python3.10

import sys


from time import perf_counter

sys.setrecursionlimit(3000)

total_start_time = perf_counter()
print()
print("=========================================")

SLOPES = ["<", ">", "^", "v"]
PATH_LENGTH = set()


def parse_input(lines):
    records = [[c for c in row] for row in lines]
    start = (records[0].index("."), 0)
    end = (records[len(records) - 1].index("."), len(records) - 1)

    return records, start, end


def dfs_paths_search(grid, end, current, memory):
    """
    brute force DFS for the first part, not efficient enough for the second one
    """
    if current in memory:
        return

    if current == end:
        PATH_LENGTH.add(len(memory))
        return

    memory.add(current)

    x, y = current
    for dirindex, (dx, dy) in enumerate([(-1, 0), (1, 0), (0, -1), (0, 1)]):
        newX = x + dx
        newY = y + dy

        if not (0 <= newX < len(grid[0]) and 0 <= newY < len(grid)):
            continue

        if grid[newY][newX] in SLOPES and SLOPES.index(grid[newY][newX]) != dirindex:
            continue

        if grid[newY][newX] != "#":
            dfs_paths_search(grid, end, (newX, newY), memory)

    memory.remove(current)


def solve_first(grid, start, end):
    dfs_paths_search(grid, end, start, set())
    return max(PATH_LENGTH)


def get_graph(input):
    graph = {}
    for line_index, line in enumerate(input):
        for col_index, c in enumerate(line):
            if c in ".>v":
                for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                    newX = line_index + dx
                    newY = col_index + dy

                    if not (0 <= newX < len(input) and 0 <= newY < len(line)):
                        continue

                    if input[newX][newY] in ".>v":
                        graph.setdefault((line_index, col_index), set())
                        graph.setdefault((newX, newY), set())

                        graph[(line_index, col_index)].add((newX, newY, 1))
                        graph[(newX, newY)].add((line_index, col_index, 1))

    return graph


def clean_graph(graph):
    """
    The idea here is to remove all nodes with exactly 2 neighbors because this means there is no choice to go further
    """
    isProcessing = True
    while isProcessing:
        isProcessing = False
        for key, values in graph.items():
            if len(values) == 2:
                isProcessing = True
                xKey, yKey = key
                (xA, yA, weightA), (xB, yB, weightB) = values

                graph[(xA, yA)].remove((xKey, yKey, weightA))
                graph[(xA, yA)].add((xB, yB, weightA + weightB))

                graph[(xB, yB)].remove((xKey, yKey, weightB))
                graph[(xB, yB)].add((xA, yA, weightA + weightB))
                del graph[key]
                break
        else:
            break

    return graph


def dfs_graph(graph, end, current, memory, path_length):
    x, y, weight = current

    if (x, y) in memory:
        return

    if (x, y) == end:
        path_length.add(weight)
        return

    memory.add((x, y))

    for xchild, ychild, wchild in graph[(x, y)]:
        dfs_graph(graph, end, (xchild, ychild, wchild + weight), memory, path_length)

    memory.remove((x, y))


def solve_second(input):
    line_number = len(input)
    end = (line_number - 1, input[line_number - 1].index("."))

    raw_graph = get_graph(input)

    cleaned_graph = clean_graph(raw_graph)
    path_length = set()
    dfs_graph(cleaned_graph, end, (0, input[0].index("."), 0), set(), path_length)

    return max(path_length)


with open(sys.argv[1], "r") as file:
    file_content = file.read().strip()
    lines = file_content.split("\n")
    grid, start, end = parse_input(lines)


start_time = perf_counter()
print("first star :", solve_first(grid, start, end))
print("Time:", round(perf_counter() - start_time, 4), "sec")
print()

start_time = perf_counter()
print("second star:", solve_second(lines))
print("Time:", round(perf_counter() - start_time, 4), "sec")
print()
print("Total time:", round(perf_counter() - total_start_time, 4), "sec")
print("=========================================")
