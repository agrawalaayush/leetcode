class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        val = None
        for num in nums:
            if val == None:
                val = num
                count = count + 1
            elif val == num:
                count = count + 1
            else:
                count = count - 1
                if count == 0:
                    val = num
                    count = count + 1
        return val
        