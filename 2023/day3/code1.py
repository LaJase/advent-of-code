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

    posReturn = []
    pos = ""

    # print(Ystart, Ysize, Yend, Yendend)

    if x > 0:
        linebefore = tab[x - 1]
        subListBefore = linebefore[Ystart:Yendend]
        for itemIndex, item in enumerate(subListBefore):
            if item == '*':
                pos = str(x-1) + " " + str(Ystart + itemIndex)
                # posReturn.append(pos)

    if x < len(tab) - 1:
        lineUnder = tab[x + 1]

        subListAfter = lineUnder[Ystart:Yendend]
        for itemIndex, item in enumerate(subListAfter):
            if item == '*':
                pos = str(x+1) + " " + str(Ystart + itemIndex)
                # posReturn.append(pos)

    if y > 0:
        # print("char before: ", tab[x][y-1])
        if tab[x][y-1] == '*':
            pos = str(x) + " " + str(y - 1)
            # posReturn.append(pos)

    if Yend < len(tab[x]):
        # print("char after: ", tab[x][Yend-1])
        if tab[x][Yend - 1] == '*':
            pos = str(x) + " " + str(Yend - 1)
            # posReturn.append(pos)

    if len(pos) > 0:
        # charac = tab[int(posReturn[0].split()[0])][int(posReturn[0].split()[1])]
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

    # print(Ystart, Ysize, Yend, Yendend)

    if x > 0:
        linebefore = tab[x - 1]
        subListBefore = linebefore[Ystart:Yendend]
        chars.extend(subListBefore)
        # print("line Before :", subListBefore)

    if x < len(tab) - 1:
        lineUnder = tab[x + 1]

        subListAfter = lineUnder[Ystart:Yendend]
        chars.extend(subListAfter)
        # print("line After :", subListAfter)

    if y > 0:
        # print("char before: ", tab[x][y-1])
        chars.append(tab[x][y-1])

    if Yend < len(tab[x]):
        # print("char after: ", tab[x][Yend-1])
        chars.append(tab[x][Yend - 1])

    for el in chars:
        if not el.isdigit() and el != '.':
            return True

    return False


with open("./input1.txt", 'r') as file:
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
            # print(x, y, number)

            # Appel de la fonction pour recherche char spec
            isValid = isThereASpecialCharForMyNumber(x, y, number)
            # print(number, isValid)

            posList = getPosForStar(x, y, number)
            if posList != "":
                if posList in secondResultDict:
                    # Si la clé existe, ajouter la valeur num à la liste existante
                    secondResultDict[posList].append(number)
                else:
                    # Si la clé n'existe pas, créer une nouvelle liste avec la valeur num
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
