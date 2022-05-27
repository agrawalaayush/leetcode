class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        if num==0:
            return 0
        while num!=0:
            if num&1:
                count = count + 2
            else:
                count = count + 1
            num = num/2
        return count-1
        