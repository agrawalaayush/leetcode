# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    first = []
    second = []
    def inorder(self, root, first):
        if root is None:
            return 
        self.inorder(root.left, first)
        if first:
            self.first.append(root.val)
        else:
            self.second.append(root.val)
        self.inorder(root.right, first)
        
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        self.first = []
        self.second = []
        self.inorder(root1, True)
        self.inorder(root2, False)
        #print(self.first)
        #print(self.second)
        
        res = []
        r1 = len(self.first)
        r2 = len(self.second)
        l1 = 0
        l2 = 0
        while l1 < r1 and l2 < r2:
            if self.first[l1] < self.second[l2]:
                res.append(self.first[l1])
                l1 = l1 + 1
            else:
                res.append(self.second[l2])
                l2 = l2 + 1
        while l1 < r1:
            res.append(self.first[l1])
            l1 = l1 + 1
        while l2 < r2:
            res.append(self.second[l2])
            l2 = l2 + 1
        return res
            
            
        
        