import pprint
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
    print("Task " + str(taskNr) + ", Test:   " + str(taskResult) + ", " + rightOrWrong)


def find_local_mins(data):
    local_mins = []

    for i, row in enumerate(data):
        for j, char in enumerate(row):
            if not ((i > 0 and int(char) >= int(data[i-1][j])) or
                (j > 0 and int(char) >= int(data[i][j-1])) or
                (j < len(row)-1 and int(char) >= int(data[i][j+1])) or
                (i < len(data)-1 and int(char) >= int(data[i+1][j]))):
                local_mins.append([i, j, int(char)])
    return local_mins


def get_bigger_neighbors(data, local_min, basin_list):
    row, col, val = local_min

    if row > 0 and val < int(data[row-1][col]) and int(data[row-1][col]) != 9:
        pos = [row-1, col, int(data[row-1][col])]
        if pos not in basin_list:
            basin_list.append(pos)
            get_bigger_neighbors(data, pos, basin_list)

    if col > 0 and val < int(data[row][col-1]) and int(data[row][col-1]) != 9:
        pos = [row, col-1, int(data[row][col-1])]
        if pos not in basin_list:
            basin_list.append(pos)
            get_bigger_neighbors(data, pos, basin_list)
    
    if col < len(data[0])-1 and val < int(data[row][col+1]) and int(data[row][col+1]) != 9:
        pos = [row, col+1, int(data[row][col+1])]
        if pos not in basin_list:
            basin_list.append(pos)
            get_bigger_neighbors(data, pos, basin_list)
    
    if row < len(data)-1 and val < int(data[row+1][col]) and int(data[row+1][col]) != 9:
        pos = [row+1, col, int(data[row+1][col])]
        if pos not in basin_list:
            basin_list.append(pos)
            get_bigger_neighbors(data, pos, basin_list)
    
    return 0


def task1(data):
    risk_sum = 0
    for x in find_local_mins(data):
        # print(x[0], x[1], x[2])
        risk_sum += x[2] + 1
    return risk_sum

    
def task2(data):
    basin_sizes = []
    for x in find_local_mins(data):
        # print(x[0], x[1], x[2])
        basin_list = [x]
        get_bigger_neighbors(data, x, basin_list)
        # print(basin_list)
        basin_sizes.append(len(basin_list))
    basin_sizes.sort(reverse=True)
    return  basin_sizes[0]*basin_sizes[1]*basin_sizes[2]


testData = ["2199943210",
"3987894921",
"9856789892",
"8767896789",
"9899965678"]
testResult1 = 15
testResult2 = 1134
data = getLines("09input.txt")

print()
testAndVerify(1, task1(testData), testResult1)
print("Task 1, Answer: " + str(task1(data)))
testAndVerify(2, task2(testData), testResult2)
print("Task 2, Answer: " + str(task2(data)))
print()