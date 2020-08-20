# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# BFS
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return None
        res = []
        q = [root]
        while q:
            tmp = []
            res.append(q[-1].val)
            for i in q:
                if i.left:
                    tmp.append(i.left)
                if i.right:
                    tmp.append(i.right)
            q = tmp
        return res
# DFS
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def dfs(root, depth):
            if not root:
                return 
            if len(res) <= depth:
                res.append(0)
            res[depth] = root.val
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
        
        dfs(root, 0)
        return res

