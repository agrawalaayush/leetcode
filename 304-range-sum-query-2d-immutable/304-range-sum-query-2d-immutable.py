class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        self.m = len(matrix)
        self.n = len(matrix[0])
        
        self.col_major = [[0 for i in range(self.n)] for j in range(self.m)]
        self.row_major = [[0 for i in range(self.n)] for j in range(self.m)]
        self.sum_major = [[0 for i in range(self.n)] for j in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                if j != 0:
                    self.col_major[i][j] = self.matrix[i][j] + self.col_major[i][j-1]
                    self.sum_major[i][j] = self.matrix[i][j] + self.sum_major[i][j-1]
                else:
                    self.col_major[i][j] = self.matrix[i][j]
                    self.sum_major[i][j] = self.matrix[i][j]
                
                if i!=0:
                    self.row_major[i][j] = self.matrix[i][j] + self.row_major[i-1][j]
                else:
                    self.row_major[i][j] = self.matrix[i][j]
        for i in range(self.m):
            for j in range(self.n):
                if i!=0:
                    self.sum_major[i][j] = self.sum_major[i][j] + self.sum_major[i-1][j]
        
        
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        #print(self.sum_major)
        #print(self.row_major)
        #print(self.col_major)
        total_sum = self.sum_major[row2][col2]
        
        rem_sum = 0
        if row1==0 and col1==0:
            return total_sum
        
        if row1>=1 and col1>=1:
            rem_sum = self.sum_major[row1-1][col1-1]
        
        row_sum = 0
        col_sum = 0
        if col1>0:
            i = row1
            while i<=row2:
                row_sum = row_sum + self.col_major[i][col1-1]
                i = i + 1
        
        
        if row1>0:
            i = col1
            while i<=col2:
                col_sum = col_sum + self.row_major[row1-1][i]
                i = i + 1
        
        #print(total_sum)
        #print(rem_sum)
        #print(row_sum)
        #print(col_sum)
        return total_sum - (rem_sum + row_sum + col_sum)

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)