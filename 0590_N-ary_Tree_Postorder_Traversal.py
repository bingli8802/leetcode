"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# 递归1
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []
        res = []
        for child in root.children:
            res.extend(self.postorder(child))
        res.append(root.val)
        return res
# 递归2
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        def post(root):
            if not root: 
                return []
            for node in root.children:
                post(node)
            res.append(root.val)
        res = []
        post(root)
        return res
# 迭代
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return None
        res = []
        stack = [root]
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            for node in cur.children:
                stack.append(node)
        return res[::-1]

