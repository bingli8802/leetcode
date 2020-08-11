class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        self.arrow_len(root)
        return self.ans
    
    def arrow_len(self, node):
        if not node:
            return 0
        left = self.arrow_len(node.left)
        right = self.arrow_len(node.right)
        # 初始化两边同值路径都是0 因为不知道左右节点是否和根节点相等
        left_arrow = right_arrow = 0
        # 如果左子树和根节点一样的话 左边路径加1
        if node.left and node.left.val == node.val:
            left_arrow = left + 1
        # 如果右子树和根节点一样的话 右边路径加1
        if node.right and node.right.val == node.val:
            right_arrow = right + 1
        # 更新返回值 也就是左右子树最长同值路径的和
        self.ans = max(self.ans, left_arrow + right_arrow)
        # 递归结束的时候 返回左子树/右子树已计算过的同值路径长的那个
        return max(left_arrow, right_arrow)
