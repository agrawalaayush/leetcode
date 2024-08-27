class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        ch = 0
        orig = x
        while x>0:
            ch  =  ch * 10 + x%10
            x = x/10
        print ch
        if ch == orig:
            return True
        return False
        