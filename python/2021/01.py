import pprint
import re

def getLines(path):
    f = open(path)
    lines = f.read().splitlines()
    f.close()
    return lines

def task1(data):
    incCnt = 0
    for i, line in enumerate(data[1:]):
        if int(line) > int(data[i]):
            incCnt += 1
    return incCnt
    
def task2(data):
    data = [int(x) for x in data]
    sumData = []

    for i, line in enumerate(data):
        if (i + 2) > (len(data) - 1):
            break

        sumData.append(str(sum(data[i:i+3])))

    return task1(sumData)

testData = ["199",
"200",
"208",
"210",
"200",
"207",
"240",
"269",
"260",
"263"]
data = getLines("01input.txt")

print()
print("Task 1")
print("---------")
print("Test: " + str(task1(testData)))
print("Answer: " + str(task1(data)))
print()
print()
print("Task 2")
print("---------")
print("Test: " + str(task2(testData)))
print("Answer: " + str(task2(data)))
print()