# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        # 记录当前奇数和偶数的指针
        odd = head
        even = head.next
        # 偶数的head 不改变
        even_head = head.next
        
        while odd.next and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        # 奇数的尾巴指向偶数的头
        odd.next = even_head
        return head
            
