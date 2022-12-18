package year2022

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

const (
	input06 = `nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg`
)

func Day06() {
	f, err := os.Open("internal/year2022/06.txt")
	if err != nil {
		fmt.Printf("Error: %v", err)
		os.Exit(1)
	}
	defer f.Close()

	linesTest := getLines(strings.NewReader(input06))
	linesReal := getLines(bufio.NewReader(f))

	fmt.Println("Task 1 test data:", day06Task1(linesTest))
	fmt.Println("Task 1 real data:", day06Task1(linesReal))
	fmt.Println("Task 2 test data:", day06Task2(linesTest))
	fmt.Println("Task 2 real data:", day06Task2(linesReal))

}

func day06Task1(lines []string) string {
	datastream := lines[0]
	firstMarker := 0

	for i, _ := range datastream {
		startOfPacket := datastream[i : i+4]
		if !multipleCharOccurence(startOfPacket) {
			firstMarker = i + 4
			break
		}
	}
	return fmt.Sprintf("%d", firstMarker)
}

func day06Task2(lines []string) string {
	datastream := lines[0]
	firstMarker := 0

	for i, _ := range datastream {
		startOfMessage := datastream[i : i+14]
		if !multipleCharOccurence(startOfMessage) {
			firstMarker = i + 14
			break
		}
	}
	return fmt.Sprintf("%d", firstMarker)
}

func multipleCharOccurence(dataSubString string) bool {
	for _, val := range dataSubString {
		if strings.Count(dataSubString, string(val)) > 1 {
			return true
		}
	}

	return false
}
