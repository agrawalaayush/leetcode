class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = dict()
        for i in s:
            d[i] = d.get(i, 0) + 1
        
        ##e = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
        import operator
        sorted_x = sorted(d.items(), key=operator.itemgetter(1))
        h = set()
        max_index = 1
        count = 0
        #print(sorted_x)
        for x in sorted_x:
            c = x[1]
            #print(c)
            if c in h:
                ct = 0
                while c in h:
                    c = c - 1
                    ct = ct + 1
                #print (ct)
                count = count + ct
                if c!=0:
                    h.add(c)
            else:
                h.add(c)
        return count
                    
                