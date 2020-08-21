# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 每个节点都设置：[偷收益, 不偷收益]
# 每一个节点的偷收益值都是：左侧子节点的不偷值 + 右侧子节点的不偷值 + 该节点的值
# 每一个节点的不偷收益值都是： 左侧子节点的最大值 + 右侧子节点的最大值
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(root):
            if not root:
                return 0, 0
            left = helper(root.left)
            right = helper(root.right)
            # 如果抢当前节点, 则左右子树都不能抢
            v1 = root.val + left[1] + right[1]
            # 如果不抢当前节点,因为左右子树可以选择抢或者不抢，所以分别取左子树中抢或者不抢最大的值 + 右子树抢或者不抢最大值
            v2 = max(left) + max(right)
            return v1, v2
        return max(helper(root))    
    
#         def _rob(root):
#             if not root: 
#                 return 0, 0  # 偷，不偷
#             left = _rob(root.left)
#             right = _rob(root.right)
#             # 如果偷当前节点, 则左右子树都不能偷
#             v1 = root.val + left[1] + right[1]
#             # 如果不偷当前节点,因为左右子树可以选择偷或者不偷，所以分别取左子树中偷或者不偷最大的值 + 右子树偷或者不偷最大值
#             v2 = max(left) + max(right)
#             return v1, v2
#         return max(_rob(root))
