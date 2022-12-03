package main

import (
	"flag"
	"fmt"

	y22 "github.com/jakobfje/advent-of-code/go/internal/year2022"
)

func main() {
	yearFlag := flag.Int("y", 2022, "# Year")
	dayFlag := flag.Int("d", 1, "# Day")
	flag.Parse()

	year := *yearFlag
	day := *dayFlag
	fmt.Print("Year: ", year)
	fmt.Println(", Day:", day)

	switch year {
	case 2022:
		switch day {
		case 1:
			y22.Day01()
		default:
			fmt.Println("Did not participate that day")
		}
	default:
		fmt.Println("Did not participate that year")
	}
}
