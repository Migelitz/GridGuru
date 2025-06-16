# WTF CODE IS THIS? HAHAHAHA I LOVE FLOATY BRAIN👌👌👌

GRID = [[7,8,0,4,0,0,1,2,0],
        [6,0,0,0,7,5,0,0,9],
        [0,0,0,6,0,1,0,7,8],
        [0,0,7,0,4,0,2,6,0],
        [0,0,1,0,5,0,9,3,0],
        [9,0,4,0,6,0,0,0,5],
        [0,7,0,3,0,0,0,1,2],
        [1,2,0,0,0,7,4,0,0],
        [0,4,9,2,0,6,0,0,7]]

def show_board(board):
    for row in range(len(GRID)):
        for col in range(len(GRID)):
            print(board[row][col], end=' ')
        print()
        
def find_empty():
    for row in range(len(GRID)):
        for col in range(len(GRID)):
            if GRID[row][col] == 0:
                return check_row(row, col)
            
def check_row(row, col):
    for test_num in range(1, 9 + 1):
        if test_num not in row:
            return check_col(row, col), check_box(row, col)
        else:
            return find_empty()

def check_col(row, col):
    for cols in len(GRID):
        if GRID[row][cols] == col:
            return find_empty()

def check_box(row, col):
    print("idk, leave me alone.")