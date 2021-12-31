class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_sum = 0
        i = 1 
        while i < len(prices):
            if prices[i]>prices[i-1]:
                max_sum = max_sum + prices[i] - prices[i-1]
            i = i + 1
        return max_sum