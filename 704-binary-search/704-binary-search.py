class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binarySearch(nums, left, right, target):
            if left>right:
                return -1
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            if (left == right):
                return -1
            
            mid = left + (right-left)/2
            if nums[mid] == target:
                return mid
            if nums[mid]>target:
                return binarySearch(nums, left, mid-1, target)
            else:
                return binarySearch(nums, mid+1, right, target)
        
        return binarySearch(nums, 0, len(nums)-1, target)