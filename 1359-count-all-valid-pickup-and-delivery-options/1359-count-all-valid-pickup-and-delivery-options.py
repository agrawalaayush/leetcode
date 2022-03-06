class Solution(object):
    def countOrders(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        n = n * 2
        s = 1
        while n>0:
            s = (s%1000000007) * ((n%1000000007)*((n-1)%1000000007))/2
            #print(s, n)
            n = n - 2
        return s
        