# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        min_val = 10000
        res = self.getNodes(root)
        for i in range(len(res) - 1):
            min_val = min(res[i + 1] - res[i], min_val)
        return min_val
    # 中序遍历得到节点 已排好序
    def getNodes(self, root):
        if root == None:
            return []
        return self.getNodes(root.left) + [root.val] + self.getNodes(root.right)
