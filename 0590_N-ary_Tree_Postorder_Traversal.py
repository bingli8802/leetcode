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
        # 先遍历每一个子节点 再把root入栈
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
            # 先遍历每一个子节点 再把root入栈
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
            # 根节点入栈
            res.append(cur.val)
            # 从最左边孩子入栈
            for node in cur.children:
                stack.append(node)
        # 结果要反转
        return res[::-1]

