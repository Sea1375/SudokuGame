colorPair = []
temp = [0,0,0,0,0,0,0,0,0]
def push(index):
    global colorPair
    if index == 0:
        for i in range(1, 5):
            temp[index] = i
            push(index + 1)
    if index == 1:
        for i in range(1, 5):
            if i != temp[0]:
                temp[index] = i
                push(index + 1)
    if index == 2:
        for i in range(1, 5):
            if i != temp[0] and i != temp[1]:
                temp[index] = i
                push(index + 1)
    if index == 3:
        for i in range(1, 5):
            if i != temp[0] and i != temp[1] and i != temp[2]:
                temp[index] = i
                push(index + 1)
    if index == 4:
        for i in range(1, 5):
            if i != temp[0] and i != temp[1]:
                temp[index] = i
                push(index + 1)
    if index == 5:
        for i in range(1, 5):
            if i != temp[0] and i != temp[3]:
                temp[index] = i
                push(index + 1)
    if index == 6:
        for i in range(1, 5):
            if i != temp[0] and i != temp[1] and i != temp[4]:
                temp[index] = i
                push(index + 1)
    if index == 7:
        for i in range(1, 5):
            if i != temp[0] and i != temp[6]:
                temp[index] = i
                push(index + 1)
    if index == 8:
        for i in range(1, 5):
            if i != temp[0] and i != temp[6] and i != temp[7]:
                temp[index] = i
                colorPair.append(temp.copy())

if __name__ == '__main__':
    push(0)
    for x in colorPair:
        print(x)
    print(len(colorPair))
    
