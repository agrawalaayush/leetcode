class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        maxRows = numRows
        maxCols = 1001
        if numRows == 1 and numRows == len(s):
            return s
        arr = []
        for i in range(maxRows):
            a = []
            for j in range(maxCols):
                a.append("-1")
            arr.append(a)
        
        i = 0
        j = 0
        down = 1
        for s1 in s:
            arr[i][j] = s1
            if i == (numRows - 1):
                down = 0
            elif i == 0:
                down = 1
            
            if down == 1:
                i = i + 1
            else:
                if i == 0:
                    i = 0
                else:
                    i = i - 1
                
                j = j + 1
        res = ""
        #print j
        i=0
        j1 = 0
        for i in range(numRows):
            for j1 in range(j+1):
                if arr[i][j1] != "-1":
                    #print(i,j1,arr[i][j1])
                    res = res + arr[i][j1]
        return res