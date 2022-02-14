# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
        
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_level = 0
        def maxDeptUtil(root, level):
            if root is None:
                self.max_level = max(level, self.max_level)
                return None
        
            maxDeptUtil(root.left, level+1)
            maxDeptUtil(root.right, level+1)
        
        maxDeptUtil(root, 0)
        return self.max_level
        
        