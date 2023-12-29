# Advent of Code Solutions

This repository contains my solutions for Advent of Code challenges. Each folder corresponds to the respective year,
and each subfolder represents a specific day of the challenge.

## Repository Organization

```text
./
├── 2022/
├── 2023/
│ ├── puzzles/
│ │ ├── day01.txt
│ │ ├── day02.txt
│ │ ├── day03.txt
│ │ └── ...
│ │
│ ├── python/
│ │ ├── day01.py
│ │ ├── day02.py
│ │ ├── day03.py
│ │ └── ...
│ │
│ ├── go/
│ │ ├── days/
│ │ │ ├── day_01/
│ │ │ │ ├── dayXX_example.txt
│ │ │ │ ├── main.go
│ │ │ │ ├── main_test.go
│ │ │ │ └── ...
│ │ │ ├── day_02/
│ │ │ ├── day_03/
│ │ │ └── ...
│ │ ├── internal/
│ │ │ ├── executor.go
│ │ │ ├── loader.go
│ │ │ └── ...
│ │ ├── main.go
│ │ ├── go.mod
│ │ └── ...
└── ... (TBC)
```

## Running the Python Solutions

### How to run a solution

- For each day, there is a `dayXX.py` file containing the code to solve the corresponding day's problem.
- The `./puzzles/dayXX.txt` files contain input data specific to the problem.

To run a particular solution, use the following command (make sure to have the corresponding language installed):

```bash
python 2023/pyhton/dayXX/solution.py ./puzzles/dayXX.txt
```

Each solution should print two lines - the answer for star 1 and the answer for star 2.

### Init script

The init.sh script, available for certain years, utilizes a Python script template that I prefer, ensuring a quicker
setup. To execute it, use the following command:

```bash
# For Day 1; having it on 2 digits aids in sorting file names
bash init.sh 01
```

This script is designed to streamline the preparation process and set up the initial structure for a new day's
solution. Adjust the day number accordingly.

## Running the go solutions (WIP)

### How to run the solutions

- For each day there is a folder days/day_XX, `main.go` files contains the solutions code.
- `dayXX.txt` files are located in the same folder as for Python

To run a particular solution, use the following command (make sure to have the corresponding language installed):

```bash
# Inside go repository
go run . -day XX -help
```
