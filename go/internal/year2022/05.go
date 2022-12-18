package year2022

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const (
	input05 = `    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2`
)

func Day05() {
	f, err := os.Open("internal/year2022/05.txt")
	if err != nil {
		fmt.Printf("Error: %v", err)
		os.Exit(1)
	}
	defer f.Close()

	linesTest := getLines(strings.NewReader(input05))
	linesReal := getLines(bufio.NewReader(f))

	fmt.Println("Task 1 test data:", day05Task1(linesTest))
	fmt.Println("Task 1 real data:", day05Task1(linesReal))
	fmt.Println("Task 2 test data:", day05Task2(linesTest))
	fmt.Println("Task 2 real data:", day05Task2(linesReal))

}

func day05Task1(lines []string) string {
	layout := getLayout(lines)

	for _, line := range lines {
		if !strings.Contains(line, "move") {
			continue
		}

		amount, _ := strconv.Atoi(strings.Split(line, " ")[1])
		from, _ := strconv.Atoi(strings.Split(line, " ")[3])
		to, _ := strconv.Atoi(strings.Split(line, " ")[5])
		from--
		to--

		for i := 0; i < amount; i++ {
			crate := layout[from][len(layout[from])-1]
			layout[to] = append(layout[to], crate)
			layout[from] = layout[from][:len(layout[from])-1]
		}
	}

	result := ""
	for _, pile := range layout {
		result += string(pile[len(pile)-1])
	}
	return fmt.Sprintf("%s", result)
}

func day05Task2(lines []string) string {
	layout := getLayout(lines)

	for _, line := range lines {
		if !strings.Contains(line, "move") {
			continue
		}

		amount, _ := strconv.Atoi(strings.Split(line, " ")[1])
		from, _ := strconv.Atoi(strings.Split(line, " ")[3])
		to, _ := strconv.Atoi(strings.Split(line, " ")[5])
		from--
		to--

		crates := layout[from][len(layout[from])-amount:]
		layout[from] = layout[from][:len(layout[from])-amount]
		for _, crate := range crates {
			layout[to] = append(layout[to], crate)
		}
	}

	result := ""
	for _, pile := range layout {
		result += string(pile[len(pile)-1])
	}
	return fmt.Sprintf("%s", result)
}

func getLayout(lines []string) [][]byte {
	var layoutLines []string
	for _, line := range lines {
		if line == "" {
			break
		}
		layoutLines = append(layoutLines, line)
	}
	pileNrs := strings.Split(strings.TrimSpace(layoutLines[len(layoutLines)-1]), " ")
	piles, _ := strconv.Atoi(pileNrs[len(pileNrs)-1])

	var layout [][]byte
	for len(layout) < piles {
		layout = append(layout, make([]byte, 0))
	}

	for i := len(layoutLines) - 2; i >= 0; i-- {
		for j := 0; j < piles; j++ {
			charIdx := 1 + 4*j
			char := layoutLines[i][charIdx]
			if char != 32 {
				layout[j] = append(layout[j], layoutLines[i][charIdx])
			}
		}
	}

	return layout
}
