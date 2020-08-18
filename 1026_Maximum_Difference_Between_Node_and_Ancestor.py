# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.res = 0
        self.dfs(root, root.val, root.val)
        return self.res
    def dfs(self, root, maxValue, minValue):
        # 最大值和根节点比较
        maxValue = max(root.val, maxValue)
        # 最小值和根节点比较
        minValue = min(root.val, minValue)
        # 如果走到叶子节点 就用最大值减去最小值 与res比较
        if not root.left and not root.right:
            self.res = max(self.res, maxValue - minValue)
        # 如果不是叶子节点 递归查询左子树
        if root.left:
            self.dfs(root.left, maxValue, minValue)
        # 如果不是叶子节点 递归查询右子树
        if root.right:
            self.dfs(root.right, maxValue, minValue)
    
