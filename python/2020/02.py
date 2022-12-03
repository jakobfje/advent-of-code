

def getLines(path):
    f = open(path)
    lines = f.read().splitlines()
    f.close()
    return lines

def task1(input):
    count = 0

    for line in input:
        print(line)
        countLow = line.split(' ')[0].split('-')[0]
        countHigh = line.split(' ')[0].split('-')[1]
        letter = line.split(' ')[1].split(':')[0]
        password = line.split(' ')[2]

        if password.count(letter) >= int(countLow) and password.count(letter) <= int(countHigh):
            print("Valid")
            count = count+1
        else:
            print("Invalid")
    
    return count

    
def task2(input):
    count = 0

    for line in input:
        print(line)
        indexLow = line.split(' ')[0].split('-')[0]
        indexHigh = line.split(' ')[0].split('-')[1]
        letter = line.split(' ')[1].split(':')[0]
        password = line.split(' ')[2]

        indexLowMatch = password[int(indexLow) - 1] == letter
        indexHighMatch = password[int(indexHigh) - 1] == letter
        if (indexLowMatch and not indexHighMatch) or (not indexLowMatch and indexHighMatch):
            print("Valid")
            count = count+1
        else:
            print("Invalid")
    
    return count

# print(task1(["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]))
# print(task1(getLines("02input.txt")))
print(task2(["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]))
print(task2(getLines("02input.txt")))