package year2022

import (
	"fmt"
	"os"
	"strings"
)

const (
	input07 = `$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k`
)

type File struct {
	name string
	size uint
}

type Dir struct {
	parent  *Dir
	name    string
	size    uint
	dirs    *Dir
	dirCnt  uint
	files   *File
	fileCnt uint
}

func Day07() {
	f, err := os.Open("internal/year2022/07.txt")
	if err != nil {
		fmt.Printf("Error: %v", err)
		os.Exit(1)
	}
	defer f.Close()

	linesTest := getLines(strings.NewReader(input07))
	// linesReal := getLines(bufio.NewReader(f))

	fmt.Println("Task 1 test data:", day07Task1(linesTest))
	// fmt.Println("Task 1 real data:", day07Task1(linesReal))
	// fmt.Println("Task 2 test data:", day07Task2(linesTest))
	// fmt.Println("Task 2 real data:", day07Task2(linesReal))

}

func day07Task1(lines []string) string {
	baseDir := createNewDir("/", nil)
	currentDir := baseDir
	for i, line := range lines {
		args := strings.Split(" ")
		if args[1] == "cd" {
			currentDir = handleChangeDir(currentDir, args[2])
		}

	}

	return fmt.Sprintf("%d", len(lines))
}

func day07Task2(lines []string) string {
	return fmt.Sprintf("%d", len(lines))
}

func createNewDir(name string, parent *Dir) Dir {
	return Dir{name: name, size: 0, dirCnt: 0, fileCnt: 0, parent: parent}
}
