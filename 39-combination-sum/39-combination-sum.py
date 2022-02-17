class Solution(object):
    result = []
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.result=[]
        potential = []
        candidates.sort()
        self.utils(candidates, target, potential)
        return self.result
    
    def utils(self, candidates, target, potential):
        #print target
        #print potential
        if target == 0:
            self.result.append(potential)
            return 
        for i in range(len(candidates)):
            if target >= candidates[i]:
                potential.append(candidates[i])
                self.utils(candidates[i:], target-candidates[i], potential[:])
                potential.pop()