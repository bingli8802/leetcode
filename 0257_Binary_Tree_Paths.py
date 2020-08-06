# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def getPath(root, path):
            # 如果根节点不为空 首先把根节点加到返回的string上 更新path
            if root:
                path += str(root.val)
                # 如果根节点的左右子树都是空 就把当前path的值append到list 并返回
                if not root.left and not root.right:
                    paths.append(path)
                # 如果根节点的左右子树不都为空 就把"->"加到path后面 递归左右子树
                else:
                    path += "->"
                    getPath(root.left, path)
                    getPath(root.right, path)
        paths = []
        # 调用函数
        getPath(root, "")
        return paths
