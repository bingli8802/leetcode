# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 做法不对
# 想法是找到p q的根节点 再比较
# class Solution(object):
#     def lowestCommonAncestor(self, root, p, q):
#         """
#         :type root: TreeNode
#         :type p: TreeNode
#         :type q: TreeNode
#         :rtype: TreeNode
#         """
#         self.roots = []     
#         p_roots = self.getRoots(root, p.val)
#         self.roots = []
#         q_roots = self.getRoots(root, q.val)

#     # 找到target所有根节点 
#     def getRoots(self, root, target):
#         if target < root.val:
#             self.roots.append(root.val)
#             self.getRoots(root.left, target)
#         elif target > root.val:
#             self.roots.append(root.val)
#             self.getRoots(root.right, target)
#         elif target == root.val:
#             self.roots.append(root.val)
#             # return self.roots
#         return self.roots

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        parent_val = root.val
        p_val = p.val
        q_val = q.val
        
        # If both p and q are greater than parent
        if p_val > parent_val and q_val > parent_val:    
            return self.lowestCommonAncestor(root.right, p, q)
        # If both p and q are lesser than parent
        elif p_val < parent_val and q_val < parent_val:    
            return self.lowestCommonAncestor(root.left, p, q)
        # We have found the split point, i.e. the LCA node.
        else:
            return root
            
            
            
            
            
            
            
