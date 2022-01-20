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

def IntCode(index, code, instrAddrList, phaseSetting, firstInput, inSignal):
    outSignal = 0
    phaseSet = not firstInput
    instrAddr = instrAddrList[index]

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
            if not phaseSet:
                phaseSet = True
                # print("Input: ", phaseSetting, " to adress ", storeAddr)
                code[storeAddr] = phaseSetting
            else:
                # print("Input: ", inSignal, " to adress ", storeAddr)
                code[storeAddr] = inSignal
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
            instrAddrList[index] = instrAddr
            return outSignal, False

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
            return 0, True

        # print(code)
        # input()


# code = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
code = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]

f = open('Day7Data.txt', 'r')
code = [int(x) for x in list(f.readline().rstrip().split(','))]

maxOutput = 0
perms = list(permutations(range(5, 5+5)))

# phaseSettings = [9,7,8,5,6]

for phaseSettings in perms:
    codeList = [code.copy() for i in range(0, 5)]
    instPointers = [0 for i in range(0, 5)]
    
    inSignal = 0
    output = 0
    firstInput = True
    finished = False

    while not finished:
        for i in range(0, len(phaseSettings)):
            inSignal = output
            newOutput, finished = IntCode(i, codeList[i], instPointers, phaseSettings[i], firstInput, inSignal)
            # print(phaseSetting, inSignal, output)

            if not finished:
                output = newOutput

        firstInput = False

    if output > maxOutput:
        maxOutput = output
        print(maxOutput)

print(maxOutput)

