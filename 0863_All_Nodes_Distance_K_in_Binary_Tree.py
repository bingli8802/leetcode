# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        # DFS - 给树的每个节点添加一个父节点指针
        def dfs(cur, parent):
            if cur:
                cur.parent = parent
                dfs(cur.left, cur)
                dfs(cur.right, cur)
        dfs(root, None)
        
        # BFS - q队列用来记录从target这个节点出发 它的父节点 左子树 右子树 与target距离
        q = [(target, 0)]
        # seen用来记录那些点已经遍历过
        seen = [target]
        while q:
            # 如果发现distance和k相等 那么当前q里所有元素和target的距离都应该是k
            if q[0][1] == K:
                return [node.val for node, distane in q]
            node, distance = q.pop(0)
            for n in (node.parent, node.left, node.right):
                if n and (n not in seen):
                    q.append((n, distance + 1))
                    seen.append(n)
        return []
