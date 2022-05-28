class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        status = [0]*len(nums)
        for i in range(len(nums)):
            if nums[i] >= len(nums):
                continue
            else:
                status[abs(nums[i])] = 1
        for i in range(len(nums)):
            if status[i]==0:
                return i
        return len(nums)
        