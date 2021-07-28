import pprint
import re

def getLines(path):
    f = open(path)
    lines = f.read().splitlines()
    f.close()
    return lines

def getRuleDict(input):
    rules = [x.split('bags contain') for x in input]
    ruleDict = {}
    for rule in rules:
        ruleDict[rule[0].strip()] = [x.strip().split(' ')[1] + " " + x.strip().split(' ')[2] for x in rule[1].split(',')]
    return ruleDict
    

def getRuleDictWithCnt(input):
    rules = [x.split('bags contain') for x in input]
    ruleDict = {}
    for rule in rules:
        ruleDict[rule[0].strip()] = [x.strip().split(' ')[0] + " " + x.strip().split(' ')[1] + " " + x.strip().split(' ')[2] for x in rule[1].split(',')]
    return ruleDict


def cntMasters(ruleDict, bagType, masterSet=None):
    if not masterSet:
        masterSet = set()

    cnt = 0
    for rule in ruleDict.keys():
        if rule not in masterSet and bagType in ruleDict[rule]:
            masterSet.add(rule)
            cnt += 1 + cntMasters(ruleDict, rule, masterSet)
    
    return cnt


def cntTotalSlaves(ruleDict, bagType):
    cnt = 0

    for slave in ruleDict[bagType]:
        if (slave.split(' ')[1] + " " + slave.split(' ')[2]) != "other bags.":
            cnt += int(slave.split(' ')[0]) + int(slave.split(' ')[0]) * cntTotalSlaves(ruleDict, slave.split(' ')[1] + " " + slave.split(' ')[2])

    return cnt


def task1(input):
    return cntMasters(getRuleDict(input), "shiny gold")

    
def task2(input):
    return cntTotalSlaves(getRuleDictWithCnt(input), "shiny gold")


testInput1 = ["light red bags contain 1 bright white bag, 2 muted yellow bags.",
    "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
    "bright white bags contain 1 shiny gold bag.",
    "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
    "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
    "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
    "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
    "faded blue bags contain no other bags.",
    "dotted black bags contain no other bags."]
testInput2 = ["shiny gold bags contain 2 dark red bags.",
    "dark red bags contain 2 dark orange bags.",
    "dark orange bags contain 2 dark yellow bags.",
    "dark yellow bags contain 2 dark green bags.",
    "dark green bags contain 2 dark blue bags.",
    "dark blue bags contain 2 dark violet bags.",
    "dark violet bags contain no other bags."]
input = getLines("07input.txt")

print()
print("Task 1")
print("---------")
print("Test: " + str(task1(testInput1)))
print("Answer: " + str(task1(input)))
print()
print()
print("Task 2")
print("---------")
print("Test1: " + str(task2(testInput1)))
print("Test2: " + str(task2(testInput2)))
print("Answer: " + str(task2(input)))
print()