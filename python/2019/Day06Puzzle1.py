map = []

dataFile = open('Day6Data.txt', 'r')
line = dataFile.readline()
while line:
    line = line.rstrip()
    map.append(line)
    line = dataFile.readline()
print(map)

# map = ['COM)B','C)D','B)C','D)E','E)F','B)G','G)H','D)I','E)J','J)K','K)L','K)YOU','I)SAN']

def updateChildren(objects, children, count, objIndex, addCount):
    for child in children[objIndex]:
        childIndex = objects.index(child)
        count[childIndex] += (1 + addCount)
        updateChildren(objects, children, count, childIndex, addCount)

objects = []
children = []
count = []

for line in map:
    newOrbit = line.split(')')
    # print(newOrbit)

    if not (newOrbit[0] in set(objects)):
        objects.append(newOrbit[0])
        children.append([])
        count.append(0)

    if not (newOrbit[1] in set(objects)):
        objects.append(newOrbit[1])
        children.append([])
        count.append(0)

    children[objects.index(newOrbit[0])].append(newOrbit[1])
    count[objects.index(newOrbit[1])] += (1 + count[objects.index(newOrbit[0])])

    # Update children
    updateChildren(objects, children, count, objects.index(newOrbit[1]), count[objects.index(newOrbit[0])])


    # for x in range(0, len(objects)):
    #     print(objects[x], children[x], count[x])
    # input()

# print(sum(count))

startIndex = objects.index('COM')

def getPath(index, goal):
    if children[index] == []:
        if objects[index] == goal:
            return True, [objects[index]]
        else:
            return False, []
    else:
        goalFound = False
        path = []

        for child in children[index]:
            goalFound, path = getPath(objects.index(child), goal)
            if goalFound:
                break
        path.append(objects[index])
        # print(objects[index], children[index], path)
        return goalFound, path

x, youPath = getPath(startIndex, 'YOU')
# print(youPath)
y, sanPath = getPath(startIndex, 'SAN')
# print(sanPath)

for i in range(0, max(len(youPath), len(sanPath))):
    if youPath[-1] == sanPath[-1]:
        youPath.remove(youPath[-1])
        sanPath.remove(sanPath[-1])
    else:
        break

print(youPath)
print(sanPath)

print(1 + len(youPath) + len(sanPath) - 3)