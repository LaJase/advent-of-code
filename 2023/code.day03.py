#! /usr/bin/python3.10

tab = []
num = ""
number = ""
x, y, result = 0, 0, 0
isAlreadyFound = False
secondResultDict = {}


def getPosForStar(x, y, number):
    # recherche ligne au dessus
    Ystart = 0 if y - 1 < 0 else y - 1
    Ysize = len(number) + 2 if y - 1 >= 0 else len(number) + 1
    Yend = Ystart + Ysize
    Yendend = Yend if Yend <= len(tab[x]) else len(tab[x])

    pos = ""

    if x > 0:
        linebefore = tab[x - 1]
        subListBefore = linebefore[Ystart:Yendend]
        for itemIndex, item in enumerate(subListBefore):
            if item == '*':
                pos = str(x-1) + " " + str(Ystart + itemIndex)

    if x < len(tab) - 1:
        lineUnder = tab[x + 1]

        subListAfter = lineUnder[Ystart:Yendend]
        for itemIndex, item in enumerate(subListAfter):
            if item == '*':
                pos = str(x+1) + " " + str(Ystart + itemIndex)

    if y > 0:
        if tab[x][y-1] == '*':
            pos = str(x) + " " + str(y - 1)

    if Yend < len(tab[x]):
        if tab[x][Yend - 1] == '*':
            pos = str(x) + " " + str(Yend - 1)

    if len(pos) > 0:
        charac = tab[int(pos.split()[0])][int(pos.split()[1])]
        print("pos: [{}], char: {}".format(pos, charac))

    return pos


def isThereASpecialCharForMyNumber(x, y, number):
    # recherche ligne au dessus
    Ystart = 0 if y - 1 < 0 else y - 1
    Ysize = len(number) + 2 if y - 1 >= 0 else len(number) + 1
    Yend = Ystart + Ysize
    Yendend = Yend if Yend <= len(tab[x]) else len(tab[x])

    chars = []


    if x > 0:
        linebefore = tab[x - 1]
        subListBefore = linebefore[Ystart:Yendend]
        chars.extend(subListBefore)

    if x < len(tab) - 1:
        lineUnder = tab[x + 1]

        subListAfter = lineUnder[Ystart:Yendend]
        chars.extend(subListAfter)

    if y > 0:
        chars.append(tab[x][y-1])

    if Yend < len(tab[x]):
        chars.append(tab[x][Yend - 1])

    for el in chars:
        if not el.isdigit() and el != '.':
            return True

    return False


with open("../puzzles/input.day3.txt", 'r') as file:
    for line in file:
        tab.append([*line.strip()])

for lineIndex, line in enumerate(tab):
    for charIndex, char in enumerate(line):
        if char.isdigit():
            if not isAlreadyFound:
                x, y = lineIndex, charIndex

            isAlreadyFound = True
            number = number + char

        elif not char.isdigit() and isAlreadyFound:
            isValid = isThereASpecialCharForMyNumber(x, y, number)

            posList = getPosForStar(x, y, number)
            if posList != "":
                if posList in secondResultDict:
                    secondResultDict[posList].append(number)
                else:
                    secondResultDict[posList] = [number]

            if isValid:
                result += int(number)

            pos, number, isAlreadyFound = (), "", False

secondResult = 0
for key, value in secondResultDict.items():
    if len(value) == 2:
        secondResult = secondResult + int(value[0])*int(value[1])

print()
print("First start result: ", result)
print("second start result: ", secondResult)
print()
