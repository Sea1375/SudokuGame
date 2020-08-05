import copy

#This is color sorting.
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
            if i != temp[0] and i != temp[6] and i != temp[7] and i != temp[3] and i != temp[5]:
                temp[index] = i
                colorPair.append(temp.copy())

#color and number sorting

input = [[0 for x in range(9)] for y in range(9)]
color = [[0 for x in range(9)] for y in range(9)]
row_up = [[0 for x in range(5)] for y in range(10)]
row_down = [[0 for x in range(5)] for y in range(10)]
col_left = [[0 for x in range(5)] for y in range(10)]
col_right = [[0 for x in range(5)] for y in range(10)]

def printColor(center, number):
    
    center_y = (center % 3) * 3 + 1
    center_x = int(center / 3) * 3 + 1
    dif_y = [0, -1, 0, 1, -1, 1, -1, 0, 1]
    dif_x = [0, -1, -1, -1, 0, 0, 1, 1, 1]

    for i in range(0, 9):
        color[center_x + dif_x[i]][center_y + dif_y[i]] = colorPair[number][i]

def conditionZero():
    for i in range(0, 3):
        for j in range(0, 3):
            row_up[input[i][j]][color[i][j]] = 1
            col_left[input[i][j]][color[i][j]] = 1

def freeZero():
    row_up = [[0 for x in range(5)] for y in range(10)]
    row_down = [[0 for x in range(5)] for y in range(10)]
    col_left = [[0 for x in range(5)] for y in range(10)]
    col_right = [[0 for x in range(5)] for y in range(10)]
    

def conditionOne():
    for i in range(0, 3):
        for j in range(3, 6):
            if row_up[input[i][j]][color[i][j]] == 1:
                return False
    for i in range(0, 3):
        for j in range(3, 6):
            row_up[input[i][j]][color[i][j]] = 1

    col_left[input[0][3]][color[0][3]] = 1
    col_left[input[1][3]][color[1][3]] = 1
    col_left[input[2][3]][color[2][3]] = 1
    col_right[input[0][5]][color[0][3]] = 1
    col_right[input[1][5]][color[1][3]] = 1
    col_right[input[2][5]][color[2][3]] = 1
    return True

def freeOne():
    for i in range(0, 3):
        for j in range(3, 6):
            row_up[input[i][j]][color[i][j]] = 0
    
def conditionTwo():
    for i in range(0, 3):
        for j in range(6, 9):
            if row_up[input[i][j]][color[i][j]] == 1:
                return False
    for i in range(0, 3):
        for j in range(6, 9):
            row_up[input[i][j]][color[i][j]] = 1
            col_right[input[i][j]][color[i][j]] = 1
    return True

def freeTwo():
    for i in range(0, 3):
        for j in range(6, 9):
            row_up[input[i][j]][color[i][j]] = 0
            col_right[input[i][j]][color[i][j]] = 0

def conditionThree():
    if row_up[input[3][0]][color[3][0]] == 1 or row_up[input[3][1]][color[3][1]] == 1 or row_up[input[3][2]][color[3][2]] == 1:
        return False
    for i in range(3, 6):
        for j in range(0, 3):
            if col_left[input[i][j]][color[i][j]] == 1:
                return False
    
    row_up[input[3][0]][color[3][0]] = 1
    row_up[input[3][1]][color[3][1]] = 1
    row_up[input[3][2]][color[3][2]] = 1
    row_down[input[5][0]][color[5][0]] = 1
    row_down[input[5][1]][color[5][1]] = 1
    row_down[input[5][2]][color[5][2]] = 1
    
    for i in range(3, 6):
        for j in range(0, 3):
            col_left[input[i][j]][color[i][j]] = 1
    return True

def freeThree():
    row_up[input[3][0]][color[3][0]] = 0
    row_up[input[3][1]][color[3][1]] = 0
    row_up[input[3][2]][color[3][2]] = 0
    row_down[input[5][0]][color[5][0]] = 0
    row_down[input[5][1]][color[5][1]] = 0
    row_down[input[5][2]][color[5][2]] = 0
    for i in range(3, 6):
        for j in range(0, 3):
            col_left[input[i][j]][color[i][j]] = 0

