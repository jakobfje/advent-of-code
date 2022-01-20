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

    # print(opCode, modes)
    return opCode, modes

def getData(code, mode, value):
    if mode == 0:
        return code[value]
    elif mode == 1:
        return value

def IntCode(code, phaseSetting, inSignal):
    instrAddr = 0
    inCounter = 0
    outSignal = 0

    while True:
        instr = code[instrAddr]
        opCode, modes = parseInstruction(str(instr))

        if (opCode == 0):
            print("Error")
            exit()
        elif opCode == 1:
            # Add
            # print(code[instrAddr:instrAddr+4])
            data1 = getData(code, modes[0], code[instrAddr + 1])
            data2 = getData(code, modes[1], code[instrAddr + 2])
            storeAddr = code[instrAddr + 3]
            # print(data1, " + ", data2)
            code[storeAddr] = data1 + data2
            instrAddr += 4
        elif opCode == 2:
            # Multiply
            # print(code[instrAddr:instrAddr+4])
            data1 = getData(code, modes[0], code[instrAddr + 1])
            data2 = getData(code, modes[1], code[instrAddr + 2])
            storeAddr = code[instrAddr + 3]
            # print(data1, " * ", data2)
            code[storeAddr] = data1 * data2
            instrAddr += 4
        elif opCode == 3:
            # Input
            # print(code[instrAddr:instrAddr+2])
            storeAddr = code[instrAddr + 1]
            # code[storeAddr] = int(input("Input: "))
            if inCounter == 0:
                # print("Input: ", phaseSetting, " to adress ", storeAddr)
                code[storeAddr] = phaseSetting
            else:
                # print("Input: ", inSignal, " to adress ", storeAddr)
                code[storeAddr] = inSignal
            inCounter += 1
            instrAddr += 2
        elif opCode == 4:
            # Output
            # print(code[instrAddr:instrAddr+2])
            data1 = getData(code, modes[0], code[instrAddr + 1])
            # print("Output: ", data1)
            outSignal = data1
            # if data1 != 0:
            #     exit()
            instrAddr += 2
        elif opCode == 5:
            # Jump if true
            data1 = getData(code, modes[0], code[instrAddr + 1])
            data2 = getData(code, modes[1], code[instrAddr + 2])
            if data1 != 0:
                instrAddr = data2
            else:
                instrAddr += 3
        elif opCode == 6:
            # Jump if false
            data1 = getData(code, modes[0], code[instrAddr + 1])
            data2 = getData(code, modes[1], code[instrAddr + 2])
            if data1 == 0:
                instrAddr = data2
            else:
                instrAddr += 3
        elif opCode == 7:
            # Less than
            data1 = getData(code, modes[0], code[instrAddr + 1])
            data2 = getData(code, modes[1], code[instrAddr + 2])
            storeAddr = code[instrAddr + 3]
            if data1 < data2:
                code[storeAddr] = 1
            else:
                code[storeAddr] = 0
            instrAddr += 4
        elif opCode == 8:
            # Less than
            data1 = getData(code, modes[0], code[instrAddr + 1])
            data2 = getData(code, modes[1], code[instrAddr + 2])
            storeAddr = code[instrAddr + 3]
            if data1 == data2:
                code[storeAddr] = 1
            else:
                code[storeAddr] = 0
            instrAddr += 4
        elif opCode == 99:
            # print("Finished")
            break

        # print(code)
        # input()
    return outSignal



# code = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
f = open('Day7Data.txt', 'r')
code = [int(x) for x in list(f.readline().rstrip().split(','))]


maxOutput = 0
perms = list(permutations(range(0, 5)))

for phaseSettings in perms:
    inSignal = 0
    output = 0
    for phaseSetting in phaseSettings:
        inSignal = output
        codeCopy = code.copy()
        output = IntCode(codeCopy, phaseSetting, inSignal)
        # print(phaseSetting, inSignal, output)

    if output > maxOutput:
        maxOutput = output
        print(maxOutput)


print(maxOutput)

