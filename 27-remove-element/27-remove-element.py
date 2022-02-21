class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l = len(nums) - 1
        i = 0
        while i<len(nums) and i<=l:
            if nums[i] == val:
                temp = nums[l]
                nums[l] = nums[i]
                nums[i] = temp
                l = l - 1
            else:
                i = i + 1
        print(l)
        print(nums)
        return (l + 1)
        