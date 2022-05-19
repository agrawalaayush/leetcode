class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        
        vis = []
        for i in range(m):
            a = []
            for j in range(n):
                a.append(0)
            vis.append(a)
        
        def dfs(matrix, vis, i, j, m, n, depth):
            next_x = [1,0,-1,0]
            next_y = [0,1,0,-1]
            curr_depth = depth
            for k in range(4):
                x = i + next_x[k]
                y = j + next_y[k]
                
                if x>=0 and x<m and y>=0 and y<n:
                    if matrix[x][y] > matrix[i][j]:
                        if vis[x][y]:
                            curr_depth = max(curr_depth, max(depth, vis[x][y] + 1))
                        else:
                            curr_depth = dfs(matrix, vis, x, y, m, n, depth) + 1         
            vis[i][j] = max(vis[i][j], curr_depth)
            dfs_percolate(vis,i,j,vis[i][j])
            return vis[i][j]
        
        def dfs_percolate(vis, i, j, max_value):
            #print(i,j,max_value)
            next_x = [1,0,-1,0]
            next_y = [0,1,0,-1]
            for k in range(4):
                x = i + next_x[k]
                y = j + next_y[k]
                if x>=0 and x<m and y>=0 and y<n:
                    if matrix[x][y] < matrix[i][j]:
                        if vis[x][y] < (max_value + 1):
                            #print(x,y,max_value)
                            vis[x][y] = max_value + 1
                            dfs_percolate(vis, x, y, max_value+1)
            
        for i in range(m):
            for j in range(n):
                vis[i][j] = dfs(matrix, vis, i, j, m, n, 1)
        
        maxi = 0
        for i in range(m):
            #print(vis[i])
            for j in range(n):
                if vis[i][j] > maxi:
                    maxi = vis[i][j]
        return maxi
        
            
            
        