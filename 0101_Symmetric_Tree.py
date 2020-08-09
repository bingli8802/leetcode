# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursively 递归
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isEqual(root, root)
    
    def isEqual(self, left, right):
        if left == right == None:
            return True
        elif left == None or right == None:
            return False 
        return left.val == right.val and self.isEqual(left.left, right.right) and self.isEqual(left.right, right.left)

# iteratively 迭代
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = []
        if root == None:
            return True
        queue.append(root.left)
        queue.append(root.right)
        while queue:
            left = queue.pop(0)
            right = queue.pop(0)
            if left == None and right == None:
                continue
            if left == None or right == None:
                return False
            if left.val != right.val:
                return False
            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)
        return True
