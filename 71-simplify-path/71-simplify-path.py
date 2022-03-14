class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        
        paths = path.split("/")
        if path[-1] == "/":
            paths = paths[1:-1]
        else:
            paths = paths[1:]
        st = []
        #print(paths)
        for p in paths:
            if len(p) == 0: # Not valid path
                continue
            if p == "." or p == ".." and len(st) == 0: # AT root
                continue
            
            if p == ".":
                continue
            
            if p == "..":
                del st[-1]
                continue
            
            st.append(p)
        if len(st) == 0:
            return "/"
        ans = ""
        for s in st:
            ans = ans + "/" + s
        return ans