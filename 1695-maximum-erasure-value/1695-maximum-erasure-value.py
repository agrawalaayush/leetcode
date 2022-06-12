class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        mydict = dict()
        ans = -1
        s = 0
        l = len(nums)
        prefix = [0]*l
        prefix[0] = nums[0]
        i = 1
        while i<l:
            prefix[i] = prefix[i-1] + nums[i]
            i = i + 1
        
               
        for end in range(len(nums)):
            if nums[end] in mydict:
                last = mydict[nums[end]]
                #print(start, end, last)
                while start <= last:
                    s = s - nums[start]
                    start = start + 1
            mydict[nums[end]] = end
            s = s + nums[end]
            end = end + 1
            ans = max(ans, s)
        
        return ans
        
                
        