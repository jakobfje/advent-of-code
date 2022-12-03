import numpy

def getLines(path):
    f = open(path)
    lines = f.read().splitlines()
    f.close()
    return lines

def countTrees(input, right, down):
    # print(input)
    trees = 0
    col = 0
    colMax = len(input[0])
 
    for i in range(down, len(input), down):
        col = col + right
        if input[i][(col)%(colMax)] == '#':
            trees = trees + 1

    return trees

def task1(input):
    return countTrees(input, 3, 1)
    
def task2(input):
    slope = list(range(5))
    slope[0] = countTrees(input, 1, 1)
    slope[1] = countTrees(input, 3, 1)
    slope[2] = countTrees(input, 5, 1)
    slope[3] = countTrees(input, 7, 1)
    slope[4] = countTrees(input, 1, 2)
    print(slope)
    prod = slope[0] * slope[1] * slope[2] * slope[3] * slope[4] 
    return prod


print("Answer 1: " + str(task1([
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#"])))
print()
print("Answer 1: " + str(task1(getLines("03input.txt"))))
print()
print("Answer 2: " + str(task2([
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#"])))
print()
print("Answer 2: " + str(task2(getLines("03input.txt"))))