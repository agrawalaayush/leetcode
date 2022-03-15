class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        st = []
        valid = set()
        i = 0
        l = len(s)
        while i < l:
            if s[i] == "(":
                st.append(i)
            elif s[i] == ")":
                if len(st) > 0:
                    top = st[-1]
                    del st[-1]
                    valid.add(top)
                    valid.add(i)
            i = i + 1
        
        
        #print(valid)
        i = 0
        res = ""
        while i<l:
            if s[i] in ["(", ")"]: 
                if i in valid:
                    res = res + s[i]
            else:
                res = res + s[i]
            i = i + 1
        return res
                
                