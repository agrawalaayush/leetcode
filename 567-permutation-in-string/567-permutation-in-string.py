class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        def check_dict(freq1, freq2):
            for k,v in freq1.items():
                if v != freq2.get(k,0):
                    return False
            for k,v in freq2.items():
                if v != freq1.get(k,0):
                    return False
            return True
        
        freq1 = dict()
        freq2 = dict()
        for s in s1:
            freq1[s] = freq1.get(s, 0) + 1
        
        s1_len = len(s1)
        s2_len = len(s2)
        if s2_len < s1_len:
            return False
        i = 0
        j = None
        while i<s2_len:
            freq2[s2[i]] = freq2.get(s2[i],0) + 1
            if i >= (s1_len - 1):
                #print i,j
                #print freq1, freq2
                if (check_dict(freq1, freq2)):
                    return True
                if j is None:
                    j = 0
            if j is not None:
                #print j
                freq2[s2[j]] = freq2[s2[j]] - 1
                if freq2[s2[j]] == 0:
                    del freq2[s2[j]]
                j = j + 1
            i = i + 1
        
        return False
                