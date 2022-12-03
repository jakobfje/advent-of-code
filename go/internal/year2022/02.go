package year2022

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

const (
	input02 = `A Y
B X
C Z`
)

func Day02() {
	f, err := os.Open("internal/year2022/02.txt")
	if err != nil {
		fmt.Printf("Error: %v", err)
		os.Exit(1)
	}
	defer f.Close()

	linesTest := getLines(strings.NewReader(input02))
	linesReal := getLines(bufio.NewReader(f))

	fmt.Println(day02Task1(linesTest))
	fmt.Println(day02Task1(linesReal))
	fmt.Println(day02Task2(linesTest))
	fmt.Println(day02Task2(linesReal))

}

func day02Task1(lines []string) string {
	score := 0
	for _, line := range lines {
		choise := strings.Split(line, " ")

		switch choise[0] {
		case "A": // Opponent Rock
			switch choise[1] {
			case "X": // You Rock
				score += 1 + 3
			case "Y": // You Paper
				score += 2 + 6
			case "Z": // You Scissors
				score += 3 + 0
			}
		case "B": // Opponent Paper
			switch choise[1] {
			case "X": // You Rock
				score += 1 + 0
			case "Y": // You Paper
				score += 2 + 3
			case "Z": // You Scissors
				score += 3 + 6
			}
		case "C": // Opponent Scissors
			switch choise[1] {
			case "X": // You Rock
				score += 1 + 6
			case "Y": // You Paper
				score += 2 + 0
			case "Z": // You Scissors
				score += 3 + 3
			}
		}
	}

	return fmt.Sprintf("%d", score)
}

func day02Task2(lines []string) string {
	score := 0
	for _, line := range lines {
		choise := strings.Split(line, " ")

		switch choise[0] {
		case "A": // Opponent Rock
			switch choise[1] {
			case "X": // You Scissors
				score += 3 + 0
			case "Y": // You Rock
				score += 1 + 3
			case "Z": // You Paper
				score += 2 + 6
			}
		case "B": // Opponent Paper
			switch choise[1] {
			case "X": // You Rock
				score += 1 + 0
			case "Y": // You Paper
				score += 2 + 3
			case "Z": // You Scissors
				score += 3 + 6
			}
		case "C": // Opponent Scissors
			switch choise[1] {
			case "X": // You Paper
				score += 2 + 0
			case "Y": // You Scissors
				score += 3 + 3
			case "Z": // You Rock
				score += 1 + 6
			}
		}
	}

	return fmt.Sprintf("%d", score)
}
