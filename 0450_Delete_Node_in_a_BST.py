# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        def insert(left, right):
            if not left:
                return right
            if not right:
                return left
            if left and right:
                right_most = left.right
                if right_most:
                    while right_most.right:
                        right_most = right_most.right
                    right_most.right = right
                else:
                    left.right = right
                return left
        def dfs(root):
            if not root:
                return None
            if root.val == key:
                root = insert(root.left, root.right)
            elif root.left and root.left.val == key:
                root.left = insert(root.left.left, root.left.right)
            elif root.right and root.right.val == key:
                root.right = insert(root.right.left, root.right.right)
            
            # if root:
            #     dfs(root.left)
            #     dfs(root.right)
            return root
        # dfs(root)
        return dfs(root)

