class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        
        m = len(grid)
        n = len(grid[0])
        total = m*n
        k = k % total
        while k > 0:
            last = grid[m-1][n-1]
            for i in range(m):
                for j in range(n):
                    temp = grid[i][j]
                    grid[i][j] = last
                    last = temp
            k = k - 1
        return grid
        