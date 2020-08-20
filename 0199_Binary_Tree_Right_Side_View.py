# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
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
