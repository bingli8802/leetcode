# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 二分查找 最快 方法很好
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """      
        if not root:
            return 0 
        # 根节点左子树高度 和 根节点右子树高度
        left = self.get_depth(root.left)
        right = self.get_depth(root.right)
        # 如果左右子树一样高 证明左子树一定是满二叉树 现在要查询根节点右子树
        if left == right:
            return pow(2, left) + self.countNodes(root.right)
        # 如果左右子树高度不一样 一定是左子树高 右子树一定树满二叉树 现在要查询根节点左子树
        else: 
            return self.countNodes(root.left) + pow(2, right)
    # 计算当前根节点到叶节点高度
    def get_depth(self, root):
        d = 0
        while root:
            d += 1
            root = root.left
        return d
# BFS 迭代 广度优先
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        res = 0
        q = [root]
        while q:
            cur = q.pop(0)
            res += 1
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        return res
# DFS 递归
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return 0 if not root else 1 + self.countNodes(root.left) + self.countNodes(root.right)
# 二分查找
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        left_height = 0
        left_node = root
        right_height = 0
        right_node = root
        while left_node:
            left_node = left_node.left
            left_height += 1
        while right_node:
            right_node = right_node.right
            right_height += 1
        if left_height == right_height:
            return pow(2,left_height) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
