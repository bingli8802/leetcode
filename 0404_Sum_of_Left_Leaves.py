# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    res = 0
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """ 
        if root == None:
            return 0
        # 确定左节点
        if root.left and root.left.left == None and root.left.right == None:
            self.res += root.left.val
        # 访问左节点
        self.sumOfLeftLeaves(root.left)
        # 访问右节点
        self.sumOfLeftLeaves(root.right)
        return self.res

