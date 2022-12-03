import pprint
import re
import math
import numpy as np
import time

def getLines(path):
    f = open(path)
    lines = f.read().splitlines()
    f.close()
    return lines

def task1(data):
    timeStamp = int(data[0])
    busses = [int(bus) for bus in data[1].split(',') if bus != 'x']
    timeToNext = [math.floor(timeStamp/bus) * bus + bus - timeStamp for bus in busses]

    return min(timeToNext) * busses[timeToNext.index(min(timeToNext))]

    
def task2(data):
    busses = [[idx, int(bus)] for idx,bus in enumerate(data[1].split(',')) if bus != 'x']

    time = busses[0][1] - busses[0][0]
    step = busses[0][1]
    checkId = 1

    while True:
        if ((time + busses[checkId][0]) % busses[checkId][1]) == 0:
            step *= busses[checkId][1]
            checkId += 1
        
        if checkId == len(busses):
            break
        
        time += step
    
    return time


testData = ["939",
    "7,13,x,x,59,x,31,19"]
testData2 = ["939",
    "17,x,13,19"]
testData3 = ["939",
    "67,7,59,61"]
testData4 = ["939",
    "67,x,7,59,61"]
testData5 = ["939",
    "67,7,x,59,61"]
testData6 = ["939",
    "1789,37,47,1889"]
data = getLines("13input.txt")

print()
print("Task 1")
print("---------")
# print("Test: " + str(task1(testData)))
# print("Answer: " + str(task1(data)))
print()
print()
print("Task 2")
print("---------")
# print("Test: " + str(task2(testData)))
# print("Test: " + str(task2(testData2)))
# print("Test: " + str(task2(testData3)))
# print("Test: " + str(task2(testData4)))
# print("Test: " + str(task2(testData5)))
start = time.time()
print("Test: " + str(task2(testData6)))
print(time.time()-start)
print("Answer: " + str(task2(data)))
print()