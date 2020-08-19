# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 递归
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.nodes = self.dfs(root)
        
    def dfs(self, root):
        if root == None:
            return []
        return self.dfs(root.left) + [root.val] + self.dfs(root.right)
        
    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        if self.hasNext:
            return self.nodes.pop(0)

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return len(self.nodes) != 0
# 迭代
class BSTIterator:
    def __init__(self, root):     
        # Stack for the recursion simulation
        self.stack = []  
        # Remember that the algorithm starts with a call to the helper function
        # with the root node as the input
        self._leftmost_inorder(root)
        
    def _leftmost_inorder(self, root): 
        # For a given node, add all the elements in the leftmost branch of the tree
        # under it to the stack.
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        """
        @return the next smallest number
        """
        # Node at the top of the stack is the next smallest element
        topmost_node = self.stack.pop()  
        # Need to maintain the invariant. If the node has a right child, call the 
        # helper function for the right child
        if topmost_node.right:
            self._leftmost_inorder(topmost_node.right)
        return topmost_node.val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
