# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 迭代 无递归
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        while (root != None):
            if root.left != None:
                most_right = root.left
                while most_right.right != None: 
                    most_right = most_right.right
                most_right.right = root.right
                root.right = root.left
                root.left = None
            root = root.right
        return
# DFS 递归 后续遍历
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        def helper(root):
            if root == None: 
                return
            helper(root.left)
            helper(root.right)
            if root.left: # 后序遍历
                pre = root.left # 令 pre 指向左子树
                while pre.right: 
                    pre = pre.right # 找到左子树中的最右节点
                pre.right = root.right # 令左子树中的最右节点的右子树 指向 根节点的右子树
                root.right = root.left # 令根节点的右子树指向根节点的左子树
                root.left = None # 置空根节点的左子树
            root = root.right # 令当前节点指向下一个节点
        helper(root)
# DFS 递归 前序遍历   
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.pre = None
        def helper(root):
            if not root:
                return None
            helper(root.right)
            helper(root.left)
            root.right = self.pre
            root.left = None
            self.pre = root
        helper(root)

