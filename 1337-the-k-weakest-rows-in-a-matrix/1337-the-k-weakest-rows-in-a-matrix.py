class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        
        max_row = len(mat)
        max_col = len(mat[0])
        mydict = dict()
        row = 0
        col = 0
        while row < max_row:
            col = 0
            while col < max_col:
                if mat[row][col] == 1:
                    col = col + 1
                else:
                    mydict[row] = col
                    break
            if col == max_col:
                mydict[row] = col
            
            row = row + 1
        
        #print(mydict)
        sorted_x = sorted(mydict.items(), key=operator.itemgetter(1))
        #print(sorted_x)
        ans = []
        while k > 0:
            ans.append(sorted_x[0][0])
            del sorted_x[0]
            k = k - 1
        return ans