import pprint
import re

def getLines(path):
    f = open(path)
    lines = f.read().splitlines()
    f.close()
    return lines

def task1(input, preambleLength):
    idx = 0
    notValidNr = 0
    for newValue in input[preambleLength:]:
        compList = input[idx : preambleLength + idx]
        idx += 1
        # print(compList)
        valid = False
        for i in compList:
            for j in compList:
                if int(i) != int(j) and (int(i) + int(j)) == int(newValue):
                    # print(i + "+" + j + "=" + newValue + " Valid")
                    valid = True
                    break
            if valid:
                break
        
        if not valid:
            notValidNr = newValue
            break

    return notValidNr

    
def task2(input, preambleLength):
    idx = 0
    notValidNr = 0
    for newValue in input[preambleLength:]:
        compList = input[idx : preambleLength + idx]
        idx += 1
        # print(compList)
        valid = False
        for i in compList:
            for j in compList:
                if int(i) != int(j) and (int(i) + int(j)) == int(newValue):
                    # print(i + "+" + j + "=" + newValue + " Valid")
                    valid = True
                    break
            if valid:
                break
        
        if not valid:
            notValidNr = newValue
            break

    contigList = []
    valid = False
    input = list(map(int, input))
    for i in range(len(input)):
        for j in range(i, len(input)+1):
            if len(input[i:j]) > 1 and int(notValidNr) == sum(input[i:j]):
                contigList = input[i:j]
                valid = True
                break
        if valid:
            break

    return min(contigList) + max(contigList)

testInput = ["35",
    "20",
    "15",
    "47",
    "25",
    "40",
    "62",
    "55",
    "65",
    "95",
    "102",
    "117",
    "150",
    "182",
    "127",
    "219",
    "299",
    "277",
    "309",
    "576"]
input = getLines("09input.txt")

print()
print("Task 1")
print("---------")
print("Test: " + str(task1(testInput, 5)))
print("Answer: " + str(task1(input, 25)))
print()
print()
print("Task 2")
print("---------")
print("Test: " + str(task2(testInput, 5)))
print("Answer: " + str(task2(input, 25)))
print()