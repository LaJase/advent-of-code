#! /usr/bin/python3.10

result = 0


with open("./input2.txt", 'r') as file:
    for line in file:
        print(line.strip())
        isValidGame = True
        ref = {'blue': 1, 'green': 1, 'red': 1}

        for elem in line.strip().split(":")[1].split(";"):
            dico = {}
            for item in elem.strip().split(","):
                pair = item.strip().split()
                dico[pair[1]] = int(pair[0])

            for color, val in dico.items():
                ref[color] = max(val, ref[color])

        result = result + ref['blue']*ref['green']*ref['red']
        print(ref)
        print()


print(result)
print()
