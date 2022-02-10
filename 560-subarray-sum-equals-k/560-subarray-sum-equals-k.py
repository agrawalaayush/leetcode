class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        my_dict = dict()
        curr_sum = 0
        result = 0
        my_dict[0] = 1
        for i in nums:
            curr_sum = curr_sum + i
            #print(curr_sum, my_dict, result)
            if (curr_sum-k) in my_dict:
                result = result + my_dict[curr_sum-k]
            
            if curr_sum in my_dict:
                my_dict[curr_sum] = my_dict[curr_sum] + 1
            else:
                my_dict[curr_sum] = 1
        
        return result
        