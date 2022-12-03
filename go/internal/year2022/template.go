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

	fmt.Println(dayXXTask1(linesTest))
	fmt.Println(dayXXTask1(linesReal))
	fmt.Println(dayXXTask2(linesTest))
	fmt.Println(dayXXTask2(linesReal))

}

func dayXXTask1(lines []string) string {
	helperOutput := helper(lines)
	return fmt.Sprintf("%d", helperOutput)
}

func dayXXTask2(lines []string) string {
	helperOutput := helper(lines)
	return fmt.Sprintf("%d", helperOutput)
}

func helper(lines []string) int {
	return len(lines)
}
