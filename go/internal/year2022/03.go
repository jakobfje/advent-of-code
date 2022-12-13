package year2022

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"unicode"
)

const (
	input03 = `vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw`
)

func Day03() {
	f, err := os.Open("internal/year2022/03.txt")
	if err != nil {
		fmt.Printf("Error: %v", err)
		os.Exit(1)
	}
	defer f.Close()

	linesTest := getLines(strings.NewReader(input03))
	linesReal := getLines(bufio.NewReader(f))

	fmt.Println(day03Task1(linesTest))
	fmt.Println(day03Task1(linesReal))
	fmt.Println(day03Task2(linesTest))
	fmt.Println(day03Task2(linesReal))

}

func day03Task1(lines []string) string {
	sum := 0

	for _, backpack := range lines {
		comp1 := backpack[:len(backpack)/2]
		comp2 := backpack[len(backpack)/2:]

		for _, item := range comp1 {
			if strings.ContainsRune(comp2, item) {
				sum += getPrio(item)
				break
			}
		}

	}

	return fmt.Sprintf("%d", sum)
}

func day03Task2(lines []string) string {
	sum := 0

	for i := 0; i < len(lines)/3; i++ {
		bp1 := lines[i*3]
		bp2 := lines[i*3+1]
		bp3 := lines[i*3+2]

		for _, item := range bp1 {
			if strings.ContainsRune(bp2, item) && strings.ContainsRune(bp3, item) {
				sum += getPrio(item)
				break
			}
		}

	}

	return fmt.Sprintf("%d", sum)
}

func getPrio(item rune) int {
	if unicode.IsUpper(item) {
		return int(item) - 65 + 27
	} else {
		return int(item) - 97 + 1
	}
}
