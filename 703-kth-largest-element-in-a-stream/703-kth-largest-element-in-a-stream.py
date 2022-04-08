from heapq import heapify, heappush, heappop
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        l = len(nums)
        i = 0
        self.h = []
        heapify(self.h)
        while i<k and i<l:
            heappush(self.h, nums[i])
            i = i + 1
        while i<l:
            element = heappop(self.h)
            if element < nums[i]:
                heappush(self.h, nums[i])
            else:
                heappush(self.h, element)
            i = i + 1
            

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        #print(self.h, val)
        element = None
        if len(self.h) > 0 and len(self.h) == self.k:
            element = heappop(self.h)
        
        if element is not None and val < element:
            heappush(self.h, element)
        else:
            heappush(self.h, val)
        
        ele = heappop(self.h)
        heappush(self.h, ele)
        #print(self.h, val)
        return ele
            
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)