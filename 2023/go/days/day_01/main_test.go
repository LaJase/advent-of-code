package day_01_test

import (
	"testing"

	"github.com/LaJase/advent_of_code/2023/go/days/day_01"
	"github.com/LaJase/advent_of_code/2023/go/internal"
)

func TestPartOne(t *testing.T) {
	t.Parallel()

	input := internal.LoadInputLines("day01_example_1.txt")
	expectedResult := 142
	result := day_01.Part1(input)

	if result != expectedResult {
		t.Errorf("expected result was %d, but got %d instead", expectedResult, result)
	}
}

func TestPartTwo(t *testing.T) {
	t.Parallel()

	input := internal.LoadInputLines("day01_example_2.txt")
	expectedResult := 281
	result := day_01.Part2(input)

	if result != expectedResult {
		t.Errorf("expected result was %d, but got %d instead", expectedResult, result)
	}
}
