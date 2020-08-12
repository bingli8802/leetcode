# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        left = self.dfs(root1)
        right = self.dfs(root2)
        
        # mergesort
        ans, i, j = [], 0, 0
        while i < len(left) or j < len(right):
            if i < len(left) and (j == len(right) or left[i] <= right[j]):
                ans.append(left[i])
                i += 1
            else:
                ans.append(right[j])
                j += 1
        return ans
    # 遍历一棵树 把所有节点放进list
    def dfs(self, root):
        if root == None:
            return []
        else:
            # 注意递归的写法
            res = self.dfs(root.left) + [root.val] + self.dfs(root.right)
        return res
  

class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        def dfs(node, v):
            if not node:
                return
            dfs(node.left, v)
            v.append(node.val)
            dfs(node.right, v)
        # 递归结束后 v1 v2的值更新为两棵树的节点    
        v1, v2 = [], []
        dfs(root1, v1)
        dfs(root2, v2)
        
        ans, i, j = list(), 0, 0
        while i < len(v1) or j < len(v2):
            if i < len(v1) and (j == len(v2) or v1[i] <= v2[j]):
                ans.append(v1[i])
                i += 1
            else:
                ans.append(v2[j])
                j += 1
        return ans
