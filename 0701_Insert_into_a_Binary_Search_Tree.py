# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root == None:
            root = TreeNode(val)
        if val < root.val and root.left:
            self.insertIntoBST(root.left, val)
        elif val < root.val and not root.left:
            root.left = TreeNode(val)
        if val > root.val and root.right:
            self.insertIntoBST(root.right, val)
        elif val > root.val and not root.right:
            root.right = TreeNode(val)
        return root

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root == None:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        elif val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        return root
