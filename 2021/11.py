from pprint import pprint
import re


def getLines(path):
    f = open(path)
    lines = f.read().splitlines()
    f.close()
    return lines


def testAndVerify(taskNr, taskResult, correctAnswer):
    rightOrWrong = ""
    if taskResult == correctAnswer:
        rightOrWrong = "Correct"
    else:
        rightOrWrong = "Wrong"
    print("Task " + str(taskNr) + ", Test:   " + str(taskResult) + ", " + str(rightOrWrong))

def increase_adjacent(data, row_in, col_in):
    coords = [[-1,-1], [-1,0], [-1,+1], 
        [0, -1], [0, +1],
        [+1,-1], [+1,0], [+1,+1]]
    for row_shift, col_shift in coords:
        row = row_in + row_shift
        col = col_in + col_shift
        if row >= 0 and row <= len(data)-1 and col >= 0 and col <= len(data[0])-1:
            if data[row][col] != 0:
                data[row][col] += 1
                if data[row][col] > 9:
                    data[row][col] = 0
                    increase_adjacent(data, row, col)


def task1(data):
    data = [[int(nr) for nr in line] for line in data]
    flash_cnt = 0
    for i in range(100):
        data = [[nr + 1 for nr in line] for line in data]
        for row, line in enumerate(data):
            for col, nr in enumerate(line):
                if nr == 10:
                    data[row][col] = 0
                    increase_adjacent(data, row, col)
        flash_cnt += sum(sum(1 for nr in line if nr == 0) for line in data)
    return flash_cnt

    
def task2(data):
    data = [[int(nr) for nr in line] for line in data]
    flash_cnt = 0
    loop_cnt = 0
    while flash_cnt != 100:
        flash_cnt = 0
        data = [[nr + 1 for nr in line] for line in data]
        for row, line in enumerate(data):
            for col, nr in enumerate(line):
                if nr == 10:
                    data[row][col] = 0
                    increase_adjacent(data, row, col)
        flash_cnt += sum(sum(1 for nr in line if nr == 0) for line in data)
        loop_cnt += 1
    return loop_cnt


testData = ["5483143223",
"2745854711",
"5264556173",
"6141336146",
"6357385478",
"4167524645",
"2176841721",
"6882881134",
"4846848554",
"5283751526"]
testResult1 = 1656
testResult2 = 195
data = getLines("11.txt")

print()
testAndVerify(1, task1(testData), testResult1)
print("Task 1, Answer: " + str(task1(data)))
testAndVerify(2, task2(testData), testResult2)
print("Task 2, Answer: " + str(task2(data)))
print()