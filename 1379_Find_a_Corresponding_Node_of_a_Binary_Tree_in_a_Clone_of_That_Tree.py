# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 使用原函数递归 返回res
# class Solution(object):
#     def getTargetCopy(self, original, cloned, target):
#         """
#         :type original: TreeNode
#         :type cloned: TreeNode
#         :type target: TreeNode
#         :rtype: TreeNode
#         """
#         if not original:
#             return None
#         if original == target:
#             return cloned
#         res = self.getTargetCopy(original.left,cloned.left,target)
#         if res:
#             return res
#         else:
#             return self.getTargetCopy(original.right,cloned.right,target)

# 构造一个函数递归 返回res 
# 缺点是遍历所有节点
class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        def helper(root):
            print root
            if not root:
                return None
            if root.val == target.val:
                self.res = root
            helper(root.left)
            helper(root.right)
        helper(cloned)
        return self.res


