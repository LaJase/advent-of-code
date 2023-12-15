#! /usr/bin/python3.10


import time


def firstStar():
    print("hello")


def secondStar():
    all_rules = []
    with open("./input-1.txt", 'r') as file:
        firstLine = file.readline().strip().split(":")[1].strip().split()
        paires = set((int(firstLine[i]), int(firstLine[i+1]) + int(firstLine[i]) - 1)
                     for i in range(0, len(firstLine) - 1, 2))
        # print(firstLine)
        print(paires)

        file.readline()

        maps = []
        for line in file:
            line = line.strip()

            if len(line) == 0:
                all_rules.append(maps)
                maps = []

            elif line[0].isdigit():
                conv_line = tuple(int(l) for l in line.split())
                maps.append(conv_line)

        print(all_rules)

    location = []
    # for element in paires:
    #     print("===============================================================")
    #     elements = [element]
    print()
    for rules in all_rules:
        new_paires = set()

        print("Paires available for new rule: ", paires)
        while len(paires) > 0:
            minPair, maxPair = paires.pop()
            print("Processing pair: ", minPair, maxPair)

            found = False
            for rule in rules:
                destination, source, rang = rule
                sourceSet = tuple([source, source + rang - 1])
                destinationSet = tuple([destination, destination + rang - 1])
                print("    Rule: {} -> {}".format(sourceSet, destinationSet))

                print("        pair change: ", minPair, maxPair, end=" -> after rule: ")

                minSource, maxSource = sourceSet
                minDest, maxDest = destinationSet

                if maxPair < minSource or minPair > maxSource:
                    new_paires.add(tuple([minPair, maxPair]))
                    print(minPair, maxPair)

                elif minPair >= minSource and maxPair <= maxSource:
                    newMin = minDest + (minPair - minSource)
                    newMax = maxDest - (maxSource - maxPair)
                    new_paires.add(tuple([newMin, newMax]))
                    if tuple([minPair, maxPair]) in new_paires:
                        new_paires.remove(tuple([minPair, maxPair]))
                    print(newMin, newMax)
                    found = True

                elif minPair >= minSource and maxPair > maxSource:
                    if tuple([minPair, maxPair]) in new_paires:
                        new_paires.remove(tuple([minPair, maxPair]))

                    newMin1 = minDest + (minPair - minSource)
                    newMax1 = maxDest
                    minPair = maxSource + 1
                    maxPair = maxPair
                    # newMin2 = maxSource + 1
                    # newMax2 = maxPair
                    new_paires.add(tuple([newMin1, newMax1]))
                    # new_paires.add(tuple([newMin2, newMax2]))
                    # print("(", newMin1, newMax1, ") (", newMin2, newMax2, ")")
                    print("(", newMin1, newMax1, ") (", minPair, maxPair, ")")

                elif minPair < minSource and maxPair <= maxSource:
                    if tuple([minPair, maxPair]) in new_paires:
                        new_paires.remove(tuple([minPair, maxPair]))

                    minPair = minPair
                    maxPair = minSource - 1
                    # newMin1 = minPair
                    # newMax1 = minSource - 1
                    newMin2 = minDest
                    newMax2 = maxDest - (maxSource - maxPair)
                    # new_paires.add(tuple([newMin1, newMax1]))
                    new_paires.add(tuple([newMin2, newMax2]))
                    print("(", minPair, maxPair, ") (", newMin2, newMax2, ")")

                else:
                    print("not handle case")

                print("        new paires: ", new_paires)
                time.sleep(1)
                if found:
                    break

            if not found:
                new_paires.add(tuple([minPair, maxPair]))

        paires = new_paires
        print()
        # for pair in paires:
    print(paires)
    for el in paires:
        x1, _ = el
        location.append(x1)

    print()
    print("list {} -> min = {}".format(location, min(location)))


# firstStar()
print()
print()
print("=====================================")
secondStar()
