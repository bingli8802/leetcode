# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 树不变
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def dfs(node, k):
            if not node:
                return None
            if node.left:
                dfs(node.left, k)
            res.append(node.val)
            if node.right:
                dfs(node.right, k)
        res = []
        dfs(root, k)
        if len(res) < k:
            return None
        else:
            return res[k - 1]
# 树经常改变
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
