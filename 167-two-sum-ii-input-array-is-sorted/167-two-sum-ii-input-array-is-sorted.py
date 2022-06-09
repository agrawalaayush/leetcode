class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #print(nums)
        left = 0
        right = len(nums) - 1
        while left < right:
            s = nums[left] + nums[right]
            if s == target:
                return [left+1, right+1]
            elif s < target:
                left = left + 1
            else:
                right = right - 1
        