# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def dfs(root):
            if root == None:
                return None, 0
            left_root, left_depth = dfs(root.left)
            right_root, right_depth = dfs(root.right)
            if left_depth > right_depth:
                return left_root, left_depth + 1
            elif left_depth < right_depth:
                return right_root, right_depth + 1
            else:
                return root, left_depth + 1
        res, height = dfs(root)
        return res
