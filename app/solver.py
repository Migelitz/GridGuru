class SudokuSolver:
    def __init__(self, grid):        
        self.grid = grid
    
    def find_empty(self):
        for row in range(len(self.grid)):
           for col in range(len(self.grid)):
               if self.grid[row][col] == 0:
                   return (row, col)
               
    def valid(self, pos, board):
        
        # Check row
        for col_num in range(len(board[pos[0]])):
            if self.grid[pos[0]][col_num] == col_num and col_num != pos[1]:
                return False
            
        # Check column
        for row_num in range(len(board)):
            if self.grid[row_num][pos[1]] == row_num and row_num != pos[0]:
                return False
            
        # Check box
        row_box = pos[0] - (pos[0] % 3)
        col_box = pos[1] - (pos[1] % 3)
        
        
        for row in range(row_box, col_box + 3):
            for col in range(col_box, col_box + 3):
                if self.grid[row][col] == pass idk