class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        l = len(height)
        left = [-1]*l
        right = [-1]*l
        
        i = 1
        left[0] = height[0]
        while i < l:
            left[i] = max(left[i-1], height[i])
            i = i + 1
        
        right[l-1] = height[l-1]
        i = l - 2
        while i>=0:
            right[i] = max(right[i+1], height[i])
            i = i - 1
        
        ans = 0
        i = 0
        
        while i<l:
            ans = ans + min(left[i], right[i]) - height[i]
            i = i + 1
        
        return ans 