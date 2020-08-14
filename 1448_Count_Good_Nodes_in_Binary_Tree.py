# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 注意节点可能是负数 curmax初始化 -float('inf')
        self.res = 0
        self.compareRoot(root,  -float('inf'))
        return self.res
    def compareRoot(self, root, curMax):
        if root == None:
            return 
        if root.val >= curMax:
            self.res += 1
            curMax = root.val
        self.compareRoot(root.left, curMax)
        self.compareRoot(root.right, curMax)
