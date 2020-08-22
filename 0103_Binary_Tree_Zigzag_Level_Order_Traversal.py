# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# BFS 非递归
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        if not root:
            return ret
        ret.append([root.val])
        q = [root]
        flag = "right"
        while q:
            tmp = []
            if flag == "left":
                for i in q[::-1]:
                    if i.left:
                        tmp.append(i.left)
                    if i.right:
                        tmp.append(i.right)
                if len(tmp) > 0:
                    ret.append([node.val for node in tmp])
                q = tmp
                flag = "right"
                
            elif flag == "right":
                for i in q[::-1]:
                    if i.right:
                        tmp.append(i.right)
                    if i.left:
                        tmp.append(i.left)
                if len(tmp) > 0:
                    ret.append([node.val for node in tmp])
                q = tmp
                flag = "left"
        return ret
    
# 和正常的输出一样，如果为锯齿只需将结果反转即可
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """              
        res = []
        cur = [root]
        sign = False   # 设置反转标识
        while cur:
            curr_res = []
            next_node_list = []
            for node in cur:
                if node:
                    curr_res.append(node.val)
                    next_node_list.extend([node.left, node.right])

            if curr_res:
                if sign:
                    curr_res=curr_res[::-1]   #将结果反转，如果为从右到左。
                res.append(curr_res)
            cur = next_node_list
            sign = False if sign else True
        return res

