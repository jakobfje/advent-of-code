import pprint
import re

def getLines(path):
    f = open(path)
    lines = f.read().splitlines()
    f.close()

    return lines

def cleanInput(input):
    input = list(map(int, input))
    input.append(0)
    input.append(max(input)+3)
    input.sort()
    return input

def task1(input):
    input = cleanInput(input)
    
    oneCnt = 0
    threeCnt = 0
    for i in range(1,len(input)):
        if input[i] - input[i-1] == 1:
            oneCnt += 1
        elif input[i] - input[i-1] == 3:
            threeCnt += 1
    
    return oneCnt*threeCnt

def getChildCnt(input, searchDict):
    cnt = 0

    for i in [1,2,3]:
        if i < len(input) and (input[i] - input[0]) < 4:
            if len(input[i:]) > 1:
                if input[i] in searchDict.keys():
                    cnt += 1 * searchDict[input[i]]
                else:
                    children = getChildCnt(input[i:], searchDict)
                    searchDict[input[i]] = children
                    cnt += 1 * children
            else:
                cnt += 1
                
    return cnt

def task2(input):
    return getChildCnt(cleanInput(input), {})

testInput1 = ["16", "10", "15", "5", "1", "11",
              "7", "19", "6", "12", "4"]
testInput2 = ["28", "33", "18", "42", "31", "14", "46", "20", "48",
              "47", "24", "23", "49", "45", "19", "38", "39", "11",
              "1", "32", "25", "35", "8", "17", "7", "9", "4", "2",
              "34", "10", "3"]
input = getLines("10input.txt")

print()
print("Task 1")
print("---------")
print("Test: " + str(task1(testInput1)))
print("Test: " + str(task1(testInput2)))
print("Answer: " + str(task1(input)))
print()
print()
print("Task 2")
print("---------")
print("Test: " + str(task2(testInput1)))
print("Test: " + str(task2(testInput2)))
print("Answer: " + str(task2(input)))
print()