#! /usr/bin/python3.10

game = 1
result = 0

ref = {'blue': 14, 'green': 13, 'red': 12}

with open("./input1.txt", 'r') as file:
    for line in file:
        print(line.strip())
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

print(result)
