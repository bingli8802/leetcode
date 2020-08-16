# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 用前序遍历的第一个元素创建出根节点
# 用前序遍历的第二个元素x，去后序遍历中找对应的下标y，将y+1就能得到左子树的个数了
# 将前序数组，后序数组拆分左右两部分
# 递归的处理前序数组左边、后序数组右边
# 递归的处理前序数组右边、后序数组右边
# 返回根节点
class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        if not pre:
            return None
        # 数组长度为1时，直接返回即可
        if len(pre) == 1:
            return TreeNode(pre[0])
        # 根据前序数组的第一个元素，创建根节点     
        root = TreeNode(pre[0])
        # 根据前序数组第二个元素，确定后序数组左子树范围
        left_count = post.index(pre[1]) + 1
        # 递归执行前序数组左边、后序数组左边
        root.left = self.constructFromPrePost(pre[1:left_count + 1],post[:left_count])
        # 递归执行前序数组右边、后序数组右边
        root.right = self.constructFromPrePost(pre[left_count + 1:],post[left_count:-1])
        # 返回根节点
        return root

class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        def dfs(pre, post):
            if not pre:
                return None
            # 数组长度为1时，直接返回即可
            if len(pre) == 1:
                return TreeNode(pre[0])
            # 根据前序数组的第一个元素，创建根节点     
            root = TreeNode(pre[0])
            # 根据前序数组第二个元素，确定后序数组左子树范围
            left_count = post.index(pre[1]) + 1
            # 递归执行前序数组左边、后序数组左边
            root.left = dfs(pre[1:left_count + 1],post[:left_count])
            # 递归执行前序数组右边、后序数组右边
            root.right = dfs(pre[left_count + 1:],post[left_count:-1])
            # 返回根节点
            return root
        return dfs(pre,post)
        
