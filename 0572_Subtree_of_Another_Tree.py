# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s == t == None:
            return True
        elif s == None or t == None:
            return False
        # 首先判断根节点s和t是否一样 不一样的话在判断s的左子树是否和t一样 再判断右子树
        return self.isSame(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSame(self, ss, tt):
        if ss == tt == None:
            return True
        elif ss == None or tt == None:
            return False
        return ss.val == tt.val and self.isSame(ss.left, tt.left) and self.isSame(ss.right, tt.right)
            
