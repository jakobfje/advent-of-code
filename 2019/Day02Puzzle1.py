codeInit = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,5,23,1,23,9,27,2,27,6,31,1,31,6,35,2,35,9,39,1,6,39,43,2,10,43,47,1,47,9,51,1,51,6,55,1,55,6,59,2,59,10,63,1,6,63,67,2,6,67,71,1,71,5,75,2,13,75,79,1,10,79,83,1,5,83,87,2,87,10,91,1,5,91,95,2,95,6,99,1,99,6,103,2,103,6,107,2,107,9,111,1,111,5,115,1,115,6,119,2,6,119,123,1,5,123,127,1,127,13,131,1,2,131,135,1,135,10,0,99,2,14,0,0]
# code = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,5,23,1,23,9,27,2,27,6,31,1,31,6,35,2,35,9,39,1,6,39,43,2,10,43,47,1,47,9,51,1,51,6,55,1,55,6,59,2,59,10,63,1,6,63,67,2,6,67,71,1,71,5,75,2,13,75,79,1,10,79,83,1,5,83,87,2,87,10,91,1,5,91,95,2,95,6,99,1,99,6,103,2,103,6,107,2,107,9,111,1,111,5,115,1,115,6,119,2,6,119,123,1,5,123,127,1,127,13,131,1,2,131,135,1,135,10,0,99,2,14,0,0]
# code = [1,0,0,0,99]
# code = [2,3,0,3,99]
# code = [2,4,4,5,99,0]
# code = [1,1,1,4,99,5,6,0,99]

def IntCode(code, noun, verb):
    code[1] = noun
    code[2] = verb
    opCodeAddr = 0
    opCode = code[opCodeAddr]

    while True:
        opCode = code[opCodeAddr]

        if (opCode == 0):
            print("Error")
            return 0
        
        if (opCode == 99):
            print("Finished")
            break

        if opCode != 99:
            data1Addr = code[opCodeAddr + 1]
            data2Addr = code[opCodeAddr + 2]
            storeAddr = code[opCodeAddr + 3]

            if (data1Addr > len(code)):
                print(data1Addr)
                print("Addr out of range, data1")
                return 0

            if (data2Addr > len(code)):
                print(data2Addr)
                print("Addr out of range, data2")
                return 0

            if (storeAddr > len(code)):
                print(storeAddr)
                print("Addr out of range, store")
                return 0

            if (opCode == 1):
                code[storeAddr] = code[data1Addr] + code[data2Addr]
            if (opCode == 2):
                code[storeAddr] = code[data1Addr] * code[data2Addr]

        opCodeAddr = opCodeAddr + 4
        
    return(code[0])

noun = 0
verb = 0

for i in range(0, 100, 1):
    for j in range(0, 100, 1):
        code = codeInit.copy()
        returnCode = IntCode(code, i, j)
        print(i, j, returnCode)
        if returnCode == 19690720:
            noun = i
            verb = j
            
            print(noun)
            print(verb)
            print(100 * noun + verb)
            exit()

        if returnCode == 0:
            exit()
