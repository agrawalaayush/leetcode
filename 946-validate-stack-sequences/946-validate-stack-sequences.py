class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        
        st = []
        
        i = 0
        j = 0
        l = len(pushed)
        
        while True:
            #print(st, i, j)
            if len(st) == 0 and j == l:
                return True
            
            if i == l:
                if st[-1] != popped[j]:
                    return False
                else:
                    while len(st) > 0 and st[-1] == popped[j]:
                        del st[-1]
                        j = j + 1
                    
            if len(st)>0:
                while len(st)>0 and st[-1] == popped[j]:
                    del st[-1]
                    j = j + 1
            if i < l:    
                st.append(pushed[i])
                i = i + 1
        