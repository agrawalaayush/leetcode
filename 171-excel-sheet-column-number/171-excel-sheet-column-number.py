class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        
        c = 0
        le = len(columnTitle)
        i=0
        while i < le:
            x = columnTitle[i]
            val = ord(x) - ord('A') + 1
            i = i + 1
            c = c*26 + val
            print(x, val, c)
        return c