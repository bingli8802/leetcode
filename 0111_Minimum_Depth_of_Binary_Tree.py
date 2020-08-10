# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 1.叶子节点的定义是左孩子和右孩子都为 null 时叫做叶子节点
# 2. 当 root 节点左右孩子都为空时，返回 1
# 3. 当 root 节点左右孩子有一个为空时，返回不为空的孩子节点的深度
# 4. 当 root 节点左右孩子都不为空时，返回左右孩子较小深度的节点值
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        # 1.左孩子和有孩子都为空的情况，说明到达了叶子节点，直接返回1即可
        if root.left == None and root.right == None:
            return 1
        # 2.如果左孩子和右孩子其中一个为空，那么需要返回比较大的那个孩子的深度 因为另一个孩子不是叶节点
        if root.left == None or root.right == None:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
        # 3. 左右孩子都不为空，返回最小深度+1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
