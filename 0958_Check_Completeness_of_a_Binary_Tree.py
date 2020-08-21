# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q = [root]
        for i in range(100):
            node = q.pop(0)
            # 当遇到第一个none 判断q里面是不是所有元素都是none 如果不是 就说明右边还有节点
            if node == None:
                if set(q) == {None}:
                    return True
                else:
                    return False
            # 把root左右子树都入队 不论是否为none
            q.append(node.left)
            q.append(node.right)
