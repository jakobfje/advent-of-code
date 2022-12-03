import pprint

f = open("01input.txt", "r")
input = f.read().split('\n')

# pprint.pprint(input)
product = 0
A = 0
B = 0
C = 0

for i in input:
    if not i == '':
        for j in input:
            if not j == '':
                for k in input:
                    if not k == '':
                        summ = int(i) + int(j) + int(k)
                        
                        if summ == 2020:
                            A = i
                            B = j
                            C = k
                            product = int(i) * int(j) * int(k)
                            print("Prod = " + str(product))

print(A)
print(B)
print(C)
print("Prod = " + str(product))