# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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
        # 如果p和q都比root大 就在右子树搜索
        if p_val > parent_val and q_val > parent_val:    
            return self.lowestCommonAncestor(root.right, p, q)
        # 如果p和q都比root小 就在左子树搜索
        elif p_val < parent_val and q_val < parent_val:    
            return self.lowestCommonAncestor(root.left, p, q)
        # 如果p小于root，q大于root 那么这个节点就是root
        else:
            return root
            
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
            
            
            
            
            
            
