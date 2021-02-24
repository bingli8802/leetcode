# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        dummy = head
        total = 0
        
        while l1 or l2 :
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
                
            num = total % 10
            total = total / 10
                
            tmp = ListNode(num)
            dummy.next = tmp
            dummy = tmp
        
        if total == 1:
            dummy.next = ListNode(1)
        
        return head.next
        

