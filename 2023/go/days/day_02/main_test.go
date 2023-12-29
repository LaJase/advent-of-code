package day_02_test

import (
	"github.com/LaJase/advent_of_code/2023/go/days/day_02"
	"github.com/LaJase/advent_of_code/2023/go/internal"
	"testing"
)

func TestPartOne(t *testing.T) {
	t.Parallel()

	input := internal.LoadInputLines("input_1_test.txt")
	expectedResult := internal.LoadFirstInputLine("solution_1.txt")
	result := day_02.Part1(input)

	if result != expectedResult {
		t.Errorf("expected result was %s, but got %s instead", expectedResult, result)
	}
}

func TestPartTwo(t *testing.T) {
	t.Parallel()

	input := internal.LoadInputLines("input_2_test.txt")
	expectedResult := internal.LoadFirstInputLine("solution_2.txt")
	result := day_02.Part2(input)

	if result != expectedResult {
		t.Errorf("expected result was %s, but got %s instead", expectedResult, result)
	}
}
