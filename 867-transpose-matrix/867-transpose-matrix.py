class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        
        m = len(matrix)
        n = len(matrix[0])
        
        ans = []
        for i in range(n):
            a = []
            for j in range(m):
                a.append(0)
            ans.append(a)
        
        for i in range(m):
            for j in range(n):
                ans[j][i] = matrix[i][j]
        return ans