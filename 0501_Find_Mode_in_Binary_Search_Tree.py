# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        """中序遍历，O（1）空间复杂度"""
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            # 如果前一个节点存在：
            if self.pre:
                if self.pre.val == root.val:
                    self.curTimes += 1
                else:
                    self.curTimes = 1
            # 再比较当前节点个数的总数与最大值大小
            # 如果当前节点个数的总数与最大值一样 就把当前节点放进res
            if self.curTimes == self.maxTimes:
                self.res.append(root.val)
            # 如果当前节点个数的总数比最大值大 就把res清空 并把当前节点放进res 更新max值
            elif self.curTimes > self.maxTimes:
                del self.res[:]
                self.res.append(root.val)
                self.maxTimes = self.curTimes
            # 当前节点就是祖先了
            self.pre = root
            inorder(root.right)

        self.res = []
        self.pre = None
        self.curTimes = 1
        self.maxTimes = 0
        inorder(root)
        
        return self.res

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.mode = 0
        self.cnt = 1
        self.pre = None
        self.res = []
        self.inOrder(root)
        return self.res
    
    def inOrder(self, root):
        if root == None:
            return
        self.inOrder(root.left)
        
        if self.pre:
            if root.val == self.pre.val:
                self.cnt += 1
            elif root.val > self.pre.val:
                self.cnt = 1
        
        if self.mode == self.cnt:
            self.res.append(root.val)
        elif self.mode < self.cnt:
            del self.res[:]
            self.res.append(root.val)
            self.mode = self.cnt
        
        self.pre = root

        self.inOrder(root.right)

