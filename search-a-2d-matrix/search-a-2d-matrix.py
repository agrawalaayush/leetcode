class Solution(object):
    
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def binarySearch(arr, low, high, target):
            if low>high:
                return -1
            if low == high and arr[low] == target:
                return low
            
            if (low + 1) == high:
                if arr[low] == target:
                    return low
                if arr[high] == target:
                    return high
            mid = low + (high - low)/2
            if arr[mid] == target:
                return mid
            
            if arr[mid]>target:
                return binarySearch(arr, low, mid-1, target)
            return binarySearch(arr, mid+1, high, target)
        
        def floor(arr, low, high, target):
            if low>high:
                return -1
            if low == high and arr[low]<=target:
                return low
            if arr[low]>target:
                return -1
            if arr[high]<=target:
                return high
            
            mid = low + (high - low)/2 
            if (mid + 1)<=high and arr[mid]<=target and arr[mid+1]>target:
                return mid
            if (mid-1)>=low and arr[mid-1]<=target and arr[mid]>target:
                return mid-1
            
            if arr[mid]>target:
                return floor(arr, low, mid-1, target)
            return floor(arr, mid+1, high, target)
        
        
        start_index_values = []
        for i in range(len(matrix)):
            start_index_values.append(matrix[i][0])
        
        check_floor = floor(start_index_values, 0, len(matrix)-1, target)
        print(check_floor)
        if check_floor == -1:
            return False
        potential_row = []
        for i  in range(len(matrix[0])):
            potential_row.append(matrix[check_floor][i])
        
        check = binarySearch(potential_row, 0, len(matrix[0])-1, target)
        if check !=-1:
            return True
        return False