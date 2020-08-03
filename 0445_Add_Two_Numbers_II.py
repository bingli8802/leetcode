# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stack1 = []
        stack2 = []
        carry = 0
        head = None
        # 先把两个链表数据分别入栈
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        # 进行加法运算    
        while stack1 or stack2:
            x = stack1.pop() if stack1 else 0
            y = stack2.pop() if stack2 else 0
            ans = x + y + carry
            res = ans % 10
            carry = ans // 10 
            # 创建新链表方法
            cur = ListNode(res) 
            cur.next = head
            head = cur
        # 如果两个栈长度相等 判断是否有进位
        if carry != 0:
            # 创建新链表 并指向cur
            last = ListNode(carry)
            last.next = cur
            return last
        return cur


