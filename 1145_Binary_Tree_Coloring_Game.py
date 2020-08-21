# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 1. 树会被红色节点分成三部分 
# 2. 在红色节点的 （父节点 左 右 ）节点里面 找一个节点并且这个节点所在连通分量的节点树大于n/2
class Solution(object):
    def btreeGameWinningMove(self, root, n, x):
        """
        :type root: TreeNode
        :type n: int
        :type x: int
        :rtype: bool
        """
        self.red_left = 0
        self.red_right = 0
        def count_nodes(root):
            if not root:
                return 0
            left = count_nodes(root.left)
            right = count_nodes(root.right)
            if root.val == x:
                self.red_left = left
                self.red_right = right
            return left + right + 1
        count_nodes(root)
        red_parent = n - 1 - self.red_left - self.red_right
        potential_node = max(red_parent, self.red_left, self.red_right)
        if potential_node > n - potential_node:
            return True
        else:
            return False
