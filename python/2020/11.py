import pprint
import re

def getLines(path):
    f = open(path)
    lines = f.read().splitlines()
    f.close()
    return lines

def getAdjSeats(rIdx, cIdx, rLen, cLen):
    adjSeats = [[rIdx - 1, cIdx - 1],
        [rIdx - 1, cIdx],
        [rIdx - 1, cIdx + 1],
        [rIdx, cIdx - 1],
        [rIdx, cIdx + 1],
        [rIdx + 1, cIdx - 1],
        [rIdx + 1, cIdx],
        [rIdx + 1, cIdx + 1]]

    adjSeats = [x for x in adjSeats if (x[0] >= 0) and (x[0] < rLen) and (x[1] >= 0) and (x[1] < cLen)]
    return adjSeats 

def updSeats(input):
    colLen = len(input[0])
    rowLen = len(input)
    lastState = input.copy()
    for rIdx in range(rowLen):
        for cIdx in range(colLen):
            adjSeats = getAdjSeats(rIdx, cIdx, rowLen, colLen)
            occupiedCnt = 0
            for seat in adjSeats:
                if lastState[seat[0]][seat[1]] == '#':
                    occupiedCnt += 1
            if occupiedCnt == 0 and lastState[rIdx][cIdx] == 'L':
                input[rIdx] = input[rIdx][:cIdx] + "#" + input[rIdx][cIdx+1:]  
            if occupiedCnt > 3 and lastState[rIdx][cIdx] == '#':
                input[rIdx] = input[rIdx][:cIdx] + "L" + input[rIdx][cIdx+1:]  

    return input

def getOccSeatsInSight(input, rIdx, cIdx, rLen, cLen):
    directions = [[-1, -1], [-1, 0], [-1, 1],
                  [0,  -1],          [0,  1],
                  [1,  -1], [1,  0], [1,  1]]

    cnt = 0
    for dir in directions:
        xy = [rIdx + dir[0], cIdx + dir[1]]
        while (xy[0] >= 0) and (xy[0] < rLen) and (xy[1] >= 0) and (xy[1] < cLen):
            if input[xy[0]][xy[1]] == '#':
                # if rIdx==0 and cIdx==2:
                #     print("Found at: " + str(xy[0]) + ", " + str(xy[1]))
                cnt += 1
                break
            if input[xy[0]][xy[1]] == 'L':
                break
            xy = [xy[0] + dir[0], xy[1] + dir[1]]

    return cnt

    
def updSeats2(input):
    colLen = len(input[0])
    rowLen = len(input)
    lastState = input.copy()
    for rIdx in range(rowLen):
        for cIdx in range(colLen):
            occupiedCnt = getOccSeatsInSight(lastState, rIdx, cIdx, rowLen, colLen)
            if occupiedCnt == 0 and lastState[rIdx][cIdx] == 'L':
                input[rIdx] = input[rIdx][:cIdx] + "#" + input[rIdx][cIdx+1:]  
            if occupiedCnt > 4 and lastState[rIdx][cIdx] == '#':
                input[rIdx] = input[rIdx][:cIdx] + "L" + input[rIdx][cIdx+1:]  

    return input


def task1(input):
    output = []
    while input != output:
        if output != []:
            input = output
        output = updSeats(input.copy())

    return sum([x.count('#') for x in output])

    
def task2(input):
    output = []
    # print(input)
    while input != output:
        if output != []:
            input = output
        output = updSeats2(input.copy())
        # print(output)

    return sum([x.count('#') for x in output])

testInput = ["L.LL.LL.LL",
    "LLLLLLL.LL",
    "L.L.L..L..",
    "LLLL.LL.LL",
    "L.LL.LL.LL",
    "L.LLLLL.LL",
    "..L.L.....",
    "LLLLLLLLLL",
    "L.LLLLLL.L",
    "L.LLLLL.LL"]
input = getLines("11input.txt")

print()
print("Task 1")
print("---------")
print("Test: " + str(task1(testInput)))
# print("Answer: " + str(task1(input)))
print()
print()
print("Task 2")
print("---------")
print("Test: " + str(task2(testInput)))
print("Answer: " + str(task2(input)))
print()