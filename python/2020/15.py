import pprint
import re

def getLines(path):
    f = open(path)
    lines = f.read().splitlines()
    f.close()
    return lines

def task1(data, stopNr):
    idx = len(data)

    while idx < stopNr:
        dataCopy = data.copy()
        dataCopy.reverse()
        try:
            lastIdx = dataCopy[1:].index(dataCopy[0])
            data.append(lastIdx+1)
        except:
            data.append(0)
        idx += 1

    return data[-1]

    
def task2(data, stopNr):
    idx = len(data)
    log = {x:i for i,x in enumerate(data)}

    while idx < stopNr:
        if data[-1] in log.keys():
            data.append(idx - 1 - log[data[-1]])
            log[data[-2]] = idx - 1
        else:
            data.append(0)
            log[data[-2]] = idx - 1
        
        idx += 1

    return data[-1]

testData = [0,3,6]
data = [2,15,0,9,1,20]

print()
print("Task 1")
print("---------")
print("Test: " + str(task1(testData, 2020)))
print("Answer: " + str(task1(data, 2020)))
print()
print()
print("Task 2")
print("---------")
print("Test: " + str(task2(testData, 30000000)))
print("Answer: " + str(task2(data, 30000000)))
print()