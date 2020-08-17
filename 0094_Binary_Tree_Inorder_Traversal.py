# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 递归1
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        res = []
        inorder(root)
        return res
# 递归2      
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
# 迭代1
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        cur = root
        while stack or cur:
            # 当左子树不存在的时候循环停止
            while cur:
                # stack入栈
                stack.append(cur)
                # 目标左子树
                cur = cur.left
            # 出栈
            cur = stack.pop()
            res.append(cur.val)
            # 目标值右子树
            cur = cur.right
        return res
