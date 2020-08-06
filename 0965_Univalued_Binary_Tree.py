# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root.left == None and root.right == None:
            return True
        elif root.left == None:
            if root.val != root.right.val:
                return False
            else:
                return self.isUnivalTree(root.right)
        elif root.right == None:
            if root.val != root.left.val:
                return False
            else:
                return self.isUnivalTree(root.left)
        elif root.left != None and root.right != None:
            if root.val != root.left.val or root.val != root.right.val:
                return False
            else:
                return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
            
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        else:
            if root.left and root.val != root.left.val:
                return False
            elif root.right and root.val != root.right.val:
                return False
            else:
                return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
