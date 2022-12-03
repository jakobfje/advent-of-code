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
    print("Task " + str(taskNr) + ", Test:   " + taskResult + ", " + rightOrWrong)


def getPointsInLine(x1, y1, x2, y2, diagonal):
    points = []
    if diagonal and ((x1 != x2) and (y1 != y2)):
        if x2 > x1:
            xSign = 1
        else:
            xSign = -1
        if y2 > y1:
            ySign = 1
        else:
            ySign = -1

        points = [str(x1 + xSign * i) + "," + str(y1 + ySign * i) for i in range(abs(x2-x1) + 1)]
    else:
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1

        if x1 == x2:
            points = [str(x1) + "," + str(y) for y in range(y1, y2 + 1)]
        elif y1 == y2:
            points = [str(x) + "," + str(y1) for x in range(x1, x2 + 1)]
    return points


def task1(data):
    grid = {}
    for line in data:
        x1, y1, x2, y2 = [int(x) for x in re.split('->|,', line.replace(" ", ""))]
        if (x1 == x2) or (y1 == y2):
            points = getPointsInLine(x1, y1, x2, y2, False)
            for point in points:
                if point not in grid:
                    grid[point] = 0
                
                grid[point] += 1

    return sum(1 for val in grid.values() if val > 1)

    
def task2(data):
    grid = {}
    for line in data:
        x1, y1, x2, y2 = [int(x) for x in re.split('->|,', line.replace(" ", ""))]
        points = getPointsInLine(x1, y1, x2, y2, True)
        for point in points:
            if point not in grid:
                grid[point] = 0
            
            grid[point] += 1

    return sum(1 for val in grid.values() if val > 1)


testData = ["0,9 -> 5,9",
"8,0 -> 0,8",
"9,4 -> 3,4",
"2,2 -> 2,1",
"7,0 -> 7,4",
"6,4 -> 2,0",
"0,9 -> 2,9",
"3,4 -> 1,4",
"0,0 -> 8,8",
"5,5 -> 8,2"]
testResult1 = "5"
testResult2 = "12"
data = getLines("05input.txt")

print()
testAndVerify(1, str(task1(testData)), testResult1)
print("Task 1, Answer: " + str(task1(data)))
testAndVerify(2, str(task2(testData)), testResult2)
print("Task 2, Answer: " + str(task2(data)))
print()