class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mymap = dict()
        for num in nums:
            if num in mymap:
                mymap[num] = mymap[num] + 1
            else:
                mymap[num] = 1
        
        count = 0
        #print(mymap)
        for key,value in mymap.items():
            #print key, value, count
            if k == 0:
                if value>1:
                    count = count + 1
                continue
                
            if (key - k) in mymap:
                count = count + 1
            if (key + k) in mymap:
                count = count + 1
        if k==0:
            return count
        return count/2
        