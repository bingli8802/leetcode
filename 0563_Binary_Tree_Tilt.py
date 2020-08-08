# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 1.要计算每个节点的坡度，就要计算每个节点的 左子树的节点之和 与 右子树的节点之和；
# 2.左子树的节点之和 = 左子树根节点的值 + 左子树的左子树节点之和 + 左子树的右子树节点之和；
# 3.继续这样分解下去，直到分解到空树，空树的节点之和为0，作为递归出口。

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 定义一个全局变量 tilt
        self.tilt = 0
        # 遍历树
        self.traverse(root)
        # 返回tilt的值
        return self.tilt
    
    def traverse(self, root):
        # 遇到根节点返回0
        if root == None:
            return 0
        # 遍历左子树
        left = self.traverse(root.left)
        # 遍历右子树
        right = self.traverse(root.right)
        # 更新tilt的值
        self.tilt += abs(left - right)
        # 更新root节点的值
        return root.val + left + right



            
