# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 一个指针不适用于dynamic链表 考虑用快慢指针
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

# 快慢指针 实时查找middle
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """         
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
