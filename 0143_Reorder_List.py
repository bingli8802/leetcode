# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        # 找中点 取后半段
        slow = head
        fast = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # 截取后半段
        second = slow.next
        # 将链表断开
        slow.next = None
        prev = None
        # 反转后半段
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        # 将后半段插入前半段
        res = head
        while prev:
            temp = res.next
            res.next = prev

            prev = prev.next
            res = res.next
            
            res.next = temp
            res = temp
        return head
