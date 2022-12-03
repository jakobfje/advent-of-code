package year2022

import (
	"bufio"
	"io"
)

func getLines(reader io.Reader) []string {
	scanner := bufio.NewScanner(reader)
	var lines []string

	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	return lines
}
