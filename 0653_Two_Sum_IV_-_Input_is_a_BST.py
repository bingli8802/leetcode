# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        # inOrder遍历 得到数组
        li = []
        def searchBST(root):
            if root == None:
                return
            searchBST(root.left)
            li.append(root.val)
            searchBST(root.right)
            return li
        res = searchBST(root)
        low = 0
        high = len(res) - 1
        while low < high:
            total = res[low] + res[high]
            if total == k:
                return True
            elif total < k:
                low += 1
            elif total > k:
                high -= 1
        return False
    
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """             
        def searchBST(root):
            if not root:
                return []
            return searchBST(root.left) + [root.val] + searchBST(root.right)
        res = searchBST(root)
        low, high = 0, len(res) - 1
        while low < high:
            total = res[low] + res[high]
            if total == k:
                return True
            elif total < k:
                low += 1
            elif total > k:
                high -= 1
        return False
        
        
        
