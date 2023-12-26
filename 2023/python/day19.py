#! /usr/bin/python3.10

import sys
import parse
import math
import re
import collections

from time import perf_counter

total_start_time = perf_counter()
print()
print("=========================================")

PART_PATTERN = parse.compile("{cat}={value:d}")
WORKFLOW_PATTERN = parse.compile("{cat}{op}{value:d}:{target}")


def parse_workflow(workflows):
    result_dict = {}
    for work in workflows.split("\n"):
        match = re.match(r"(\w+)\{([^}]+)\}", work)

        if match:
            prefix = match.group(1)
            key_value_pairs = match.group(2).split(",")

            result_dict[prefix] = {}

            for ind, pair in enumerate(key_value_pairs):
                if ind == len(key_value_pairs) - 1:
                    result_dict[prefix]["dest"] = pair
                else:
                    key, value = pair.split(":")
                    result_dict[prefix][key] = value

    return result_dict


def parse_ratings(ratings):
    result_list = []
    for rat in ratings.split("\n"):
        # Utilisation d'une expression régulière pour extraire les paires clé-valeur
        matches = re.findall(r"(\w+)=(\d+)", rat)

        result_dict = {key: int(value) for key, value in matches}
        result_list.append(result_dict)

    return result_list


def solve_part1(workflow, ratings):
    ans = 0
    for rating in ratings:
        current_work = "in"
        while current_work not in ["A", "R"]:
            rules = workflow[current_work]
            for key, value in rules.items():
                if key == "dest":
                    continue

                letter, condition, val = key[0], key[1], int(key[2:])

                isValid = False
                if condition == ">":
                    isValid = True if rating[letter] > val else False
                elif condition == "<":
                    isValid = True if rating[letter] < val else False

                if isValid:
                    current_work = value
                    break

                current_work = rules["dest"]

            if current_work == "A":
                for _, value in rating.items():
                    ans += value

    return ans


def parse_workflow_prt2(text):
    name, descriptions = text[:-1].split("{")
    workflows = []
    for description in descriptions.split(","):
        if match := WORKFLOW_PATTERN.parse(description):
            result = match.named
        else:
            result = {"cat": "", "op": "", "value": 0, "target": description}
        workflows.append(
            (result["cat"], result["op"], result["value"], result["target"])
        )
    return (name, workflows)


def process_intervals(intervals, workflow):
    for category, op, value, target in workflow:
        if not op:
            yield target, intervals
            continue

        low, high = intervals[category]
        if op == "<" and low < value:
            yield target, intervals | {category: (low, value)}
            intervals |= {category: (value, high)}
        if op == ">" and high > value:
            yield target, intervals | {category: (value + 1, high)}
            intervals |= {category: (low, value + 1)}


def solve_part2(data):
    accepted = []
    to_process = collections.deque(
        [("in", {"x": (1, 4001), "m": (1, 4001), "a": (1, 4001), "s": (1, 4001)})]
    )

    while to_process:
        workflow, intervals = to_process.popleft()
        for new_workflow, new_intervals in process_intervals(intervals, data[workflow]):
            if new_workflow == "A":
                accepted.append(new_intervals)
            elif new_workflow != "R":
                to_process.append((new_workflow, new_intervals))

    return sum(
        math.prod(high - low for low, high in interval.values())
        for interval in accepted
    )


with open(sys.argv[1], "r") as file:
    file_content = file.read().strip()
    workflows, ratings = file_content.split("\n\n")
    workflows_dict = parse_workflow(workflows)
    ratings_dict = parse_ratings(ratings)
    workflow_parsed_prt2 = dict(
        [parse_workflow_prt2(line) for line in workflows.split("\n")]
    )


start_time = perf_counter()
print("first star :", solve_part1(workflows_dict, ratings_dict))
print("Time:", round(perf_counter() - start_time, 4), "sec")
print()

start_time = perf_counter()
print("second star:", solve_part2(workflow_parsed_prt2))
print("Time:", round(perf_counter() - start_time, 4), "sec")
print()
print("Total time:", round(perf_counter() - total_start_time, 4), "sec")
print("=========================================")
