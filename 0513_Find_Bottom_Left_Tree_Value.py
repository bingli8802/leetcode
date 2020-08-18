# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# DFS 递归
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, depth):
            if not root:
                return None
            # 如果当前深度大于最大深度 就把最大深度更新 res更新为当前root的值
            if depth > self.max_depth :
                self.max_depth = depth
                self.res = root.val
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
        self.max_depth = -1
        self.res = 0
        dfs(root, 0)
        return self.res

# BFS 层序遍历的最后一个节点就是要找的节点 注意先把右子树入队 再把左子树入队
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return None
        q = [root]
        while q:
            cur = q.pop(0)
            if cur.right:
                q.append(cur.right)
            if cur.left:
                q.append(cur.left)
        return cur.val
        
