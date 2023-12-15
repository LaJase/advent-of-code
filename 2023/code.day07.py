#! /usr/bin/python3.10

import sys
from collections import Counter

print()
print("==========================================")
with open(sys.argv[1], "r") as file:
    file_content = file.read().strip()
    lines = file_content.split("\n")


def strength(hand, part2):
    hand = hand.replace('T', chr(ord('9')+1))
    hand = hand.replace('J', chr(ord('2')-1) if part2 else chr(ord('9')+2))
    hand = hand.replace('Q', chr(ord('9')+3))
    hand = hand.replace('K', chr(ord('9')+4))
    hand = hand.replace('A', chr(ord('9')+5))

    counter = Counter(hand)
    print(counter, sorted(counter.values()))
    if part2:
        target = list(counter.keys())[0]
        for k in counter:
            if k != '1':
                if counter[k] > counter[target] or target == '1':
                    target = k
        assert target != '1' or list(counter.keys()) == ['1']
        if '1' in counter and target != '1':
            counter[target] += counter['1']
            del counter['1']
        assert '1' not in counter or list(counter.keys()) == ['1'], f'{counter} {hand}'

    if sorted(counter.values()) == [5]:
        return (10, hand)
    elif sorted(counter.values()) == [1, 4]:
        return (9, hand)
    elif sorted(counter.values()) == [2, 3]:
        return (8, hand)
    elif sorted(counter.values()) == [1, 1, 3]:
        return (7, hand)
    elif sorted(counter.values()) == [1, 2, 2]:
        return (6, hand)
    elif sorted(counter.values()) == [1, 1, 1, 2]:
        return (5, hand)
    elif sorted(counter.values()) == [1, 1, 1, 1, 1]:
        return (4, hand)
    else:
        assert False, f'{counter} {hand} {sorted(counter.values())}'


for part2 in [False, True]:
    sorted_list = []
    for line in lines:
        hand, bid = line.split()
        sorted_list.append((hand, bid))
    sorted_list = sorted(sorted_list, key=lambda hb: strength(hb[0], part2))
    ans = 0
    for i, (h, b) in enumerate(sorted_list):
        print(i, h, b)
        ans += (i+1)*int(b)
    print(ans)
