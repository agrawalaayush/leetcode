class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        count = [0]*26
        for s1 in s:
            count[ord(s1)-ord('a')] = count[ord(s1)-ord('a')] + 1
        
        visited = [0]*26
        st = []
        
        for s1 in s:
            ind = ord(s1) - ord('a')
            count[ind] = count[ind] - 1 
            if visited[ind]:
                continue
            while len(st)>0 and st[-1]>s1 and count[ord(st[-1])-ord('a')]>0:
                visited[ord(st[-1])-ord('a')] = 0
                del st[-1]
            
            st.append(s1)
            visited[ind] = 1
        return "".join(st)