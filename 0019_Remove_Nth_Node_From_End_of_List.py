# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        slow = fast = head
        # 快指针先走n步
        for i in range(n):
            fast = fast.next
        # 如果当前快指针走到头 说明倒数第n个节点就是第一个节点
        if fast == None:
            return head.next
        # 慢指针再和快指针一起走 当快指针走到头 慢指针在的节点就是第n个节点
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
       
        slow.next = slow.next.next
        return head
        
