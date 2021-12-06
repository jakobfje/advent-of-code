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

def task1(data):
    print(data)
    grid = {}
    for line in data:
        x1, y1, x2, y2 = re.split('->|,', line.replace(" ", ""))
        if x1 == x2 or y1 == y2:
            if x1 == x2:
                range(int(y1), int(y2))
            else:
                range(int(x1), int(x2))
            print(x1, y1, x2, y2)
            if (x1 + "," + y1) not in grid.keys():
                grid[(x1 + "," + y1)] = 0
            
            grid[(x1 + "," + y1)] += 1

            print(grid)
            
    return "output1"

    
def task2(data):
    print(data)
    return "output2"

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
testResult2 = ""
data = getLines("01input.txt")

print()
testAndVerify(1, str(task1(testData)), testResult1)
# print("Task 1, Answer: " + str(task1(data)))
# testAndVerify(2, str(task2(testData)), testResult2)
# print("Task 2, Answer: " + str(task2(data)))
print()