# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # 如果快慢指针相遇则证明有环
            if slow == fast:
                res = head
                while res != slow:
                    res = res.next
                    slow = slow.next
                return res
        return None
