f = open('Day8Data.txt', 'r')
code = [int(i) for i in list(f.readline().rstrip())]

width = 25
height = 6
length = width * height

layers = [code[x:x+length] for x in range(0, len(code), length)]

minZeroCount = length
layerIndex = 0
i = 0

for layer in layers:
    zeroCount = layer.count(0)
    if zeroCount < minZeroCount:
        minZeroCount = zeroCount
        layerIndex = i
    i += 1

print(layerIndex)
print(minZeroCount)
print(len(layers[layerIndex]))
print(layers[layerIndex])

print(layers[layerIndex].count(1) * layers[layerIndex].count(2))