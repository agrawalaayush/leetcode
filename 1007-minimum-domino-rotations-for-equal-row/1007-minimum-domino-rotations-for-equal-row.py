class Solution(object):
    def minDominoRotations(self, tops, bottoms):
        """
        :type tops: List[int]
        :type bottoms: List[int]
        :rtype: int
        """
        
        start = tops[0]
        start2 = bottoms[0]
        
        i = 0 
        l = len(tops)
        
        topcount = 0
        bottomcount = 0
        possible = True
        while i<l:
            flag = False
            flag2 = False
            if tops[i] == start:
                topcount = topcount + 1
                flag = True
            if bottoms[i] == start:
                bottomcount = bottomcount + 1
                flag2 = True 
            if not (flag or flag2):
                possible = False
                break
            i = i + 1
        
        #print(topcount, bottomcount, start)
        ans = None
        if possible:
            ans = min(l-topcount, l-bottomcount)
        
        #print(ans)
        topcount = 0
        bottomcount = 0
        possible = True
        i = 0 
        while i<l:
            flag = False
            flag2 = False
            if tops[i] == start2:
                topcount = topcount + 1
                flag = True
            if bottoms[i] == start2:
                bottomcount = bottomcount + 1
                flag2 = True 
            if not (flag or flag2):
                possible = False
                break
            i = i + 1
        #print(topcount, bottomcount, start2, ans)
        if not possible and not ans:
            return -1
        if ans:
            ans = min(ans, min(l-topcount, l-bottomcount))
        else:
            ans = min(l-topcount, l-bottomcount)
        return ans
        