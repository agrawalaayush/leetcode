# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        curr = head 
        prev = None
        while curr is not None and curr.next is not None:
            tmp = curr
            while curr.next is not None and curr.val == curr.next.val:
                curr = curr.next
            n = curr.next
            if tmp == curr:
                # no duplicates
                prev = tmp
                curr = curr.next
            
            else:
                if tmp.val == head.val:
                    head = n
                else:    
                    prev.next = n
                curr = n
        
        return head
                
                
        return head