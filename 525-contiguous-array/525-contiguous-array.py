class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new_nums = nums
        le = len(new_nums)

        i = 0 
        my_dict = dict()
        curr_sum = 0
        max_len = 0
        while i < le:
            if new_nums[i] == 0:
                curr_sum = curr_sum - 1
            else:
                curr_sum = curr_sum + 1
            if curr_sum == 0:
                max_len = max(max_len, i+1)
            elif curr_sum in my_dict:
                prev = my_dict[curr_sum]
                max_len = max(max_len, i-prev)
            else:
                my_dict[curr_sum] = i
            i = i + 1
        return max_len