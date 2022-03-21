class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        
        first = [0]*26
        last = [0]*26
        
        i = 0
        for s1 in s:
            index = ord(s1) - ord('a')
            if first[index] == 0:
                first[index] = i 
                last[index] = i
            else:
                last[index] = i
            i = i + 1
        
        
        visited = [0]*26
        res = []
        m = -1
        
        i = 0
        l = len(s)
        start = 0
        max_end = None
        while i<l:
            index = ord(s[i]) - ord('a')
            max_end = last[index]
            j = start
            while j<=max_end:
                indexj = ord(s[j]) - ord('a')
                max_end = max(max_end, last[indexj])
                j = j + 1
            
            res.append(max_end-start+1)
            i = max_end + 1
            start = i
            #print(max_end, start)
        return res