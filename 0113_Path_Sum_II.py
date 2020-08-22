# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 注意!
# 数组在python中为可变类型,path+[root.val]相当于从新创建了一个对象入栈
# 如果用append表示没有从新创建一个对象即原对象入栈，所以结果不对
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.res = []
        def dfs(root, path, total):
            if not root:
                return []
            total += root.val
            path = path + [root.val]     
            if not root.left and not root.right and total == sum:
                self.res.append(path) 
            dfs(root.left, path, total)
            dfs(root.right, path, total)
            
        dfs(root, [], 0)
        return self.res

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        self.res = []
        def dfs(root, total, path):
            total += root.val
            path = path + [root.val]
            if not root.left and not root.right and total == sum:
                self.res.append(path)
            if root.left:
                dfs(root.left, total, path)
            if root.right:
                dfs(root.right, total, path)
        dfs(root, 0, [])
        return self.res
