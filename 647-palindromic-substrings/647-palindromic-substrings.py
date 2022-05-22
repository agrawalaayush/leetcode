class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        z = []
        for i in range(l):
            y = []
            for j in range(l):
                y.append(0)
            z.append(y)
        
        for i in range(l):
            z[i][i] = 1
        le = 2
        count = l
        while le<=l:
            for i in range(l):
                j = i + le - 1
                if j<l:
                    if le == 2 and s[i] == s[j]:
                        z[i][j] = 1
                        count = count + 1
                        continue
                    if s[i] == s[j] and z[i+1][j-1]!=0:
                        z[i][j] = 1
                        count = count + 1
            le = le + 1
        return count