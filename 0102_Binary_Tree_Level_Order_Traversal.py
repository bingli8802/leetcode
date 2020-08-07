# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [root]
        res = []
        
        while queue:
            cur = []
            nxt = []
            for q in queue:
                cur.append(q.val)
                if q.left:
                    nxt.append(q.left)
                if q.right:
                    nxt.append(q.right)
            res.append(cur)
            queue = nxt
        return res
            
