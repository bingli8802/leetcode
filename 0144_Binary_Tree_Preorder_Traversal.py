# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 递归1
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
# 递归2
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def preorder(root):
            if not root:
                return
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)
        res = []
        preorder(root)
        return res
# 迭代1
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """  
        res = []
        stack = []
        cur = root
        while stack or cur:
            while cur:
                # res先把root节点入栈
                res.append(cur.val)
                # stack入栈
                stack.append(cur)
                # 目标左子树
                cur = cur.left
            cur = stack.pop()
            # 目标右子树
            cur = cur.right
        return res
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        stack = [root]
        # 出栈的时候 先出左子树 再出右子树
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            # 先把右子树入栈
            if cur.right:
                stack.append(cur.right)
            # 再把左子树入栈
            if cur.left:
                stack.append(cur.left)
        return res
        
