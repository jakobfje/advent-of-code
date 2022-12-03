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
    data = [int(x) for x in data[0].split(',')]
    costArray = []

    for i in range(max(data)):
        totalCost = 0
        for crab in data:
            totalCost += abs(i-crab)
        costArray.append(totalCost)
    # pprint.pprint(costArray)
    return min(costArray)

    
def task2(data):
    data = [int(x) for x in data[0].split(',')]
    costArray = []

    for i in range(max(data)):
        totalCost = 0
        for crab in data:
            totalCost += sum(list(range(abs(i-crab)+1)))
        costArray.append(totalCost)

    return min(costArray)


testData = ["16,1,2,0,4,2,7,1,2,14"]
testResult1 = "37"
testResult2 = "168"
data = getLines("07input.txt")

print()
testAndVerify(1, str(task1(testData)), testResult1)
print("Task 1, Answer: " + str(task1(data)))
testAndVerify(2, str(task2(testData)), testResult2)
print("Task 2, Answer: " + str(task2(data)))
print()