class Solution(object):
    def isValidRow(self, board, row, val):
        count = 0
        for i in range(9):
            if board[row][i] == val:
                count = count + 1
        if count>1:
            return False
        return True
    
    def isValidCol(self, board, col, val):
        count = 0
        for i in range(9):
            if board[i][col] == val:
                count = count + 1
        if count>1:
            return False
        return True
    
    def isValidBox(self, board, row, col, val):
        box_row = row/3
        box_col = col/3
        start_row = box_row * 3
        start_col = box_col * 3
        #print(start_row, start_col, box_row, box_col, row, col)
        i = start_row 
        count = 0
        while i<(start_row+3):
            j = start_col
            while j < (start_col+3):
                #if start_col == 3:
                #    print(board[i][j])
                if board[i][j] == val:
                    count = count + 1
                j = j + 1
            i = i + 1
        if count >1:
            return False
        return True
    
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    check = self.isValidRow(board, i, board[i][j])
                    check2 = self.isValidCol(board, j, board[i][j])
                    check3 = self.isValidBox(board, i, j, board[i][j])
                    #print(check, check2, check3, i, j)
                    if not (check and check2 and check3):
                        return False
        
        return True
                    
        