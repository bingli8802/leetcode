# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # slow,fast,prev = head,head,None
        slow = head
        fast = head

        # 找中点 slow是中点
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # fast = fast.next.next if fast.next is not None else fast.next
            
        # 反转slow后面的元素
        prev = None
        while slow:
            curr = slow.next
            slow.next = prev
            prev = slow
            slow = curr
            # slow.next, slow, prev= prev, slow.next, slow
            
        # 比较slow后面的元素和head
        while head and prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True

