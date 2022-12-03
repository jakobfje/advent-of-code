import pprint
import re

def getLines(path):
    f = open(path)
    lines = f.read().splitlines()
    f.close()
    return lines

def task1(data):
    print(data)
    return "output1"

    
def task2(data):
    print(data)
    return "output2"

testData = [""]
data = getLines("xxinput.txt")

print()
print("Task 1")
print("---------")
print("Test: " + str(task1(testData)))
# print("Answer: " + str(task1(data)))
print()
print()
print("Task 2")
print("---------")
# print("Test: " + str(task2(testData)))
# print("Answer: " + str(task2(data)))
print()