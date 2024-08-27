class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        blen = len(b) - 1
        alen = len(a) - 1
        c = 0
        res = ""
        while blen >=0 or alen >=0 or c > 0:
            x = 0
            if blen >= 0:
                x = x + int(b[blen])
                blen = blen - 1 
            if alen >= 0:
                x = x + int(a[alen])
                alen = alen - 1
            x = x + c
            if x > 1:
                c = 1
            else:
                c = 0
            if x % 2  == 1:
                res = res + "1"
            else:
                res = res + "0"
        return res[::-1]
        