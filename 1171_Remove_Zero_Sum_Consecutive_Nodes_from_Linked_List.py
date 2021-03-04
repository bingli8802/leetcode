# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        '''                
        head = [1, 2, 3, -1, -2, 1]
         arr = [1, 2, -3]
                      cur       i
                   j
        '''
        if not head.next:
            if head.val == 0:
                return None
            else:
                return head
        arr = []
        
        while head != None:
            arr.append(head.val)
            head = head.next
            
            cur = len(arr) - 1
            total = 0
            
            for j in range(cur, -1, -1):
                total += arr[j]
                if total == 0:
                    arr = arr[:j]
                    break
                
        dummy = ListNode(0)
        pre = dummy
        
        for num in arr:
            dummy.next = ListNode(num)
            dummy = dummy.next
            
        return pre.next
        

                    
                
        
