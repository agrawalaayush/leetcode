class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        m = len(board)
        n = len(board[0])
        
        next_state = []
        for i in range(m):
            a = []
            for j in range(n):
                a.append(0)
            next_state.append(a)
        
        x = [1, 1, 1, 0, -1, -1, -1, 0]
        y = [1, 0, -1, -1, -1, 0, 1, 1]
        
        for i in range(m):
            for j in range(n):
                alive = 0
                dead = 0
                for k in range(8):
                    next_x = i + x[k]
                    next_y = j + y[k]
                    
                    if next_x>=0 and next_x<m and next_y>=0 and next_y<n:
                        if board[next_x][next_y] in [1,3]:
                            alive = alive + 1
                        else:
                            dead = dead + 1
                
                
                if board[i][j] == 1:
                    if alive in [2,3]:
                        board[i][j] = 3
                    else:
                        board[i][j] = 1
                else:
                    if alive in [3]:
                        board[i][j] = 2
        for i in range(m):
            for j in range(n):
                if board[i][j] in [2,3]:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
        print(board)
        