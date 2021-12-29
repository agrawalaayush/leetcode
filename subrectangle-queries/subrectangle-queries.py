class SubrectangleQueries(object):

    def __init__(self, rectangle):
        """
        :type rectangle: List[List[int]]
        """
        self.rectangle = rectangle
        self.stack = []
        

    def updateSubrectangle(self, row1, col1, row2, col2, newValue):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :type newValue: int
        :rtype: None
        """
        self.stack.append((row1, col1, row2, col2, newValue))

    def getValue(self, row, col):
        """
        :type row: int
        :type col: int
        :rtype: int
        """
        l = len(self.stack) - 1 
        while l>=0:
            row1, col1, row2, col2, new_value = self.stack[l]
            if row>=row1 and row<=row2 and col>=col1 and col<=col2:
                return new_value
            l = l - 1
        return self.rectangle[row][col]
            


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)