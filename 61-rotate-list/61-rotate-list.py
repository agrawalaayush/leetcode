# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        count = 0
        curr = head 
        if head is None or head.next is None:
            return head
        prev = None
        mymap = dict()
        while curr is not None:
            prev = curr
            curr = curr.next
            mymap[curr] = prev
            count = count + 1
    
        #print(count)
        #print(prev)
        #print(mymap)
        #print(len(mymap))
        k = k % count 
        curr = head
        while k > 0:
            parent = mymap[prev]
            #print(prev, parent)
            parent.next = None
            prev.next = curr
            curr = prev
            prev = parent
            k = k - 1
        return curr        