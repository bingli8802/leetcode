# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        cur = head
        res = 0
        while cur:
            # 正序 二进制转换十进制
            res = res * 2 + cur.val
            cur = cur.next
        return res
