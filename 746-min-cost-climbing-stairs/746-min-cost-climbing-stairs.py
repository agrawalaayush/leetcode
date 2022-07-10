class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.append(0)
        l = len(cost)
        res = [0]*l
        res[0] = cost[0]
        res[1] = min(cost[0], cost[1])
        for i in range(l):
            res[i] = cost[i] + min(res[i-1], res[i-2])
        print(res)
        return res[l-1]
        