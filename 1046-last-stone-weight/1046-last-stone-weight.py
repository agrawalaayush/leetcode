class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        
        stones.sort()
        
        while len(stones)!=1:
            h1 = stones[-1]
            del stones[-1]
            h2 = stones[-1]
            del stones[-1]
            stones.append(h1-h2)
            stones.sort()
        return stones[0]