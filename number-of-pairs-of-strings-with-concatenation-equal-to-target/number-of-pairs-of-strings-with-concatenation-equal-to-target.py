class Solution(object):
    def numOfPairs(self, nums, target):
        """
        :type nums: List[str]
        :type target: str
        :rtype: int
        """
        def check_all_same(target):
            l = len(target)
            i = 0
            while i<l-1:
                if target[i] != target[i+1]:
                    return False
                i = i + 1
            return True
        l = len(nums)
        
        i = 0 
        res = 0
        check = check_all_same(target)
        while i<l:
            j = 0
            while j<l:
                if i!=j:
                    concat = nums[i] + nums[j]
                    #print(i,j,concat)
                    if concat == target:
                        res = res + 1
                j = j + 1
            i = i + 1
        return res