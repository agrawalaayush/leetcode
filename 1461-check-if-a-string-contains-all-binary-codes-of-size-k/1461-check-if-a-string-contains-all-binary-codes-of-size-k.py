class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        
        mydict = dict()
        
        st=""
        i = 0
        if k > len(s):
            return False
        
        while i<k:
            st = st + s[i]
            i = i + 1
        
        mydict[st] = 1
        
        while i<len(s):
            st = st[1:] + s[i]
            if st not in mydict:
                mydict[st] = 1
            i = i + 1
        
        if len(mydict) == (1<<k):
            return True
        return False