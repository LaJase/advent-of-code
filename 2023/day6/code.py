#! /usr/bin/python3.10

def firstStar():
    with open("./input-1.txt", 'r') as file:
        times = file.readline().split(":")[1].strip().split()
        distances = file.readline().split(":")[1].strip().split()

    result = 1

    for time, distance in zip(times, distances):
        ways = 0
        for it in range(1, int(time) + 1):
            if (int(time) - it) * it > int(distance):
                ways += 1
                print("valid for: ", it)

        print(ways)
        result *= ways

    print(result)


def secondStar():
    with open("./input-2.txt", 'r') as file:
        times = file.readline().split(":")[1].strip().split()
        distances = file.readline().split(":")[1].strip().split()

    result = 1

    for time, distance in zip(times, distances):
        ways = 0
        for it in range(1, int(time) + 1):
            if (int(time) - it) * it > int(distance):
                ways += 1

        print(ways)
        result *= ways

    print(result)


# firstStar()
print()
secondStar()
print()
