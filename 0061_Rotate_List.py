# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # 快慢指针做法
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return
        
        cnt = 0
        dummy = head
        while dummy:
            cnt += 1
            dummy = dummy.next
        
        k = k % cnt   
                    
        if cnt == 1 or k == 0:
            return head
        
        slow = head
        fast = head
        for i in range(k):
            fast = fast.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        
        cur = slow.next
        tmp = cur
        slow.next = None
                
        while tmp and tmp.next:
            tmp = tmp.next
            
        if tmp:    
            tmp.next = head
        
        return cur
       
    # liweiwei 解法 首尾相连
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 0:
            return head
        
        cnt = 1
        dummy = head
        while dummy.next:
            cnt += 1
            dummy = dummy.next
            
        dummy.next = head
        dummy = head
        k = k % cnt
        
        for i in range(cnt - k - 1):
            dummy = dummy.next
            
        new_head = dummy.next
        dummy.next = None
        return new_head
        
        
        
