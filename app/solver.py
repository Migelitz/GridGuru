class SudokuSolver:
    def __init__(self, grid):        
        self.grid = grid
    
    def find_empty(self):
        for row in range(len(self.grid)):
           for col in range(len(self.grid)):
               if self.grid[row][col] == 0:
                   return (row, col)
        
        return None # If no zeroes (0) found
               
    def valid(self, num, pos, board):
        
        # Check column
        for row_num in range(len(board)):
            if self.grid[row_num][pos[1]] == num and row_num != pos[0]: # row_num != pos[0] means the column is not equal to the column were placing. Note: Tuple received form find_empty()
                return False    
        
        # Check row
        for col_num in range(len(board[pos[0]])):
            if self.grid[pos[0]][col_num] == num and col_num != pos[1]: # col_num != pos[1] means the column is not equal to the row were placing. Note: Tuple received form find_empty()
                return False
            
        # Check box
        row_box = pos[0] - (pos[0] % 3)
        col_box = pos[1] - (pos[1] % 3)
            
        for row in range(row_box, col_box + 3):
            for col in range(col_box, col_box + 3):
                if self.grid[row][col] == num and (row, col) != pos:
                    return False
        
        return True
    
    def solve(self):
        find = self.find_empty()
        if not find: # This will receive None from find_empty()
            return True  # This means all boxes are filled and solution is complete
        else:
            row, col = find # Else save the row and column on find_empy() to these variable
            
        for test in range(1, len(self.grid) + 1):
            if self.valid(test, (row, col), self.grid):
                self.grid[row][col] = test
                
                if self.solve(self.grid): # Recursively call the solve(); this works even inside of if statement to test if we will receive True or False
                    return True # If the line 39 become True and receive True, this will run and return True to the caller which tells that it is solved
                
                self.grid[row][col] = 0 # After saving, reset the test value then...
                
        return False # Return False and return to the last call stack (Below for explanation)
    
    # The last call stack is (0,4) and current iteration is (0,5), if no valid, we weill return False to the last caller from (0,4) then process continues. For test, look for test file (Migelitz hold it for example oke? Its on .gitignore lol)