# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# BFS 容易做出来
class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            v1 = TreeNode(v)
            v1.left = root
            return v1        
        height = 1
        q = [root]
        while height < d - 1:
            height += 1
            tmp = []
            for i in q:
                if i.left:
                    tmp.append(i.left)
                if i.right:
                    tmp.append(i.right)
            q = tmp
        for i in q:
            v1 = TreeNode(v)
            v2 = TreeNode(v)
            v1.left = i.left
            v2.right = i.right
            i.left = v1
            i.right = v2
        return root

# DFS
class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1: # 当d==1的时候，d-1不存在，则创建一个新的根节点 v，原先的整棵树将作为 v 的左子树。
            t = TreeNode(v)
            t.left = root
            return t

        def dfs(root, depth, d, val):
            if root is None: # 终止条件
                return 
            if depth == d - 1: # 如果递归的深度等于d-1
                temp_left, temp_right = root.left, root.right # 临时变量
                root.left = TreeNode(val)
                root.right = TreeNode(val)
                root.left.left = temp_left
                root.right.right = temp_right
            else: # 对左右子树递归
                dfs(root.left, depth + 1, d, val)
                dfs(root.right, depth + 1, d, val)
            return root

        return dfs(root, 1, d, v)



