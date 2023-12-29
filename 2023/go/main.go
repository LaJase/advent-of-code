package main

import (
	"flag"
	"fmt"
	"os"
	"strconv"

	"github.com/LaJase/advent_of_code/2023/go/internal"
)

func main() {
	sDay := flag.String("day", "", "day ID to execute")
	sInputFile := flag.String("input", "", "input file path")
	bAll := flag.Bool("all", true, "If you want to run all the puzzles")
	bFirst := flag.Bool("first", false, "if you want to run only the first part")
	bSecond := flag.Bool("second", false, "if you want to run only the second part")
	flag.Parse()

	var day int

	fmt.Println("")
	fmt.Println("=============================")
	if *sDay == "" {
		os.Exit(1)
	} else {
		var err error
		day, err = strconv.Atoi(*sDay)
		if err != nil {
			fmt.Println("couldn't parse day")
			os.Exit(1)
		}
	}

	if *sInputFile == "" {
		currentWd, _ := os.Getwd()
		*sInputFile = fmt.Sprintf("%s/../puzzles/day%02d.txt", currentWd, day)
		_, err := os.Stat(*sInputFile)
		if os.IsNotExist(err) {
			fmt.Println("No input file found or given")
			os.Exit(1)
		} else {
			fmt.Printf("\t found file: %s\n\n", *sInputFile)
		}
	}

	inputPath := *sInputFile
	internal.RunChallenge(day, inputPath, *bAll, *bFirst, *bSecond)
	fmt.Println("=============================")
}
