# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None
        root = TreeNode(postorder[-1])
        middle = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:middle], postorder[:middle])
        root.right = self.buildTree(inorder[middle + 1:], postorder[middle:-1])
        return root
