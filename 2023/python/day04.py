#! /usr/bin/python3.10


def firstStar():
    myNumbers = []
    winning = []
    result = 0
    with open("../puzzles/input.day4.txt", 'r') as file:
        for line in file:
            splitted = line.strip().split(": ")[1].split(" | ")
            myNumbers = splitted[1].strip()
            winning = splitted[0].strip()
            inter = list(set(winning.split()) & set(myNumbers.split()))
            interLenght = len(inter)

            if interLenght > 0:
                result += 2 ** (len(inter) - 1)
                print(inter)

    print("result first star: ", result)
    print()


def secondStar():
    myNumbers = []
    winning = []
    matching = []
    with open("./input-2.txt", 'r') as file:
        lines = file.readlines()

    splitted = [line.strip().split(": ")[1].split(" | ") for line in lines]
    myNumbers = [el[1].strip() for el in splitted]
    winning = [el[0].strip() for el in splitted]
    for win, num in zip(winning, myNumbers):
        inter = list(set(win.split()) & set(num.split()))
        matching.append(len(inter))
    print("matchs: ", matching)

    copies = [1] * len(matching)
    for itemIndex, item in enumerate(matching):
        for i in range(itemIndex+1, itemIndex+1 + item):
            copies[i] += 1 * copies[itemIndex]
    print("copies: ", copies)
    print("result: ", sum(copies))


firstStar()
print()
secondStar()
print()
