class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums1 = copy.copy(nums)
        nums.sort()
        
        i = 0
        j = len(nums)-1
        
        while i<j:
            if (nums[i]+nums[j]) == target:
                if nums[i]*2 == target:
                    return [nums1.index(nums[i]),nums1.index(nums[j], nums1.index(nums[i])+1)]
                else:
                    return [nums1.index(nums[i]),nums1.index(nums[j])]
            elif (nums[i]+nums[j]) > target:
                j = j-1
            else:
                i = i + 1