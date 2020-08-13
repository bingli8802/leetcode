# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 花花酱题解
class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N == 1:
            return [TreeNode(0)]
        # 如果N是奇数 直接返回空
        if N % 2 == 0:
            return []
        ans = []
        # i代表着给左节点分配的数值 1，3，5，7，..., N-1
        for i in range(1, N, 2):
            # l代表着左节点可能的组合
            for l in self.allPossibleFBT(i):
                # r代表着右节点可能的组合
                for r in self.allPossibleFBT(N - i - 1):
                    root = TreeNode(0)
                    root.left = l
                    root.right = r
                    ans.append(root)
        return ans