def conditionFour():
    if row_up[input[3][3]][color[3][3]] == 1 or row_up[input[3][4]][color[3][4]] == 1 or row_up[input[3][5]][color[3][5]] == 1:
        return False
    if row_down[input[5][3]][color[5][3]] == 1 or row_down[input[5][4]][color[5][4]] == 1 or row_down[input[5][5]][color[5][5]] == 1:
        return False
    if col_left[input[3][3]][color[3][3]] == 1 or col_left[input[4][3]][color[4][3]] == 1 or col_left[input[5][3]][color[5][3]] == 1:
        return False
    if col_right[input[3][5]][color[3][5]] == 1 or col_right[input[4][5]][color[4][5]] == 1 or col_right[input[5][5]][color[5][5]] == 1:
        return False
    
    row_up[input[3][3]][color[3][3]] = 1
    row_up[input[3][4]][color[3][4]] = 1
    row_up[input[3][5]][color[3][5]] = 1
    
    row_down[input[5][3]][color[5][3]] = 1
    row_down[input[5][4]][color[5][4]] = 1
    row_down[input[5][5]][color[5][5]] = 1

    col_left[input[3][3]][color[3][3]] = 1
    col_left[input[4][3]][color[4][3]] = 1
    col_left[input[5][3]][color[5][3]] = 1
    
    col_right[input[3][5]][color[3][5]] = 1
    col_right[input[4][5]][color[4][5]] = 1
    col_right[input[5][5]][color[5][5]] = 1

    return True

def freeFour():
    row_up[input[3][3]][color[3][3]] = 0
    row_up[input[3][4]][color[3][4]] = 0
    row_up[input[3][5]][color[3][5]] = 0
    
    row_down[input[5][3]][color[5][3]] = 0
    row_down[input[5][4]][color[5][4]] = 0
    row_down[input[5][5]][color[5][5]] = 0

    col_left[input[3][3]][color[3][3]] = 0
    col_left[input[4][3]][color[4][3]] = 0
    col_left[input[5][3]][color[5][3]] = 0
    
    col_right[input[3][5]][color[3][5]] = 0
    col_right[input[4][5]][color[4][5]] = 0
    col_right[input[5][5]][color[5][5]] = 0


colorname = ['n', 'r', 'g', 'b', 'y']
count = 0

#This is number sorting

def print_grid(arr): 
    for i in range(9): 
        for j in range(9): 
            print("" + str(arr[i][j]), end = " ") 
        print ()
    print()

def find_empty_location(arr, l): 
    for row in range(9): 
        for col in range(9): 
            if(arr[row][col]== 0): 
                l[0]= row 
                l[1]= col 
                return True
    return False

def used_in_row(arr, row, num): 
    for i in range(9): 
        if(arr[row][i] == num): 
            return True
    return False
  
def used_in_col(arr, col, num): 
    for i in range(9): 
        if(arr[i][col] == num): 
            return True
    return False
  

def used_in_box(arr, row, col, num): 
    for i in range(3): 
        for j in range(3): 
            if(arr[i + row][j + col] == num): 
                return True
    return False
  

def check_location_is_safe(arr, row, col, num): 
    return not used_in_row(arr, row, num) and not used_in_col(arr, col, num) and not used_in_box(arr, row - row % 3, col - col % 3, num) 
  
def solve_sudoku(arr): 
    l =[0, 0] 
    if(not find_empty_location(arr, l)):
        input = arr.copy()
        print_grid(input)
        for block_zero in range(0, len(colorPair)):
            printColor(0, block_zero)
            conditionZero()
            for block_one in range(0, len(colorPair)):
                printColor(1, block_one)
                if conditionOne() == True:
                    for block_two in range(0, len(colorPair)):
                        printColor(2, block_two)
                        if conditionTwo() == True:
                            print("Found")
                            break
                            freeTwo()
                    freeOne()
            freeZero()
    row = l[0] 
    col = l[1] 
      
    for num in range(1, 10): 
        if(check_location_is_safe(arr, row, col, num)): 
            arr[row][col]= num 
            if(solve_sudoku(arr)): 
                return True
            arr[row][col] = 0
    return False 

if __name__ == '__main__':
    push(0)
    grid =[[0 for x in range(9)]for y in range(9)] 
    if(solve_sudoku(grid)): 
        print("success")
    else: 
        print("No solution exists")







