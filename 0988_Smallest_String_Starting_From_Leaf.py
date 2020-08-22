# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# ans的初值为什么是‘~’
# 只要以大于'z'的字符开头的字符串，这个字符串就比字母字符串都要大，并不局限于“～” 字符串
class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        self.ans = "~"
        def dfs(node, A):
            if not node:
                return []
            # ord('a') = 97
            # chr(0+97) = 'a'
            A = A + [chr(node.val + ord('a'))]
            if not node.left and not node.right:
                self.ans = min(self.ans, "".join((A[::-1])))
            dfs(node.left, A)
            dfs(node.right, A)
        dfs(root, [])
        return self.ans
    
class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        def dfs(node, A):
            if node:
                A.append(chr(node.val + ord('a')))
                if not node.left and not node.right:
                    self.ans = min(self.ans, "".join((A[::-1])))
                dfs(node.left, A)
                dfs(node.right, A)
                A.pop()
        dfs(root, [])
        return self.ans

class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        paths = []
        def dfs(root, path=[]):
            if not (root.left or root.right):
                paths.append(''.join(chr(num + ord('a')) for num in path[::-1]))
            if root.left:
                dfs(root.left, path + [root.left.val])
            if root.right:
                dfs(root.right, path + [root.right.val])
        # run it
        dfs(root, [root.val])
        return min(paths)

