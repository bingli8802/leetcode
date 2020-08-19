# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # 如果当前节点为none 或者当前节点的值等于p，q 那么直接返回当前节点值
        if not root or root.val == p or root.val == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # 如果左子树为none，返回右子树的值
        if not left:
            return right
        # 如果右子树为none，返回左子树的值
        if not right:
            return left
        # 只有当左右子树都存在 表示p和q就在当前根节点两边 返回当前根节点
        if left and right:
            return root
