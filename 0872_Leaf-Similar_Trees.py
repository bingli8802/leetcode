# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        x = self.getLeaf(root1, [])
        y = self.getLeaf(root2, [])
        return x == y
    
    def getLeaf(self, root, res):
        if root == None:
            return
        if root.left == None and root.right == None:
            res.append(root.val)
        else:
            self.getLeaf(root.left, res)
            self.getLeaf(root.right, res)
        return res

