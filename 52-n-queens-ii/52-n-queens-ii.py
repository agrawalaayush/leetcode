class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def check_negative_diagonal(matrix, row, col,n):
            i = row 
            j = col
            while i<n and j>=0:
                if matrix[i][j] == "Q":
                    return False
                i = i + 1
                j = j - 1
            
            i = row 
            j = col
            while i>=0 and j<n:
                if matrix[i][j] == "Q":
                    return False
                i = i - 1
                j = j + 1
            return True
        def check_positive_diagonal(matrix, row, col,n):
            i = row 
            j = col
            while i<n and j<n:
                if matrix[i][j] == "Q":
                    return False
                i = i + 1
                j = j + 1
            i = row 
            j = col
            while i>=0 and j>=0:
                if matrix[i][j] == "Q":
                    return False
                i = i - 1
                j = j - 1
            return True
        def check_col(matrix, col, n):
            i = 0 
            while i<n:
                if matrix[i][col] == "Q":
                    return False
                i = i + 1
            return True
        
        def check_row(matrix, row, n):
            i = 0
            while i<n:
                if matrix[row][i] == "Q":
                    return False
                i = i + 1
            return True
            
        def isValid(matrix, row, col, n):
            return check_row(matrix, row, n) and check_col(matrix, col, n) and check_positive_diagonal(matrix, row, col, n) and check_negative_diagonal(matrix, row, col, n)
            
        def backTrack(matrix, row, col, queens, n):
            #print(matrix, row, col, queens)
            if queens == 0:
                self.result.append(matrix)
                return    
            if isValid(matrix, row, col, n):
                matrix[row][col] = "Q"
                queens = queens - 1
                if queens == 0:
                    import copy
                    self.result.append(copy.deepcopy(matrix)) 
                if (row+1) < n: 
                    for j in range(n):
                        if matrix[row+1][j] == ".":
                            check = backTrack(matrix, row+1, j, queens, n)
                matrix[row][col] = "."
                queens = queens + 1
        
        self.result = []
        for j in range(n):
            matrix = []
            for ii in range(n):
                aa = []
                for jj in range(n):
                    aa.append(".")
                matrix.append(aa)
            backTrack(matrix, 0, j, n, n)
            
        res = []
        for ans in self.result:
            m = []
            for i in range(n):
                s = ""
                for j in range(n):
                    s = s + ans[i][j]
                m.append(s)
            res.append(m)
        return len(res)