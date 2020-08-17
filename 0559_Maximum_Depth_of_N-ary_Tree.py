"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# 递归
# class Solution(object):
#     def maxDepth(self, root):
#         """
#         :type root: Node
#         :rtype: int
#         """
#         if not root:
#             return 0
#         elif root.children == []:
#             return 1
#         else:
#             height = [self.maxDepth(c) for c in root.children]
#             return max(height) + 1
# 迭代DFS
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
# 迭代BFS
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
