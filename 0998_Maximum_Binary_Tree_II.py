# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 题目的意思想要节点直接插入到右子树
# 这题难度全在理解题干上了
class Solution(object):
    def insertIntoMaxTree(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root or val > root.val:
            newRoot = TreeNode(val)
            newRoot.left = root
            return newRoot
        else:
            root.right = self.insertIntoMaxTree(root.right, val)
        return root
