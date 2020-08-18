# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if not root1 and not root2:
            return True
        if not root1 or not root2 or root1.val != root2.val:
            return False
        left_left = self.flipEquiv(root1.left, root2.left)
        right_right = self.flipEquiv(root1.right, root2.right)
        left_right = self.flipEquiv(root1.left, root2.right)
        right_left = self.flipEquiv(root1.right, root2.left)
        return (left_left and right_right) or (left_right and right_left)

        
