# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# BFS
class Solution(object):
    def largestValues(self, root):
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
            # 定义负无穷
            max_val = float("-inf")
            for cur in q:
                # 找每行最大值
                max_val = max(max_val, cur.val)
                # 把左子树 右子树入队
                if cur.left:
                    tmp.append(cur.left)
                if cur.right:
                    tmp.append(cur.right)
            res.append(max_val)
            # 更新队列q
            q = tmp
        return res
                    
