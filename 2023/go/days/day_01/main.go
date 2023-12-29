package day_01

import (
	"fmt"
	"log"
	"regexp"
	"strconv"
	"strings"
	"time"
)

func atoi(s string) int {
	i, err := strconv.Atoi(s)
	if err != nil {
		log.Fatal(err)
	}
	return i
}

func IndexOf[T comparable](collection []T, elt T) int {
	for i, x := range collection {
		if x == elt {
			return i
		}
	}
	return -1
}

func digitValue(s string) int {
	if digitRe.MatchString(s) {
		return atoi(s)
	}
	var i int
	if i = IndexOf(digitNames, s); i < 0 {
		panic("Name of digit unknown: " + s)
	}
	return i + 1
}

// Run function of the daily challenge
func Run(input []string, all bool, first bool, second bool) {
	if all || first {
		start := time.Now()
		result := Part1(input)
		end := time.Now()
		fmt.Printf("Part one: %d \texecution time: %.4f sec\n", result, end.Sub(start).Seconds())
	}
	if all || second {
		start := time.Now()
		result := Part2(input)
		end := time.Now()
		fmt.Printf("Part two: %d \texecution time: %.4f sec\n", result, end.Sub(start).Seconds())
	}
}

// solves the first part of the exercise
func Part1(input []string) int {
	var i, high, low, sum, value int
	digits := "0123456789"
	for _, line := range input {
		if i = strings.IndexAny(line, digits); i < 0 {
			continue
		}
		high = atoi(line[i : i+1])
		if i = strings.LastIndexAny(line, digits); i < 0 {
			continue
		}
		low = atoi(line[i : i+1])
		value = high*10 + low
		sum += value
	}
	return sum
}

var (
	digitAnyRe, digitRe *regexp.Regexp
	digitNames          = []string{"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"}
)

// solves the second part of the exercise
func Part2(input []string) int {
	digitAnyRe = regexp.MustCompile("[0-9]|one|two|three|four|five|six|seven|eight|nine")
	digitRe = regexp.MustCompile("[0-9]")
	var sum, value int
	var match string
	for _, line := range input {
		if match = digitAnyRe.FindString(line); len(match) == 0 {
			continue
		}
		high := digitValue(match)
		low := 0
		l := len(line)
		for i := len(line) - 1; i >= 0; i-- {
			if match = digitAnyRe.FindString(line[i:l]); len(match) == 0 {
				continue
			}
			low = digitValue(match)
			break
		}
		value = high*10 + low
		sum += value
	}
	return sum
}
