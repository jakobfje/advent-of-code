import pprint
import re

def getLines(path):
    f = open(path)
    lines = f.read().splitlines()
    f.close()
    return lines

def maskValue(mask, value):
    mult = 1
    maskedVal = 0
    value = "{0:b}".format(int(value))
    value = list(['0']*(36-len(value)) + list(value))
    value.reverse()
    mask = list(mask)
    mask.reverse()
    for idx, char in enumerate(list(value)):
        if mask[idx] == 'X':
            maskedVal += int(char)*mult
        else:
            maskedVal += int(mask[idx])*mult
        mult *= 2
    
    return maskedVal

def task1(data):
    mask = ""
    memory = {}
    for line in data:
        cmd = line.split('=')[0].strip()
        value = line.split('=')[1].strip()

        if cmd == 'mask':
            mask = value
        elif cmd[0:3] == 'mem':
            addr = cmd.split('[')[1].split(']')[0]
            memory[addr] = maskValue(mask, value)

    memSum = 0
    for key in memory.keys():
        memSum += memory[key]
    return memSum

def getMaskedAddr(mask, addr):
    mult = 1
    addresses = ['']
    addr = "{0:b}".format(int(addr))
    addr = list(['0']*(36-len(addr)) + list(addr))
    addr.reverse()
    mask = list(mask)
    mask.reverse()

    for idx, char in enumerate(list(addr)):
        if mask[idx] == 'X':
            # Floating
            addresses = ["1" + x for x in addresses] + ["0" + x for x in addresses]
        elif mask[idx] == '0':
            # Unchanged
            addresses = [char + x for x in addresses]
        else:
            # Overwritten with 1
            addresses = ["1" + x for x in addresses]
        mult *= 2
    
    return addresses

    
def task2(data):
    mask = ""
    memory = {}
    for line in data:
        cmd = line.split('=')[0].strip()
        value = line.split('=')[1].strip()

        if cmd == 'mask':
            mask = value
        elif cmd[0:3] == 'mem':
            addr = cmd.split('[')[1].split(']')[0]
            addresses = getMaskedAddr(mask, addr)
            for x in addresses:
                memory[x] = int(value)

    memSum = 0
    for key in memory.keys():
        memSum += memory[key]
    return memSum

testData = ["mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
    "mem[8] = 11",
    "mem[7] = 101",
    "mem[8] = 0"]
testData2 = ["mask = 000000000000000000000000000000X1001X",
    "mem[42] = 100",
    "mask = 00000000000000000000000000000000X0XX",
    "mem[26] = 1"]
data = getLines("14input.txt")

print()
print("Task 1")
print("---------")
print("Test: " + str(task1(testData)))
print("Answer: " + str(task1(data)))
print()
print()
print("Task 2")
print("---------")
print("Test: " + str(task2(testData2)))
print("Answer: " + str(task2(data)))
print()