# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS自己做的
class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        total = 0
        if root == None:
            return 0
        q = [root]
        while q:
            root = q.pop()
            if root.left:
                q.append(root.left)
                if root.val % 2 == 0 and root.left.left:
                    total += root.left.left.val
                if root.val % 2 == 0 and root.left.right:
                    total += root.left.right.val
            if root.right:
                q.append(root.right)
                if root.val % 2 == 0 and root.right.left:
                    total += root.right.left.val
                if root.val % 2 == 0 and root.right.right:
                    total += root.right.right.val
        return total
# DFS
class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.ans = 0
        self.dfs(None, None, root)
        return self.ans
    
    def dfs(self, grandparent, parent, node):
        if node == None:
            return
        if grandparent != None and grandparent.val % 2 == 0:
            self.ans += node.val
        self.dfs(parent, node, node.left)
        self.dfs(parent, node, node.right)
# DFS
class Solution:
    def sumEvenGrandparent(self, root):
        self.ans = 0
        self.dfs(1, 1, root)
        return self.ans
    def dfs(self, gp_val, p_val, node):
        if not node:
            return
        if gp_val % 2 == 0:
            # nonlocal ans
            self.ans += node.val
        self.dfs(p_val, node.val, node.left)
        self.dfs(p_val, node.val, node.right)
        


            
