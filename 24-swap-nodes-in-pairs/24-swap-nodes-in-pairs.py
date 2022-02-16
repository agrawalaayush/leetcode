# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        
        first = head
        second = head.next 
        next_link = second.next
        
        second.next = first
        first.next = self.swapPairs(next_link)
        head = second
        return head
        
        