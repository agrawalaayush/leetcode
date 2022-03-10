# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        carry = 0
        l3 = None
        curr = None
        while l1 is not None and l2 is not None:
            print l1.val
            print l2.val
            num = l1.val+l2.val+carry
            print num
            carry = num/10
            num = num%10
            if l3==None:
                l3 = ListNode(num)
                curr = l3
            else:
                curr.next = ListNode(num)
                curr = curr.next
            l1 = l1.next
            l2 = l2.next
        while l1 is not None:
            print l1.val
            num = l1.val+carry
            carry = num/10
            num = num%10
            if l3==None:
                l3 = ListNode(num)
                curr = l3
            else:
                curr.next = ListNode(num)
                curr = curr.next
            l1 = l1.next
        while l2 is not None:
            print l2.val
            num = l2.val+carry
            carry = num/10
            num = num%10
            if l3==None:
                l3 = ListNode(num)
                curr = l3
            else:
                curr.next = ListNode(num)
                curr = curr.next
            l2 = l2.next
        if carry:
            curr.next = ListNode(carry)
            curr = curr.next
        return l3
        