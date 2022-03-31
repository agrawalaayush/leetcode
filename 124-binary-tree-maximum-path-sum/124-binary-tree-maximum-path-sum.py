# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    max_sum = -10005
    def util(self, root):
        #print root
        if root is None:
            return 0
        left_sum = max(0, self.util(root.left))
        right_sum = max(0, self.util(root.right))
        self.max_sum = max(self.max_sum, left_sum+right_sum+root.val)
        return root.val + max(left_sum, right_sum)
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.util(root)
        return self.max_sum