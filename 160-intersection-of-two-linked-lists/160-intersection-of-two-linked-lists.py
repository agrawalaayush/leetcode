# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        list1 = []
        list2 = []
        while headA is not None:
            list1.append(headA)
            headA = headA.next
        
        while headB is not None:
            list2.append(headB)
            headB = headB.next
        
        k = len(list2)-1
        k1 = len(list1)-1
        #print list1
        #print list2
        #print k
        #print k1
        #print type(list2[k])
        while k>=0 and k1>=0 and (list2[k] == list1[k1]):
            k = k-1
            k1= k1-1
        if k==len(list2)-1:
            return None
        return list2[k+1]
            
            
        
         