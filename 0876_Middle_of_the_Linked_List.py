# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
            
        mid = length / 2
        
        for i in range(0,mid):
            head = head.next
        return head
            
