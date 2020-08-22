# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        # 用一个字典存储每一个子树 包括叶子节点 出现的频率 
        d = collections.defaultdict(list)
        def dfs(root):
            if not root: 
                return ''
            # 用"#"连接 根节点 左孩子 右孩子
            s = '#'.join((str(root.val), dfs(root.left), dfs(root.right)))
            # 遍历出来的每一个子树都放入字典，每次更新字典
            d[s].append(root)
            return s
        dfs(root)
        # 对字典里每一个value，也就是相同子树的集合，如果这个value的长度大于1，也就说明相同子树至少有两个，那么返回这个树
        return [l[0] for l in d.values() if len(l) > 1]

        
