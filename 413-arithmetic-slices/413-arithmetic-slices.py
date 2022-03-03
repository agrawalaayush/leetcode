class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        le = len(nums)
        
        i = 0
        curr_diff = None
        ans = 0
        while i < (le - 2):
            a = nums[i]
            b = nums[i+1]
            c = nums[i+2]
            if (b - a) == (c-b):
                if curr_diff == None:
                    curr_diff = b-a
                    count = 1
                else:
                    if curr_diff == (c-b):
                        count = count + 1
                    else:
                        curr_diff = c-b
                        count = 1
                ans = ans  + count
            else:
                curr_diff = None
            i = i + 1
        return ans