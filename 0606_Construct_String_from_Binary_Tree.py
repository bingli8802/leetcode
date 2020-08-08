# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t == None:
            return ""
        # 左右子树都为空 只返回当前root的值
        if t.left == None and t.right == None:
            return str(t.val)
        # 如果只有右子树为空 返回当前 root + root.left 递归
        if t.left and not t.right:
            return str(t.val) + "(" + self.tree2str(t.left) + ")"
        else:
            return str(t.val) + "(" + self.tree2str(t.left) + ")" + "(" + self.tree2str(t.right) + ")"
