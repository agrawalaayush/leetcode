class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        
        dp = []
        for i in range(105):
            x = []
            for j in range(105):
                x.append(0)
            dp.append(x)
        
        dp[0][0] = 0
        l = []
        for s in strs:
            a = sorted(s)
            l.append("".join(a))
        lst2 = sorted(l, key=len)
        def countZero(s):
            count = 0
            i = 0
            while i<len(s):
                if s[i] == "1":
                    break
                count = count + 1
                i = i + 1
            return count
        def printDP(dp, m, n):
            print("----------DP Start-----")
            for i in range(m+1):
                for j in range(n+1):
                    print dp[i][j]
                print("**************----------*********")
            print("----------DP End-----")
            
            
        for s in lst2:
            cz = countZero(s)
            c1 = len(s) - cz
            m1 = m
            while m1>=cz:
                n1 = n 
                while n1>=c1:
                    if m1>=cz and n1>=c1:
                        dp[m1][n1] = max(dp[m1][n1], dp[m1-cz][n1-c1]+1)
                    
                    n1 = n1 - 1
                m1 = m1 - 1
                        
        return dp[m][n]
        
         
        
        