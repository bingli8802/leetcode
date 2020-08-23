# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubPath(self, head, root):
        """
        :type head: ListNode
        :type root: TreeNode
        :rtype: bool
        """
        if not root: 
            return False
        return self.helper(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right) 

    def helper(self, head, root):
        if not head: 
            return True
        if root and root.val != head.val or not root: 
            return False
        return self.helper(head.next, root.left) or self.helper(head.next, root.right)
    
# 自己答案 不对 TODO
# class Solution(object):
#     def isSubPath(self, head, root):
#         """
#         :type head: ListNode
#         :type root: TreeNode
#         :rtype: bool
#         """
#         cur = head
#         def dfs(head, root):
#             # if not root:
#             #     return False
#             if head.next == None:
#                 return True
#             if root.val != head.val:
#                 if root.left:
#                     dfs(head, root.left)
#                 if root.right:
#                     dfs(head, root.right)
#             elif root.val == head.val:    
#                 if root.left:
#                     dfs(head.next, root.left)
#                 if root.right:
#                     dfs(head.next, root.right)
#         return dfs(head, root)
