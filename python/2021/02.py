import pprint
import re

def getLines(path):
    f = open(path)
    lines = f.read().splitlines()
    f.close()
    return lines

def task1(data):
    hori = 0
    depth = 0

    for line in data:
        dir, val = line.split(" ")
        
        if dir == "forward":
            hori += int(val)
        elif dir == "up":
            depth -= int(val)
        elif dir == "down":
            depth += int(val)

    return hori * depth

    
def task2(data):
    hori = 0
    depth = 0
    aim = 0

    for line in data:
        dir, val = line.split(" ")
        
        if dir == "forward":
            hori += int(val)
            depth += aim * int(val)
        elif dir == "up":
            aim -= int(val)
        elif dir == "down":
            aim += int(val)

    return hori * depth

testData = ["forward 5",
"down 5",
"forward 8",
"up 3",
"down 8",
"forward 2"]
data = getLines("02input.txt")

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