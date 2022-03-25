class Solution(object):
    def solve(self, costs):
        N = len(costs)/2
        dp = [[0 for i in range(N+1)] for j in range(N+1)]
        
        i = 1
        while i <= N:
            dp[0][i] = dp[0][i-1] + costs[i-1][1]
            i = i + 1
        i = 1
        while i <= N:
            dp[i][0] = dp[i-1][0] + costs[i-1][0]
            i = i + 1
        
        i = 1
        while i<=N:
            j = 1
            while j<=N:
                dp[i][j] = min(dp[i-1][j]+costs[i+j-1][0], dp[i][j-1]+costs[i+j-1][1])
                j = j + 1
            i = i + 1
        #print dp
        return dp[N][N]
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        return self.solve(costs)
        
        
        
        