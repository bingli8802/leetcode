# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        num = 0
        cur = root
        res = []
        # 计算链表长度
        while cur:
            num += 1
            cur = cur.next
        # 得到基础长度
        width = num / k
        # 有rem个长度需要加一
        rem = num % k
        # 两个for循环
        cur = root
        for i in range(k):
            res.append(cur)
            # 算出每段长度是否需要加一
            size = width + (1 if rem > 0 else 0) 
            if cur:   
                # 余数rem就是前rem段每段的长度为：width + 1
                for j in range(size - 1):
                    cur = cur.next
                rem -= 1
                tmp = cur.next
                cur.next = None
                cur = tmp
        return res
        
