class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        z = -1
        for i in range(len(n)):
            if int(n[i]) > z:
                z = int(n[i])
        return z
        