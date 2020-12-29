# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # 迭代
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        cur = head
        while cur != None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        # print head
        return prev
    
    # 递归
	def reverseList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
        if head == None or head.next == None:
            return head
        last = reverseList(head.next)
        head.next.next = head
        head.next = None
        return last
        
