# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 迭代 无递归
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        n = len(preorder)
        if not n:
            return None
        root = TreeNode(preorder[0])         
        stack = [root] 
        for i in range(1, n):
            parent = stack[-1]
            child = TreeNode(preorder[i])
            while stack and stack[-1].val < child.val:
                parent = stack.pop()
            if parent.val > child.val:
                parent.left = child
            else:
                parent.right = child
            stack.append(child)
        return root
# 迭代 无递归2
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        n = len(preorder)
        if not n:
            return None
        root = TreeNode(preorder[0])         
        stack = [root] 
        for i in range(1, n):
            parent = stack[-1]
            child = TreeNode(preorder[i])
            if parent.val > child.val:
                parent.left = child
            else:         
                while stack and stack[-1].val < child.val:
                    parent = stack.pop()
                parent.right = child
            stack.append(child)
        return root
# 递归插入节点
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None
        # 创建一个树 根节点的值等于preorder[0]
        root = TreeNode(preorder[0])
        # 循环插入剩下节点
        for i in range(1, len(preorder)):
            self.insertTarget(root, preorder[i])
        return root
    
    def insertTarget(self, root, target):
        # 递归结束条件：当root为空 返回以target为值的子树
        if root == None:
            return TreeNode(target)
        elif root.val > target:
            root.left = self.insertTarget(root.left, target)
        else:
            root.right = self.insertTarget(root.right, target)
        return root
