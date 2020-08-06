# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 如果不是单值二叉树，则必定存在至少一对父子关系的结点，值不同。
# 1.递归访问左右子树。查看左右子树满足的情况
# 2.如果当前结点和左孩子或右孩子值不同，返回false
# 3.如果当前结点为空，则该路径上未存在不同的值，返回true

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root.left == None and root.right == None:
            return True
        elif root.left == None:
            if root.val != root.right.val:
                return False
            else:
                return self.isUnivalTree(root.right)
        elif root.right == None:
            if root.val != root.left.val:
                return False
            else:
                return self.isUnivalTree(root.left)
        elif root.left != None and root.right != None:
            if root.val != root.left.val or root.val != root.right.val:
                return False
            else:
                return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
            
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        else:
            if root.left and root.val != root.left.val:
                return False
            elif root.right and root.val != root.right.val:
                return False
            else:
                return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
