# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
# 树经常改变怎么办？
# 树不变
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def dfs(node):
            if not node:
                return None
            if node.left:
                dfs(node.left)
            res.append(node.val)
            if node.right:
                dfs(node.right)
        res = []
        dfs(root)
        if len(res) < k:
            return None
        else:
            return res[k - 1]
    # 东哥解法   
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.rank = 0
        self.res = 0
        def dfs(node):
            if not node:
                return None
            if node.left:
                dfs(node.left)
            self.rank += 1
            if k == self.rank:
                self.res = node.val
                return
            if node.right:
                dfs(node.right)
        dfs(root)
        return self.res
