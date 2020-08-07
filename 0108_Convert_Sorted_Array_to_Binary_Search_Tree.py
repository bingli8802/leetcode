# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.treeGenerator(nums, 0, len(nums) - 1)
    def treeGenerator(self, nums, low, high):
        if low > high:
            return
        mid = (low + high)/2
        # 当前根节点是数组中间值
        root = TreeNode(nums[mid])
        # 左节点递归
        root.left = self.treeGenerator(nums, low, mid - 1)
        # 右节点递归
        root.right = self.treeGenerator(nums, mid + 1, high)
        return root
    
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def treeGenerator(low, high):
            if low > high:
                return
            mid = (low + high)/2
            root = TreeNode(nums[mid])
            root.left = treeGenerator(low, mid - 1)
            root.right = treeGenerator(mid + 1, high)
            return root
        return treeGenerator(0, len(nums) - 1)
