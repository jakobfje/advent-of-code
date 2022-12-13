package year2022

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const (
	input04 = `2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8`
)

func Day04() {
	f, err := os.Open("internal/year2022/04.txt")
	if err != nil {
		fmt.Printf("Error: %v", err)
		os.Exit(1)
	}
	defer f.Close()

	linesTest := getLines(strings.NewReader(input04))
	linesReal := getLines(bufio.NewReader(f))

	fmt.Println("Task 1 test data:", day04Task1(linesTest))
	fmt.Println("Task 1 real data:", day04Task1(linesReal))
	fmt.Println("Task 2 test data:", day04Task2(linesTest))
	fmt.Println("Task 2 real data:", day04Task2(linesReal))

}

func day04Task1(lines []string) string {
	nrOfFulOverlaps := 0
	for _, pair := range lines {
		assignments := strings.Split(pair, ",")
		sections1 := createSectionRange(assignments[0])
		sections2 := createSectionRange(assignments[1])

		nrOfOverlaps := 0
		for _, val1 := range sections1 {
			for _, val2 := range sections2 {
				if val1 == val2 {
					nrOfOverlaps++
				}
			}
		}

		if nrOfOverlaps == len(sections1) ||
			nrOfOverlaps == len(sections2) {
			nrOfFulOverlaps++
		}
	}
	return fmt.Sprintf("%d", nrOfFulOverlaps)
}

func day04Task2(lines []string) string {
	nrOfOverlaps := 0
	for _, pair := range lines {
		assignments := strings.Split(pair, ",")
		sections1 := createSectionRange(assignments[0])
		sections2 := createSectionRange(assignments[1])

		overlapFound := false
		for _, val1 := range sections1 {
			for _, val2 := range sections2 {
				if val1 == val2 {
					nrOfOverlaps++
					overlapFound = true
					break
				}
			}
			if overlapFound {
				break
			}
		}

	}
	return fmt.Sprintf("%d", nrOfOverlaps)
}

func createSectionRange(assignment string) []int {
	minMax := strings.Split(assignment, "-")
	min, _ := strconv.Atoi(minMax[0])
	max, _ := strconv.Atoi(minMax[1])

	sections := make([]int, max-min+1)
	for i := 0; i <= max-min; i++ {
		sections[i] = i + min
	}

	return sections
}
