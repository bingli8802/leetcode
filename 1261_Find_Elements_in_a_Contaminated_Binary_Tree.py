# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS做法
class FindElements(object):
    def __init__(self, root):
        self.nums = set()
        # BFS
        root.val = 0
        # queue = collections.deque([root])
        queue = [root]
        while queue:
            node = queue.pop()
            self.nums.add(node.val)
            if node.left:
                node.left.val = 2 * node.val + 1
                queue.append(node.left)
            if node.right:
                node.right.val = 2 * node.val + 2
                queue.append(node.right)
    def find(self, target):
        return target in self.nums
# DFS做法
class FindElements(object):
    def __init__(self, root):
        self.nums = set()
        DFS
        root.val = 0
        def helper(root):
            self.nums.add(root.val)
            if not root.left and not root.right:
                return
            if root.left:
                root.left.val = 2 * root.val + 1
                helper(root.left)
            if root.right:
                root.right.val = 2 * root.val + 2
                helper(root.right)
        helper(root)

    def find(self, target):
        return target in self.nums
# DFS做法  
class FindElements:
    def __init__(self, root):
        self.elems = set()

        def dfs(node, val):
            if node:
                node.val = val
                self.elems.add(val)
                dfs(node.left, val * 2 + 1)
                dfs(node.right, val * 2 + 2)
        dfs(root, 0)

    def find(self, target):
        return target in self.elems

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
