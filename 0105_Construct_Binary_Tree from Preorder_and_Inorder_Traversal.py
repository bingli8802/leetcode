# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        # 数组长度为1时，直接返回即可
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        # 根据前序数组的第一个元素，创建根节点     
        root = TreeNode(preorder[0])
        # 用preorder[0]去中序数组中查找对应的元素 确定左右子树分界点
        middle = inorder.index(preorder[0])
        # 递归执行前序数组左边、中序数组左边
        root.left = self.buildTree(preorder[1:middle + 1],inorder[:middle])
        # 递归执行前序数组右边、中序数组右边
        root.right = self.buildTree(preorder[middle + 1:],inorder[middle + 1:])
        # 返回根节点
        return root
