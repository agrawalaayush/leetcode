class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount==0:
            return 0
        result = [-1]*(amount+1)
        coins.sort()
        for coin in coins:
            if coin<=amount:
                result[coin] = 1
        result[0] = 0
        for i in range(1,amount+1):
            if result[i] == -1:
                for coin in coins:
                    if coin>i:
                        break
                    if result[i] == -1:
                        if result[i-coin] !=-1:
                            result[i] = result[i-coin] + 1
                    else:
                        if result[i-coin] !=-1:
                            result[i] = min(result[i], result[i-coin]+1)
        return result[amount]