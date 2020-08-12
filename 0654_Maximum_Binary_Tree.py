# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        max_num = max(nums)
        mid_idx = nums.index(max_num)
        # 当前root指向最大值
        root = TreeNode(max_num)
        left = nums[:mid_idx]
        right = nums[(mid_idx + 1):]
        root.left = self.constructMaximumBinaryTree(left)
        root.right = self.constructMaximumBinaryTree(right)
        # 递归返回的是root
        return root
