"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# 递归1
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root: 
            return []
        res = [root.val]
        for node in root.children:
            res.extend(self.preorder(node))
        return res
# 递归2
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        def pre(root):  
            if not root:
                return
            # 先遍历根节点 再依次访问每一个孩子节点
            res.append(root.val)
            for child in root.children:
                pre(child)
        res = []
        pre(root)
        return res
# 迭代
class Solution(object):
    def preorder(self, root):
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
            for child in cur.children[::-1]:
                stack.append(child)
        return res
