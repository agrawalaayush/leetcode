class SummaryRanges(object):

    def __init__(self):
        self.start_map = dict()
        self.end_map = dict()

    def addNum(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_start = False
        new_end = False
        start = None
        end = None
        merge_required = False
        
        for i in sorted (self.start_map):
            if val>=i and val<=self.start_map[i]:
                return
        
        
        if (val + 1) in self.start_map:
            new_end = True
            end = self.start_map[val+1]
        if (val - 1) in self.end_map:
            start = self.end_map[val-1]
            new_start = True
        if new_start and new_end:
            del self.start_map[val+1]
            del self.end_map[val-1]
            self.start_map[start] = end
            self.end_map[end] = start
            return 
        
        if new_start:
            end = val
            del self.start_map[start]
            del self.end_map[val - 1]
            self.start_map[start] = end
            self.end_map[end] = start
            return 
        
        if new_end:
            start = val
            del self.start_map[val+1]
            del self.end_map[end]
            self.start_map[start] = end
            self.end_map[end] = start
            return 
        
        self.start_map[val] = val
        self.end_map[val] = val
        return 
    
    def getIntervals(self):
        """
        :rtype: List[List[int]]
        """
        res = []
        for i in sorted (self.start_map):
            res.append([i, self.start_map[i]])
        return res
            
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()