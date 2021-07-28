import pprint
import re

def getLines(path):
    f = open(path)
    lines = f.read().splitlines()
    f.close()
    return lines


def getSeatIds(input):
    seatIds = []

    for line in input:
        # line = line.replace('B', '1').replace('F', '0').replace('R', '1').replace('L', '0')
        # seatId = int(line[0:7], 2) * 8 + int(line[7:], 2)
        seat = [{'row':x[0].replace('B', '1').replace('F', '0'), 'col':x[1].replace('R', '1').replace('L', '0')} for x in re.findall('([BF]{7})([RL]{3})', line)][0]
        seatId = int(seat['row'], 2) * 8 + int(seat['col'], 2)
        seatIds.append(seatId)

    return seatIds


def task1(input):        
    return max(getSeatIds(input))

    
def task2(input):
    seatIds = getSeatIds(input)
    seats = range(max(seatIds)+1)
    
    return max([x for x in seats if x not in seatIds])

input = getLines("05input.txt")

print("Answer 1: " + str(task1(["BFFFBBFRRR",
    "FFFBBBFRRR",
    "BBFFBBFRLL"])))
print("Answer 1: " + str(task1(input)))
print()
print("Answer 2: " + str(task2(input)))