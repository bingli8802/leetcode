# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        if root == None:
            return None
        mapper = set(to_delete)
        # 如果根节点就在待删除列表里 直接返回空list
        # 如果根节点不在里面 把根节点放入list
        ans = [] if root.val in mapper else [root]
        def dfs(node, parent, direction):
            if node == None:
                return None
            dfs(node.left, node, "left")
            dfs(node.right, node, "right")
            # 如果根节点在列表里
            if node.val in mapper:
                # 如果有左子树就把左子树放进ans
                if node.left:
                    ans.append(node.left)
                # 如果有右子树就把右子树放进ans
                if node.right:
                    ans.append(node.right)
                # 如果它是根节点的左子树 就把根节点的左子树更新为none
                if direction == "left":
                    parent.left = None
                # 如果它是根节点的右子树 就把根节点的右子树更新为none
                if direction == "right":
                    parent.right = None
        dfs(root, None, None)
        return ans
