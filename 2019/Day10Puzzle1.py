import math

map = []

dataFile = open('Day10Data.txt', 'r')
line = dataFile.readline()
while line:
    line = line.rstrip()
    map.append(line)
    line = dataFile.readline()

x = 0
y = 0
ast = []

for line in map:
    x = 0
    for dot in line:
        if dot == '#':
            ast.append([x, y])
            # print("Asteroid at: x=", x, ", y=", y)
        x += 1
    y += 1

print(ast)


maxCount = 0
maxAst = []

for astA in ast:
    angles = []
    count = 0

    for astB in ast:
        if astA != astB:
            angle = math.atan2(astB[1] - astA[1], astB[0] - astA[0])
            if angle not in angles:
                count += 1
                angles.append(angle)
    
    if count > maxCount:
        maxCount = count
        maxAst = astA
        print(astA, count)

print()
print(maxAst, maxCount)


