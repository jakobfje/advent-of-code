# 278384-824795

count = 0

for nr in range(278384, 824795 + 1):
    st = str(nr)
    if (st[0] == st[1]) or (st[1] == st[2]) or (st[2] == st[3]) or (st[3] == st[4]) or (st[4] == st[5]):
        # print("Two adjacent digits similar.")

        largerSet = True

        if st[0] == st[1] and st[1] != st[2]:
            largerSet = False

        if st[1] == st[2] and st[0] != st[1] and st[2] != st[3]:
            largerSet = False
        
        if st[2] == st[3] and st[1] != st[2] and st[3] != st[4]:
            largerSet = False
        
        if st[3] == st[4] and st[2] != st[3] and st[4] != st[5]:
            largerSet = False
        
        if st[4] == st[5] and st[3] != st[4]:
            largerSet = False

        if (largerSet == False) and (st[0] <= st[1]) and (st[1] <= st[2]) and (st[2] <= st[3]) and (st[3] <= st[4]) and (st[4] <= st[5]):
            # print("Never decreases.")
            print(nr)
            count = count + 1

print(count)

# 603