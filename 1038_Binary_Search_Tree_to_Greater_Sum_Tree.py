# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # 定义一个全局变量
    def __init__(self):
        self.total = 0
        
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return
        # 先遍历右子树 更新当前总和 并赋值给root
        self.convertBST(root.right)
        self.total += root.val
        root.val = self.total
        # 再遍历左子树
        self.convertBST(root.left)
        return root
    



