# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if root == None:
            return []
        res = []
        queue = [root]
        
        while queue:
            # cur用来存储当前queue里面的值
            cur = []
            # nxt用来存储左右子树
            nxt = []
            for q in queue:
                # 每一次把queue里面的元素加进cur
                cur.append(q.val)
                # 判断q是否有左右子树 并放进nxt
                if q.left:
                    nxt.append(q.left)
                if q.right:
                    nxt.append(q.right)
            res.append(float(sum(cur)) / len(cur))
            # 下一次查找queue应该在nxt里面找
            queue = nxt
        return res
