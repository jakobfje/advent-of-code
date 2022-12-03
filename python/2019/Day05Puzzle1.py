codeInit = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,5,23,1,23,9,27,2,27,6,31,1,31,6,35,2,35,9,39,1,6,39,43,2,10,43,47,1,47,9,51,1,51,6,55,1,55,6,59,2,59,10,63,1,6,63,67,2,6,67,71,1,71,5,75,2,13,75,79,1,10,79,83,1,5,83,87,2,87,10,91,1,5,91,95,2,95,6,99,1,99,6,103,2,103,6,107,2,107,9,111,1,111,5,115,1,115,6,119,2,6,119,123,1,5,123,127,1,127,13,131,1,2,131,135,1,135,10,0,99,2,14,0,0]
# code = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,5,23,1,23,9,27,2,27,6,31,1,31,6,35,2,35,9,39,1,6,39,43,2,10,43,47,1,47,9,51,1,51,6,55,1,55,6,59,2,59,10,63,1,6,63,67,2,6,67,71,1,71,5,75,2,13,75,79,1,10,79,83,1,5,83,87,2,87,10,91,1,5,91,95,2,95,6,99,1,99,6,103,2,103,6,107,2,107,9,111,1,111,5,115,1,115,6,119,2,6,119,123,1,5,123,127,1,127,13,131,1,2,131,135,1,135,10,0,99,2,14,0,0]
# code = [1,0,0,0,99]
# code = [2,3,0,3,99]
# code = [2,4,4,5,99,0]
# code = [1,1,1,4,99,5,6,0,99]

def parseInstruction(instr):
    opCode = instr[-1:]
    return 0

def IntCode(code):
    instrAddr = 0

    while True:
        instr = code[instrAddr]
        instrList = parseInstruction(str(instr))

        if (opCode == 0):
            print("Error")
            exit()
        elif opCode == 1:
            # Add
            data1Addr = code[opCodeAddr + 1]
            data2Addr = code[opCodeAddr + 2]
            storeAddr = code[opCodeAddr + 3]
            code[storeAddr] = code[data1Addr] + code[data2Addr]
        elif opCode == 2:
            # Multiply
            data1Addr = code[opCodeAddr + 1]
            data2Addr = code[opCodeAddr + 2]
            storeAddr = code[opCodeAddr + 3]
            code[storeAddr] = code[data1Addr] * code[data2Addr]
        elif opCode == 3:
            # Input
        elif opCode == 4:
            # Output
        if (opCode == 99):
            print("Finished")
            break

        opCodeAddr = opCodeAddr + 4
        
    return(code[0])






IntCode(code, i, j)
