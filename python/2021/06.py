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

def cntFish(data, days):
    cnt = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for fish in data[0].split(','):
        cnt[int(fish)] += 1

    for i in range(days):
        temp = cnt[0]
        for i in range(len(cnt)-1):
            cnt[i] = cnt[i+1]
        cnt[6] += temp
        cnt[8] = temp

    return sum(cnt)

def task1(data):
    return cntFish(data, 80)

    
def task2(data):
    return cntFish(data, 256)


testData = ["3,4,3,1,2"]
testResult1 = "5934"
testResult2 = "26984457539"
data = getLines("06input.txt")

print()
testAndVerify(1, str(task1(testData)), testResult1)
print("Task 1, Answer: " + str(task1(data)))
testAndVerify(2, str(task2(testData)), testResult2)
print("Task 2, Answer: " + str(task2(data)))
print()