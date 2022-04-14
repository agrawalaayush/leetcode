# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBSTUtil(self, root, val, min_val, max_val):
        #print(root, min_val, max_val)
        if root is None:
            return None
        if root.val == val:
            return root
        if root.val < min_val or root.val > max_val:
            return None
        if root.val > val:
            return self.searchBSTUtil(root.left, val, min_val, root.val-1)
        return self.searchBSTUtil(root.right, val, root.val+1, max_val)
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        return self.searchBSTUtil(root, val, 0, 10000001)
        