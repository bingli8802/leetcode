# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max = 0
        self.traverse(root)
        return self.max
    
    def traverse(self, root):
        if root == None:
            return 0
        l_hight = self.traverse(root.left)
        r_hight = self.traverse(root.right)
        # 对于树上每个节点都要比较其左子树和右子树之和与max之间大小 并更新max
        self.max = max(self.max, l_hight + r_hight)
        # 返回的是高度
        return max(l_hight, r_hight) + 1
