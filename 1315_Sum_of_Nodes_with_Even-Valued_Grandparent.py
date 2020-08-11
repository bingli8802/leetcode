# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        total = 0
        if root == None:
            return 0
        q = [root]
        while q:
            root = q.pop()
            if root.left:
                q.append(root.left)
                if root.val % 2 == 0 and root.left.left:
                    total += root.left.left.val
                if root.val % 2 == 0 and root.left.right:
                    total += root.left.right.val
            if root.right:
                q.append(root.right)
                if root.val % 2 == 0 and root.right.left:
                    total += root.right.left.val
                if root.val % 2 == 0 and root.right.right:
                    total += root.right.right.val
        return total
            
