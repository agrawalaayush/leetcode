class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def findPivot(nums, left, right):
            if left > right:
                return -1
            
            if left == right:
                return left
            if (left + 1) == right:
                if nums[left]>nums[right]:
                    return left
                return right
            
            mid = left + (right-left)/2
            if (mid+1)<=right and nums[mid]>nums[mid+1]:
                return mid
            if (mid-1)>=left and nums[mid-1]>nums[mid]:
                return mid-1
            
            if nums[mid]>nums[left]:
                return findPivot(nums, mid, right)
            return findPivot(nums, left, mid)
        
        def binarySearch(nums, left, right, target):
            if left>right:
                return -1
            mid = left + (right-left)/2
            if nums[mid] == target:
                return mid
            
            if nums[mid]>target:
                return binarySearch(nums, left, mid-1, target)
            return binarySearch(nums, mid+1, right, target)
        
        pivot = findPivot(nums, 0, len(nums)-1)
        print(pivot)
        if pivot == -1:
            return binarySearch(nums, 0, len(nums)-1, target)
        if target>=nums[0]:
            return binarySearch(nums, 0, pivot, target)
        return binarySearch(nums, pivot+1, len(nums)-1, target)
    
            
                
        