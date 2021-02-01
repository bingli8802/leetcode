# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # 东哥思路
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        # 区间[a,b)包含k个待反转元素
        a = b = head
        for i in range(k):
            # 剩余数量小于k的话，则不需要反转 base case
            if not b:
                return head
            b = b.next
        
        # 反转前k个元素，将返回的头结点记为newHead
        newHead = self.reverse(a, b)
        # 将head.next 赋为 递归上一步反转得到的newHead
        a.next = self.reverseKGroup(b, k)
        return newHead
    
    # 反转区间[a,b)元素 注意左闭右开区间，所以本轮操作的尾结点其实就是下一轮操作的头结点
    def reverse(self, a, b):
        pre = None
        while a != b:
            tmp = a.next
            a.next = pre
            pre = a
            a = tmp
        return pre
