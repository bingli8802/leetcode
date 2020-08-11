# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.total = 0
        self.deepest = 0
        self.dfs(root, 0)
        return self.total
    def dfs(self, root, level):
        if root == None:
            return 
        if root.left == None and root.right == None:
            if level > self.deepest:
                self.deepest = level
                self.total = root.val
            elif level == self.deepest:
                self.total += root.val
            else:
                return
        self.dfs(root.left, level + 1)
        self.dfs(root.right, level + 1)
            
