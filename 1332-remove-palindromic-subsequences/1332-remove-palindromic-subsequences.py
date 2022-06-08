class Solution(object):
    def removePalindromeSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        def checkPalindrome(s):
            i = 0 
            j = len(s) - 1
            while i<j:
                if s[i] == s[j]:
                    i = i + 1
                    j = j - 1
                else:
                    return False
            return True
        
        if checkPalindrome(s):
            return 1
        return 2