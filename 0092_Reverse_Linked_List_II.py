# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        # Empty list
        if not head:
            return None

        # Move the two pointers until they reach the proper starting point
        # in the list.
        cur = head
        prev = None
        while m > 1:
            prev = cur
            cur = cur.next
            m = m - 1
            n = n - 1
        # The two pointers that will fix the final connections.
        tail = cur
        con = prev
        # Iteratively reverse the nodes until n becomes 0.
        while n:
            third = cur.next
            cur.next = prev
            prev = cur
            cur = third
            n -= 1
        # Adjust the final connections as explained in the algorithm
        # 判断cur前面是否有元素
        if con:
            con.next = prev
        else:
            head = prev
        # con.next = prev
        tail.next = cur
        return head
