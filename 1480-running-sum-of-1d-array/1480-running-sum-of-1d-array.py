class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        if l == 0:
            return []
        s = [0]*l
        s[0] = nums[0]
        i = 0
        while i<l:
            s[i] = s[i-1] + nums[i]
            i = i + 1
        return s