class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def isPredecessor(word1, word2):
            
            l1 = len(word1)
            l2 = len(word2)
            diff = 0
            i = 0
            j = 0
            while i<l1 and j<l2:
                if word1[i] == word2[j]:
                    i = i + 1
                    j = j + 1
                else:
                    j = j + 1
                    diff = diff + 1
            
            diff = diff + (l1-i) + (l2-j)
            if diff==1:
                #print(word1, " ", word2, " ", i, " ", j," ", diff)
                return True
            return False
        
        le = len(words)
        dp = [1]*le
        
        words = sorted(words , key = len)
        #print(words)
        i = 1
        ans = 1
        while i<le:
            j = 0
            while j<i:
                if len(words[j]) + 1 == len(words[i]) and isPredecessor(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j]+1)
                    ans = max(ans, dp[i])
                j = j + 1
            i = i + 1
        return ans