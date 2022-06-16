class Solution(object):
    def check_palindrome(self, s, i, j):
        while i<j:
            if s[i] == s[j]:
                i = i + 1
                j = j - 1
            else:
                return False
        return True
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        max_result = 1
        result_index = 0
        string_len = len(s)
        #dp = []
        #for i in range(len(s)):
        #    c = []
        #    for j in range(len(s)):
        #        c.append(0)
        #    dp.append(c)
        dp = [[False]*string_len for _ in range(string_len)]
        for i in range(len(s)):
            dp[i][i] = True
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                max_result = 2
                result_index = i
        palin_len = 3
        while palin_len<=string_len:
            initial_index = 0
            while True:
                j_index = initial_index + palin_len-1
                if j_index >= string_len:
                    break
                if s[initial_index] == s[j_index] and dp[initial_index+1][j_index-1] == True:
                    dp[initial_index][j_index] = True
                    if palin_len>max_result:
                        max_result=palin_len
                        result_index = initial_index
                initial_index = initial_index + 1
            palin_len = palin_len + 1
            
        #print(dp)
        result = ""
        count = 0
        while count<max_result:
            result = result + s[result_index]
            result_index = result_index + 1
            count = count + 1
        return result