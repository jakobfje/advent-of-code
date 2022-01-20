f = open('Day8Data.txt', 'r')
code = [int(i) for i in list(f.readline().rstrip())]

width = 25
height = 6
length = width * height

layers = [code[x:x+length] for x in range(0, len(code), length)]
layers.reverse()

img = [2 for i in range(0, length)]

for layer in layers:
    for i in range(0, length):
        if layer[i] != 2:
            img[i] = layer[i]



rows = [img[x:x+width] for x in range(0, len(img), width)]
for row in rows:
    for pixel in row:
        if pixel == 0:
            print(" ", end='')
        else:
            print("o", end='')
    print()


