#! /usr/bin/python3.10

def sequence_process(seq, prt2):
    seq_list = [int(el) for el in seq.split()]
    result = [seq_list[0 if prt2 else len(seq_list)-1]]

    inter = []
    while not all(el == 0 for el in seq_list):
        inter = []

        for it in range(1, len(seq_list)):
            inter.append(seq_list[it] - seq_list[it-1])

        result.append(inter[0 if prt2 else len(inter)-1])
        seq_list = inter

    res = 0
    result.reverse()
    if prt2:
        for i in range(1, len(result)):
            res = result[i] - res
    else:
        res = sum(result)

    return res


with open("input-1.txt", 'r') as file:
    inputs = [line.strip() for line in file.readlines()]

    intervals_1 = []
    intervals_2 = []
    for sequence in inputs:
        line_result_prt1 = sequence_process(sequence, False)
        intervals_1.append(line_result_prt1)
        line_result_prt2 = sequence_process(sequence, True)
        intervals_2.append(line_result_prt2)

    print("star 1: ", sum(intervals_1))
    print("star 2: ", sum(intervals_2))
