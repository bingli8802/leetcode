# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def inOrder(root):
            if root == None:
                return []
            else:
                return inOrder(root.left) + [root.val] + inOrder(root.right)
        li = inOrder(root)
        head = TreeNode(li[0])
        ans = head
        for i in range(1, len(li)):
            head.right = TreeNode(li[i])
            head = head.right
        return ans


