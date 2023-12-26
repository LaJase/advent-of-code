#! /usr/bin/python3.10

import sys

print()
print("==============================================")
with open(sys.argv[1], "r") as file:
    file_content = file.read().strip()
    init_sequence = file_content.split(",")


def compute_hash(letter):
    hash_value = 0
    for char in letter:
        hash_value = ((hash_value + ord(char)) * 17) % 256
    return hash_value


res1 = 0
for seq in init_sequence:
    res1 += compute_hash(seq)

print("first star : ", res1)

boxes = [[] for _ in range(256)]
for seq in init_sequence:
    if seq[-1] == "-":
        name = seq[:-1]
        hash = compute_hash(name)
        boxes[hash] = [el for el in boxes[hash] if el[0] != name]
    elif seq[-2] == "=":
        name = seq[:-2]
        hash = compute_hash(name)
        value = int(seq[-1])
        if name in [el[0] for el in boxes[hash]]:
            temp = []
            for el in boxes[hash]:
                if el[0] == name:
                    temp.append((el[0], value))
                else:
                    temp.append(el)

            boxes[hash] = temp
        else:
            boxes[hash].append((name, value))

res2 = 0
for i, box in enumerate(boxes):
    for j, el in enumerate(box):
        res2 += (i + 1) * (j + 1) * el[1]

print("second star: ", res2)
