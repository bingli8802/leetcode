# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):            
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """   
        if not head or not head.next:
            return head
        slow = fast = head
        # To find the middle
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        
        left = self.sortList(head)
        right = self.sortList(mid)
        
        return self.merge(left, right)
    
    def merge(self, left, right):
        if not left:
            return right
        if not right:
            return left
        if left.val < right.val:
            left.next = self.merge(left.next, right)
            return left
        else: 
            right.next = self.merge(left, right.next)    
            return right
        
        
