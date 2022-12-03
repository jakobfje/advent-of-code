package year2022

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

const (
	input01 = `1000
2000
3000

4000

5000
6000

7000
8000
9000

10000`
)

func Day01() {
	f, err := os.Open("internal/year2022/01.txt")
	if err != nil {
		fmt.Printf("Error: %v", err)
		os.Exit(1)
	}
	defer f.Close()

	linesTest := getLines(strings.NewReader(input01))
	linesReal := getLines(bufio.NewReader(f))

	fmt.Println(day01Task1(linesTest))
	fmt.Println(day01Task1(linesReal))
	fmt.Println(day01Task2(linesTest))
	fmt.Println(day01Task2(linesReal))
}

func day01Task1(lines []string) string {
	elfs := getCalorieSlice(lines)

	sort.Ints(elfs)
	length := len(elfs)

	return fmt.Sprint(elfs[length-1])
}

func day01Task2(lines []string) string {
	elfs := getCalorieSlice(lines)

	sort.Ints(elfs)
	length := len(elfs)

	return fmt.Sprintf("%d", elfs[length-1]+elfs[length-2]+elfs[length-3])
}

func getCalorieSlice(lines []string) []int {
	elfIdx := 0
	var elfs []int
	elfs = append(elfs, 0)

	for _, line := range lines {
		if line != "" {
			val, _ := strconv.Atoi(line)
			elfs[elfIdx] += val
		} else {
			elfs = append(elfs, 0)
			elfIdx++
		}
	}

	return elfs
}
