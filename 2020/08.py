import pprint
import re

def getLines(path):
    f = open(path)
    lines = f.read().splitlines()
    f.close()
    return lines

def runCode(input):
    runCnt = [0 for _ in range(len(input))]
    addr = 0
    accLast = 0
    acc = 0

    while 2 not in runCnt and addr != len(input):
        ins = input[addr].split(' ')[0]
        arg = int(input[addr].split(' ')[1])

        runCnt[addr] += 1
        if ins == 'acc':
            addr += 1
            accLast = acc
            acc += arg
        elif ins == 'jmp':
            addr += arg
        elif ins == 'nop':
            addr += 1

    if addr == len(input):
        accLast = acc

    return addr == len(input), accLast

def task1(input):
    success, accLast = runCode(input)
    print(success)
    return accLast

    
def task2(input):
    for x in range(len(input)):
        ins = input[x].split(' ')[0]
        arg = input[x].split(' ')[1]

        success = False
        accLast = 0

        if ins == 'nop':
            input[x] = 'jmp' + ' ' + arg
            success, accLast = runCode(input)
            input[x] = 'nop' + ' ' + arg
        elif ins == 'jmp':
            input[x] = 'nop' + ' ' + arg
            success, accLast = runCode(input)
            input[x] = 'jmp' + ' ' + arg

        if success:
            return accLast

    return 0

testInput = ["nop +0",
    "acc +1",
    "jmp +4",
    "acc +3",
    "jmp -3",
    "acc -99",
    "acc +1",
    "jmp -4",
    "acc +6"]
input = getLines("08input.txt")

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