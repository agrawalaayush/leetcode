class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        
        l = len(nums)
        if l == 0:
            return res
        con = 0
        i = 1
        prev_index = 0 
        while i < l:
            if nums[i] == (nums[prev_index] + i - prev_index):
                i = i + 1
            else:
                if (i - prev_index - 1) == 0:
                    res.append(str(nums[prev_index]))
                else:
                    res.append(str(nums[prev_index]) + "->" + str(nums[i-1]))
                prev_index = i
                i = i + 1
        print(i, prev_index)
        if (i - prev_index - 1) == 0:
            res.append(str(nums[prev_index]))
        else:
            res.append(str(nums[prev_index]) + "->" + str(nums[i-1]))
        print(res)
        return res
                
                
                    
        