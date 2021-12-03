import pprint
import re

def getLines(path):
    f = open(path)
    lines = f.read().splitlines()
    f.close()
    return lines

def task1(data):
    gammarate = "0b"
    epsilonrate = "0b"
    
    for i in range(len(data[0])):
        zeros = len([1 for x in data if x[i] == "0"])
        ones = len([1 for x in data if x[i] == "1"])

        if ones > zeros:
            gammarate += "1"
            epsilonrate += "0"
        else:
            gammarate += "0"
            epsilonrate += "1"
    
    return int(gammarate, 2) * int(epsilonrate, 2)

    
def task2(data):
    oxyData = data.copy()
    co2Data = data.copy()

    for i in range(len(data[0])):
        ones = len([1 for x in oxyData if x[i] == "1"])
        zeros = len([1 for x in oxyData if x[i] == "0"])
        if ones >= zeros:
            oxyData = [x for x in oxyData if x[i] == "1"]
        else:
            oxyData = [x for x in oxyData if x[i] == "0"]

        if len(oxyData) == 1:
            break

    for i in range(len(data[0])):
        ones = len([1 for x in co2Data if x[i] == "1"])
        zeros = len([1 for x in co2Data if x[i] == "0"])
        if ones >= zeros:
            co2Data = [x for x in co2Data if x[i] == "0"]
        else:
            co2Data = [x for x in co2Data if x[i] == "1"]

        if len(co2Data) == 1:
            break

    return int(oxyData[0], 2) * int(co2Data[0], 2)

testData = ["00100",
"11110",
"10110",
"10111",
"10101",
"01111",
"00111",
"11100",
"10000",
"11001",
"00010",
"01010"]
data = getLines("03input.txt")

print()
print("Task 1")
print("---------")
print("Test: " + str(task1(testData)))
print("Answer: " + str(task1(data)))
print()
print("Task 2")
print("---------")
print("Test: " + str(task2(testData)))
print("Answer: " + str(task2(data)))
print()