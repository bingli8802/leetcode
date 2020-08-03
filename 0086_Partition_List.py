# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # 两个双链表
        small = ListNode(0)
        large = ListNode(0)
        sm = small
        lg = large
        while head:
            if head.val < x:
                sm.next = head
                sm = sm.next
            else:
                lg.next = head
                lg = lg.next
            head = head.next
        # lg的tail一定要指向None 否则sm lg最后都指向2
        lg.next = None
        sm.next = large.next
        return small.next
