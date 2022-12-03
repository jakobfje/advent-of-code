from itertools import permutations

def parseInstruction(instr):
    if len(instr) > 1:
        opCode = int(instr[-2] + instr[-1])
    else:
        opCode = int(instr[-1])

    if len(instr) < 3:
        modes = [0, 0]
    else:
        modes = [int(d) for d in instr[0:(len(instr)-2)]]

    modes.reverse()
    modes.append(0)
    modes.append(0)

    return opCode, modes

def getData(comp, mode, value):
    if mode == 0:
        while value > len(comp[0]):
            comp[0].append(0)
        return comp[0][value]
    elif mode == 1:
        return value
    elif mode == 2:
        while comp[2] + value > len(comp[0]):
            comp[0].append(0)
        return comp[0][comp[2] + value]

def getStoreAddr(comp, mode, value):
    if mode == 0:
        while value > len(comp[0]):
            comp[0].append(0)
        return value
    elif mode == 2:
        while comp[2] + value > len(comp[0]):
            comp[0].append(0)
        return comp[2] + value


def store(comp, address, data):
    while address >= len(comp[0]):
        comp[0].append(0)

    comp[0][address] = data


def IntCode(comp, inSignal):
    outSignal = 0

    while True:
        instr = comp[0][comp[1]]
        opCode, modes = parseInstruction(str(instr))

        # print(opCode)
        if (opCode == 0):
            print("Error")
            exit()

        elif opCode == 1:
            # Add
            data1 = getData(comp, modes[0], comp[0][comp[1] + 1])
            data2 = getData(comp, modes[1], comp[0][comp[1] + 2])
            storeAddr = getStoreAddr(comp, modes[2], comp[0][comp[1] + 3])
            # print(comp[0][comp[1]:comp[1]+4], data1, " add ", data2, " Store at ", storeAddr)
            store(comp, storeAddr, data1 + data2)
            comp[1] += 4

        elif opCode == 2:
            # Multiply
            data1 = getData(comp, modes[0], comp[0][comp[1] + 1])
            data2 = getData(comp, modes[1], comp[0][comp[1] + 2])
            storeAddr = getStoreAddr(comp, modes[2], comp[0][comp[1] + 3])
            # print(comp[0][comp[1]:comp[1]+4], data1, " multiply ", data2, " Store at ", storeAddr)
            store(comp, storeAddr, data1 * data2)
            comp[1] += 4

        elif opCode == 3:
            # Input
            # print(comp[0][comp[1]:comp[1]+2], " input ", inSignal)
            storeAddr = getStoreAddr(comp, modes[0], comp[0][comp[1] + 1])
            store(comp, storeAddr, inSignal)
            comp[1] += 2
            return opCode, outSignal

        elif opCode == 4:
            # Output
            data1 = getData(comp, modes[0], comp[0][comp[1] + 1])
            # print(comp[0][comp[1]:comp[1]+2], " output ", data1)
            outSignal = data1
            comp[1] += 2
            return opCode, outSignal

        elif opCode == 5:
            # Jump if true
            data1 = getData(comp, modes[0], comp[0][comp[1] + 1])
            data2 = getData(comp, modes[1], comp[0][comp[1] + 2])
            # print(comp[0][comp[1]:comp[1]+3], data1, " jump if true ", data2)
            if data1 != 0:
                comp[1] = data2
            else:
                comp[1] += 3

        elif opCode == 6:
            # Jump if false
            data1 = getData(comp, modes[0], comp[0][comp[1] + 1])
            data2 = getData(comp, modes[1], comp[0][comp[1] + 2])
            # print(comp[0][comp[1]:comp[1]+3], data1, " jump if false ", data2)
            if data1 == 0:
                comp[1] = data2
            else:
                comp[1] += 3

        elif opCode == 7:
            # Less than
            data1 = getData(comp, modes[0], comp[0][comp[1] + 1])
            data2 = getData(comp, modes[1], comp[0][comp[1] + 2])
            storeAddr = getStoreAddr(comp, modes[2], comp[0][comp[1] + 3])
            # print(comp[0][comp[1]:comp[1]+4], data1, " less than ", data2, " Store at ", storeAddr)
            if data1 < data2:
                store(comp, storeAddr, 1)
            else:
                store(comp, storeAddr, 0)
            comp[1] += 4

        elif opCode == 8:
            # Equals than
            data1 = getData(comp, modes[0], comp[0][comp[1] + 1])
            data2 = getData(comp, modes[1], comp[0][comp[1] + 2])
            storeAddr = getStoreAddr(comp, modes[2], comp[0][comp[1] + 3])
            # print(comp[0][comp[1]:comp[1]+4], data1, " equals ", data2, " Store at ", storeAddr)
            if data1 == data2:
                store(comp, storeAddr, 1)
            else:
                store(comp, storeAddr, 0)
            comp[1] += 4

        elif opCode == 9:
            # Adjust relative base
            data1 = getData(comp, modes[0], comp[0][comp[1] + 1])
            # print(comp[0][comp[1]:comp[1]+2], " add value ", data1, " to relative base")
            comp[2] += data1
            comp[1] += 2

        elif opCode == 99:
            print("Finished")
            return opCode, outSignal

        # print(comp[1], comp[2])
        # input()


# code = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
# code = [1102,34915192,34915192,7,4,7,99,0]
# code = [104,1125899906842624,99]

f = open('Day9Data.txt', 'r')
code = [int(x) for x in list(f.readline().rstrip().split(','))]

instPointer = 0
relativeBase = 0
comp = [code, instPointer, relativeBase]

inSignal = 2
opCode = 0
newOutput = 0

while opCode != 99:
    opCode, newOutput = IntCode(comp, inSignal)
    if opCode == 4:
        print("Output: ", newOutput)
        


