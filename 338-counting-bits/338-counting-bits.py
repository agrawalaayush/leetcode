class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        res = [0]*100005
        
        i = 0
        res[0] = 0
        res[1] = 1
        res[2] = 1
        res[3] = 2
        
        i = 4
        while i<100005:
            res[i] = res[i/2] + i%2
            i = i + 1
        return res[0:n+1]
        