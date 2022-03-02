class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        arr = [0]*(n+1)
        arr[0] = 0
        arr[1] = 1
        i = 2
        while i<=n:
            arr[i] = arr[i-1] + arr[i-2]
            i = i + 1
        return arr[n]