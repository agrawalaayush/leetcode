class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        vis = []
        for i in range(m):
            a = []
            for j in range(n):
                a.append(0)
            vis.append(a)
        
        if obstacleGrid[0][0] == 1:
            return 0
        vis[0][0] = 1
        
        for i in range(m):
            for j in range(n):
                if i==0 and j ==0:
                    continue
                if obstacleGrid[i][j] == 1:
                    vis[i][j] = 0
                    continue
                left = 0
                up = 0
                if i-1>=0:
                    left = vis[i-1][j]
                if j-1>=0:
                    up = vis[i][j-1]
                vis[i][j] = left + up
        
        return vis[m-1][n-1]