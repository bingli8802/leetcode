# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 一个节点上的 金币数 - 1 称为过载量，那么有以下公式：
# 节点的过载量 = 左节点的过载量 + 右节点过载量 + 节点金币数 - 1
# 移动次数其实就等于每次递归时，左右节点过载量的绝对值之和
class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        def moveCount(node):
            if node == None:
                return 0
            # L是左子树应该走的总共步数
            # R是右子树应该走的总共步数
            L = moveCount(node.left)
            R = moveCount(node.right)
            # 更新ans的值 - 加上左右子树应该走的步数
            self.ans += abs(L) + abs(R)
            # 计算当前节点应该走多少步数 并返回这个值
            move = node.val + L + R - 1
            return move
        moveCount(root)
        return self.ans
