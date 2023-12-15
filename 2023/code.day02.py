#! /usr/bin/python3.10

import sys

game = 1
result = 0

ref = {"blue": 14, "green": 13, "red": 12}

print()
print("==========================================")
with open(sys.argv[1], "r") as file:
    file_content = file.read().strip()
    lines = file_content.split("\n")

for line in lines:
    isValidGame = True

    for elem in line.strip().split(":")[1].split(";"):
        dico = {}
        for item in elem.strip().split(","):
            pair = item.strip().split()
            dico[pair[1]] = int(pair[0])

        for color, val in dico.items():
            if val > ref[color]:
                isValidGame = False

    if isValidGame:
        result += game

    game += 1

print("first star: ", result)

result = 0
for line in lines:
    isValidGame = True
    ref = {"blue": 1, "green": 1, "red": 1}

    for elem in line.strip().split(":")[1].split(";"):
        dico = {}
        for item in elem.strip().split(","):
            pair = item.strip().split()
            dico[pair[1]] = int(pair[0])

        for color, val in dico.items():
            ref[color] = max(val, ref[color])

    result = result + ref["blue"] * ref["green"] * ref["red"]


print("second star: ", result)
