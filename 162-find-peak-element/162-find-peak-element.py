class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        l = len(nums)
        
        while i < l - 1:
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i
            i = i + 1
        
        if l == 1:
            return 0
        if nums[0]>nums[1]:
            return 0
        if nums[l-1]>nums[l-2]:
            return l-1
        