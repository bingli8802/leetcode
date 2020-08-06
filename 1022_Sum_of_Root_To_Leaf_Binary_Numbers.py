# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 两个类函数
class Solution(object):
    # 类函数
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        return self.sumHelper(root, 0)
    # 类函数
    def sumHelper(self, root, num):
        if not root:
            return 0
        else:
            num = num * 2 + root.val
            if root.left == None and root.right == None:
                return num
            else:
                return (self.sumHelper(root.left, num) + self.sumHelper(root.right, num)) % (10 ** 9 + 7)
# 两个类函数
class Solution(object):
    # 类函数
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        self.sumHelper(root, 0)
        return self.ans % (10 ** 9 + 7)
    # 类函数
    def sumHelper(self, root, num):
        if not root:
            return 0
        else:
            num = num * 2 + root.val
            if root.left == None and root.right == None:
                self.ans += num
            else:
                self.sumHelper(root.left, num)
                self.sumHelper(root.right, num)

class Solution(object):
    # 类函数
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        # 普通函数
        def sumHelper(root, num):
            if not root:
                return 0
            else:
                num = num * 2 + root.val
                if root.left == None and root.right == None:
                    self.ans += num
                else:
                    sumHelper(root.left, num)
                    sumHelper(root.right, num)
        sumHelper(root, 0)
        return self.ans % (10 ** 9 + 7)

