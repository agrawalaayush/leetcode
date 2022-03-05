class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = [0]*10005
        dp = [0]*10005
        for num in nums:
            count[num] = count[num] + 1
        
        
        dp[0] = 0
        dp[1] = count[1]
        
        i = 2
        while i<10005:
            incl = 0
            if count[i] != 0:
                incl = count[i]*i + dp[i-2]
            excl = dp[i-1]
            
            dp[i] = max(incl, excl)
            i = i + 1
        #print(dp[0:10])
        return dp[10004]