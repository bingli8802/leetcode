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
        # 递归
        if head == None or head.next == None:
            return head
        curr = head.next
        head.next = self.swapPairs(curr.next)
        curr.next = head
        return curr
        # 迭代
        thead = ListNode(-1)
        thead.next = head
        c = thead
        while c.next and c.next.next:
            a = c.next
            b = c.next.next
            c.next = b
            a.next = b.next
            b.next = a
            c = c.next.next
        return thead.next
