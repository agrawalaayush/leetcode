class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0 or n==1 or n == 2:
            return 0
        if n == 3:
            return 1
        
        primes = [1]*(n+1)
        primes[0] = 0
        primes[1] = 0
        primes[2] = 1
        primes[3] = 1
        
        i = 2
        while i*i <= n:
            if primes[i] == 0:
                i = i + 1
                continue
            primes[i] = 1
            j = i*i
            while j <= n:
                primes[j] = 0
                j = j + i
            i = i + 1
        
        i = 0 
        count = 0
        while i<n:
            if primes[i] == 1:
                count = count + 1
            i = i + 1
        return count