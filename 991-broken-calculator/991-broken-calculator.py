class Solution(object):
    def brokenCalc(self, startValue, target):
        """
        :type startValue: int
        :type target: int
        :rtype: int
        """
        
        count = 0 
        while target != startValue:
            if target > startValue:
                if target % 2 == 0:
                    target = target / 2
                else:
                    target = target + 1
            else:
                #target = target + 1
                count  = count + startValue - target
                break
            
            count = count + 1
        return count