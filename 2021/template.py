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
    return "output1"

    
def task2(data):
    print(data)
    return "output2"


testData = [""]
testResult1 = ""
testResult2 = ""
data = getLines("xxinput.txt")

print()
testAndVerify(1, str(task1(testData)), testResult1)
# print("Task 1, Answer: " + str(task1(data)))
# testAndVerify(2, str(task2(testData)), testResult2)
# print("Task 2, Answer: " + str(task2(data)))
print()