# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        res_x = self.searchNode(root, x)
        res_y = self.searchNode(root, y)
        return res_x[0] == res_y[0] and res_x[1] != res_y[1]
    # 找parent节点和深度 广度优先 用queue
    def searchNode(self, root, node):
        queue = [root]
        level = 0
        while queue:
            level += 1
            nxt = []
            for q in queue:
                if q.val == node:
                    return [0, root]
                if q.left:
                    if q.left.val != node:
                        nxt.append(q.left)
                    else:
                        return [level, q]
                if q.right:
                    if q.right.val != node:
                        nxt.append(q.right)
                    else:
                        return [level, q]
            queue = nxt 


