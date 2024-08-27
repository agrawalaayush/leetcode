class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i = 0 
        while True:
            if i * i > x:
                return i - 1
            i = i + 1
            
        