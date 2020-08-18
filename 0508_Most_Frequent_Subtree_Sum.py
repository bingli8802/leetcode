# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        from collections import defaultdict
        tree_dict = defaultdict(int)
        
        def dfs(root):
            if not root:
                return 0
            sum = dfs(root.left) + root.val + dfs(root.right)
            tree_dict[sum] = tree_dict.get(sum, 0) + 1
            return sum
        dfs(root)
        
        # 记录出现最多次的 子树的元素和
        tree_max = 0
        # python 通过 dict.values() 遍历出字典中的 value 
        for cnt in tree_dict.values():
            tree_max = max(cnt,tree_max)
        res_list = []
        # python 通过 dict.items() 遍历出字典中的key 和 value
        for key, val in tree_dict.items():
            if val == tree_max:
                res_list.append(key)
        return res_list

