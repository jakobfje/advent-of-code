package year2022

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

const (
	inputXX = ``
)

func DayXX() {
	f, err := os.Open("internal/year2022/XX.txt")
	if err != nil {
		fmt.Printf("Error: %v", err)
		os.Exit(1)
	}
	defer f.Close()

	linesTest := getLines(strings.NewReader(inputXX))
	linesReal := getLines(bufio.NewReader(f))

	fmt.Println("Task 1 test data:", dayXXTask1(linesTest))
	fmt.Println("Task 1 real data:", dayXXTask1(linesReal))
	fmt.Println("Task 2 test data:", dayXXTask2(linesTest))
	fmt.Println("Task 2 real data:", dayXXTask2(linesReal))

}

func dayXXTask1(lines []string) string {
	return fmt.Sprintf("%d", len(lines))
}

func dayXXTask2(lines []string) string {
	return fmt.Sprintf("%d", len(lines))
}
