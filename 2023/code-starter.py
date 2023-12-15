#! /usr/bin/python3.10

import sys

with open(sys.argv[1], 'r') as file:
    file_content = file.read().strip()
    lines = file_content.split('\n')
    records = [[c for c in row] for row in lines]
