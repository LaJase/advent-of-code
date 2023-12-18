#! /usr/bin/python3.10

import sys

print("=======================================")
with open(sys.argv[1], "r") as file:
    file_content = file.read().strip()
    grids = file_content.split("\n\n")

for prt2 in [False, True]:
    ans = 0
    smudge = 0
    for grid in grids:
        tab = [[c for c in line] for line in grid.split("\n")]
        tab_col_size = len(tab)
        tab_line_size = len(tab[0])

        smudge = 0
        for row_index in range(tab_line_size - 1):
            smudge = 0
            for row_index_sec in range(row_index + 1):
                left_match = row_index - row_index_sec
                right_match = row_index + row_index_sec + 1

                if 0 <= left_match < right_match < tab_line_size:
                    for line in range(tab_col_size):
                        if tab[line][left_match] != tab[line][right_match]:
                            smudge += 1
            if prt2 and smudge == 1:
                ans += row_index + 1
            elif not prt2 and smudge == 0:
                ans += row_index + 1

        smudge = 0
        for col_index in range(tab_col_size - 1):
            smudge = 0
            for line_index_sec in range(col_index + 1):
                left_match = col_index - line_index_sec
                right_match = col_index + line_index_sec + 1

                if 0 <= left_match < right_match < tab_col_size:
                    for col in range(tab_line_size):
                        if tab[left_match][col] != tab[right_match][col]:
                            smudge += 1

            if prt2 and smudge == 1:
                ans += (col_index + 1) * 100
            elif not prt2 and smudge == 0:
                ans += (col_index + 1) * 100

    if prt2:
        print("second star: ", ans)
    else:
        print("first star: ", ans)
