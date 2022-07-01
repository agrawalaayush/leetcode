class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        
        boxes = sorted(boxTypes, key = lambda x: x[1])
        boxes.reverse()
        #print(boxes)
        
        curr = 0
        res = 0
        for box in boxes:
            if (curr+box[0]) > truckSize:
                res = res + (truckSize - curr)*box[1]
                break
            else:
                res = res + box[0]*box[1]
                curr = curr + box[0]
        return res
        