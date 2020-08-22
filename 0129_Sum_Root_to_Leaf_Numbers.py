# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.total = 0
        # 每次传递走过的路径 记录下来
        def dfs(root, path):
            if not root:
                return ''
            path += str(root.val)
            # 遇到叶子节点就把total更新
            if not root.left and not root.right:
                self.total += int(path)
            dfs(root.left, path)
            dfs(root.right, path)
        dfs(root, '')
        return self.total
