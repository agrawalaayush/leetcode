class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        res = []    
        for op in ops:
            #print(res, op)
            if op == "+":
                s = res[-1] + res[-2]
                res.append(s)
            elif op == "D":
                d = res[-1]*2
                res.append(d)
            elif op == "C":
                del res[-1]
            else:
                res.append(int(op))
        s1 = 0
        for r in res:
            s1 = s1 + r
        return s1