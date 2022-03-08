# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        first = head
        second = head 
        if first is None:
            return False
        else:
            second = second.next
        while first is not None and second is not None:
            if first==second:
                return True
            first = first.next
            second = second.next
            if second is not None:
                second = second.next
            else:
                return False
            
        