# Advent of Code Solutions

This repository contains my solutions for Advent of Code challenges. Each folder corresponds to the respective year, and each subfolder represents a specific day of the challenge.

## Repository Organization

```text
./
├── 2022/
├── 2023/
│ ├── puzzles/
│ │ ├── input.day01.txt
│ │ ├── input.day02.txt
│ │ ├── input.day03.txt
│ │ └── ...
│ │
│ ├── code.day01.py
│ ├── code.day02.py
│ ├── code.day03.py
│ └── ...
│
└── ... (TBC)
```

## Running the Solutions

- For each day, there is a `solution.dayXX.py` file containing the code to solve the corresponding day's problem.
- The `./puzzles/input.dayXX.txt` files contain input data specific to the problem.

To run a particular solution, use the following command (make sure to have the corresponding language installed):

```bash
python 2023/dayXX/solution.py ./puzzles/input.day01.txt
```

Each solution should print two lines - the answer for star 1 and the answer for star 2.
