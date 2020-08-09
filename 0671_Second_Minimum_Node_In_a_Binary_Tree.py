# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(root, val):
            # 如果根节点为空 返回-1
            if root == None:
                return -1
            # 如果根节点大于目标值 直接返回 因为根节点一定是最小的元素
            if root.val > val:
                return root.val
            # 一次找左右子树最小值
            left = helper(root.left, val)
            right = helper(root.right, val)
            if left < 0: 
                return right
            if right < 0: 
                return left
            # 每次递归结束都返回左右子树小的那个
            return min(left, right)
        
        return helper(root, root.val)

        
        
