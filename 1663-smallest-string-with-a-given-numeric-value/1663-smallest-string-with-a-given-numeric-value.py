class Solution(object):
    def getSmallestString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        
        res = ""
        ch = n
        zs = k / 26
        rem_z = k - 26*zs
        #print(zs)
        while (ch-zs) > rem_z:
            zs = zs - 1
            rem_z = rem_z + 26
        rem_ch = ch - zs
        rem_k = k - 26*zs
        #print(rem_ch)
        new_one = rem_k - (rem_ch-1)
        #print(new_one, rem_ch, zs, rem_k)
        res = ""
        if rem_ch:
            for i in range(rem_ch - 1):
                res = res + "a"
        if rem_k and new_one:
            res = res + chr(ord('a')+new_one-1)
        if zs:
            for i in range(zs):
                res = res + "z"
        return res        
                
            
        