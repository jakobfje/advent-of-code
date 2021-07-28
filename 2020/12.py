import pprint
import re

def getLines(path):
    f = open(path)
    lines = f.read().splitlines()
    f.close()
    return lines

def task1(input):
    dir = 0
    ns = 0
    ew = 0
    # print("NS: " + str(ns) + ", WE: " + str(ew))
    for entry in input:
        cmd, nr = re.findall('([A-Z])([0-9]{1,3})', entry)[0]
        nr = int(nr)
        if cmd == 'N':
            ns += nr
        elif cmd == 'S':
            ns -= nr
        elif cmd == 'W':
            ew += nr
        elif cmd == 'E':
            ew -= nr
        elif cmd == 'L':
            dir += nr
            if dir >= 360:
                dir -= 360
        elif cmd == 'R':
            dir -= nr
            if dir < 0:
                dir += 360
        elif cmd == 'F':
            if dir == 0:
                ew -= nr
            elif dir == 90:
                ns += nr
            elif dir == 180:
                ew += nr
            elif dir == 270:
                ns -= nr
            else:
                print("Error F: " + "Dir " + str(dir) + ", Cmd " + cmd + ", Nr " + str(nr))
        else:
            print("Error")
        
        # print("NS: " + str(ns) + ", WE: " + str(ew))

    return abs(ns) + abs(ew)

    
def task2(data):
    nsWay = 1
    ewWay = 10
    nsShip = 0
    ewShip = 0
    print("y: " + str(nsShip) + ", x: " + str(ewShip) + ", y: " + str(nsWay) + ", x: " + str(ewWay))
    for entry in data:
        print(entry)
        cmd, nr = re.findall('([A-Z])([0-9]{1,3})', entry)[0]
        nr = int(nr)
        if cmd == 'N':
            nsWay += nr
        elif cmd == 'S':
            nsWay -= nr
        elif cmd == 'W':
            ewWay -= nr
        elif cmd == 'E':
            ewWay += nr
        elif cmd == 'L':
            print("y: " + str(nsShip) + ", x: " + str(ewShip) + ", y: " + str(nsWay) + ", x: " + str(ewWay))
            tmpNs = nsWay
            tmpEw = ewWay
            if nr == 90:
                nsWay = tmpEw
                ewWay = -tmpNs
            elif nr == 180:
                nsWay = -tmpNs
                ewWay = -tmpEw
            elif nr == 270:
                nsWay = -tmpEw
                ewWay = tmpNs
            else:
                print("Error")
                input()
            print("y: " + str(nsShip) + ", x: " + str(ewShip) + ", y: " + str(nsWay) + ", x: " + str(ewWay))
        elif cmd == 'R':
            print("y: " + str(nsShip) + ", x: " + str(ewShip) + ", y: " + str(nsWay) + ", x: " + str(ewWay))
            tmpNs = nsWay
            tmpEw = ewWay
            if nr == 90:
                nsWay = -tmpEw
                ewWay = tmpNs
            elif nr == 180:
                nsWay = -tmpNs
                ewWay = -tmpEw
            elif nr == 270:
                nsWay = tmpEw
                ewWay = -tmpNs
            else:
                print("Error")
                input()
                
            # print("y: " + str(nsShip) + ", x: " + str(ewShip) + ", y: " + str(nsWay) + ", x: " + str(ewWay))
        elif cmd == 'F':
            nsShip += nr * nsWay
            ewShip += nr * ewWay
        else:
            print("Error")
            input()
        
        # print("y: " + str(nsShip) + ", x: " + str(ewShip) + ", y: " + str(nsWay) + ", x: " + str(ewWay))

    return abs(nsShip) + abs(ewShip)

testInput = ["F10", "N3", "F7", "R90", "F11"]
data = getLines("12input.txt")

print()
print("Task 1")
print("---------")
print("Test: " + str(task1(testInput)))
print("Answer: " + str(task1(data)))
print()
print()
print("Task 2")
print("---------")
print("Test: " + str(task2(testInput)))
print("Answer: " + str(task2(data)))
print()