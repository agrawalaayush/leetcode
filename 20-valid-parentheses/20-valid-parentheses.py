class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = []
        
        i = 0
        l = len(s)
        while i<l:
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                st.append(s[i])
            elif s[i] == ')':
                if len(st)>0 and st[-1] == '(':
                    del st[-1]
                else:
                    return False
            elif s[i] == '}':
                if len(st)>0 and st[-1] == '{':
                    del st[-1]
                else:
                    return False
            elif s[i] == ']':
                if len(st)>0 and st[-1] == '[':
                    del st[-1]
                else:
                    return False
            i = i + 1
        if len(st) == 0:
            return True
        return False
        