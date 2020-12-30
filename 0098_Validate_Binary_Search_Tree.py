# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # 东哥解法
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isValid(root, smallest, biggest):
            if root == None:
                return True
            if smallest != None and root.val <= smallest.val:
                return False
            if biggest != None and root.val >= biggest.val:
                return False
            print smallest, biggest
            # 左子树最大值应该是root的值
            # 右子树最小值应该是root的值
            return isValid(root.left, smallest, root) and isValid(root.right, root, biggest)
        return isValid(root, None, None)
