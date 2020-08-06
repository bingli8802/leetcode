# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 方法更快
class Solution(object):
    # 类函数
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        paths = []
        # 普通函数
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
        # 调用函数
        getPath(root, "")
        return paths

class Solution(object):
    # 类函数
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        # 定义全局变量self.paths
        self.paths = []
        # 调用函数
        self.getPath(root, "")
        return self.paths
    # 类函数
    def getPath(self, root, path):
        # 如果根节点不为空 首先把根节点加到返回的string上 更新path
        if root:
            path += str(root.val)
            # 如果根节点的左右子树都是空 就把当前path的值append到list 并返回
            if not root.left and not root.right:
                self.paths.append(path)
            # 如果根节点的左右子树不都为空 就把"->"加到path后面 递归左右子树
            else:
                path += "->"
                self.getPath(root.left, path)
                self.getPath(root.right, path)

