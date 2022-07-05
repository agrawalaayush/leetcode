class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi = 0
        s = set(nums)
        for num in nums:
            if num-1 not in s:
                count = 0
                start = num
                while start in s:
                    count = count + 1
                    start = start + 1
                if count> maxi:
                    maxi= count
        return maxi