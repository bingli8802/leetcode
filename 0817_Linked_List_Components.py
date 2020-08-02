# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        # 如果当前的节点在列表G中，并且下一个节点不在列表G中，我们就找到了一个组件的尾节点，可以将答案加 1
        Gset = set(G)
        ans = 0
        while head:
            # getattr方法很好 这里判断如果head.next没有val的话 就默认赋值none
            if head.val in Gset and getattr(head.next, 'val', None) not in Gset:
                ans += 1
            head = head.next 
        return ans
    
class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        # 如果当前的节点在列表G中，并且下一个节点不在列表G中，我们就找到了一个组件的尾节点，可以将答案加 1
        Gset = set(G)
        ans = 0
        while head and head.next:
            if head.val in Gset and head.next.val not in Gset:
                ans += 1
            head = head.next 
            
        # 由于while判断head.next为空的话就停止 最后一个元素可能就错过了 所以要补充判断最后一个元素的可能性
        if head.val in Gset:
            ans += 1
        return ans


            
