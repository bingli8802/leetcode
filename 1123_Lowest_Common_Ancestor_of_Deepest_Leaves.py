# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def dfs(root):
            if root == None:
                return None, 0
            # 左子树的根，左子树的深度
            left_root, left_dep = dfs(root.left)
            # 右子树的根，右子树的深度
            right_root, right_dep = dfs(root.right)
            # 如果左子树深度大于右子树 返回 左子树，左子树深度加1
            if left_dep > right_dep:
                return left_root, left_dep + 1
            # 如果右子树深度大于左子树 返回 右子树，右子树深度加1
            elif left_dep < right_dep:
                return right_root, right_dep + 1
            # 如果左右子树深度相同 返回根节点
            else:
                return root, left_dep + 1
        res, height = dfs(root)
        return res

