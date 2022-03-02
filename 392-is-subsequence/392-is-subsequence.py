class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        first  = len(s)
        second = len(t)
        
        i = 0
        j = 0
        if first == 0:
            return True
        if second == 0:
            return False
        while i<first:
            while j<second:
                if s[i] == t[j]:
                    i = i + 1
                    j = j + 1
                else:
                    j = j + 1
                #print(i,j)
                if i == first:
                    #print(i)
                    return True
            #print(i)
            if i==first:
                return True
            else:
                return False
        