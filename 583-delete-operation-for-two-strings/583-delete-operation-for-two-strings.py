class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1 = len(word1)
        l2 = len(word2)        
        dp =[]
        for i in range(l1 + 1):
            a = []
            for j in range(l2 + 1):
                a.append(501)
            dp.append(a)
        
        
        for i in range(l1+1):
            for j in range(l2+1):
                if i==0:
                    dp[i][j] = j
                    continue
                if j ==0:
                    dp[i][j] = i
                    continue
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1])
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
        return dp[l1][l2]