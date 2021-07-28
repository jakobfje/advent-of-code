import pprint
import re

def getLines(path):
    f = open(path)
    lines = f.read().splitlines()
    f.close()
    return lines


def getGroups(input):
    groups = []
    groups.append([])

    for line in input:
        if line == "":
            groups.append([])
        else:
            groups[-1].append(line)
    
    return groups


def union(listOfStrings):
    output = set(listOfStrings[0])
    for x in listOfStrings:
        output = output | set(x)
    return list(output)


def intersect(listOfStrings):
    output = set(listOfStrings[0])
    for x in listOfStrings:
        output = output & set(x)
    return list(output)


def task1(input):
    groups = getGroups(input)
    return sum([len(union(x)) for x in groups])


def task2(input):
    groups = getGroups(input)
    return sum([len(intersect(x)) for x in groups])


testInput = ["abc", "",
    "a", "b", "c", "",
    "ab", "ac", "",
    "a", "a", "a", "a", "",
    "b"]
input = getLines("06input.txt")

print()
print("Task 1")
print("---------")
print("Test: " + str(task1(testInput)))
print("Answer: " + str(task1(input)))
print()
print()
print("Task 2")
print("---------")
print("Test: " + str(task2(testInput)))
print("Answer: " + str(task2(input)))
print()