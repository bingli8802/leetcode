# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
class CBTInserter(object):
    # 先把没有左子树 或者 没有右子树的节点加到deque里面 全局变量self.deque
    def __init__(self, root):
        self.deque = []
        self.root = root
        q = [root]
        while q:
            node = q.pop(0)
            if not node.left or not node.right:
                self.deque.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    # deque当前为[3,4,5,6]            
    def insert(self, v):
        # 第一个节点是个要插入的坑
        node = self.deque[0]
        # 把待插入节点先append到队尾
        self.deque.append(TreeNode(v))
        # 如果第一个节点没有左子树 那么待插入节点就是新的左子树 
        if not node.left:
            node.left = self.deque[-1]
        # 如果第一个节点没有右子树 那么待插入节点就是新的右子树 这棵树就是满二叉树 需要把第一个节点pop出来
        # queue更新为[4,5,6]
        else:
            node.right = self.deque[-1]
            self.deque.pop(0)
        return node.val

    def get_root(self):
        return self.root
    
# 用deque代替list
class CBTInserter(object):
    # 先找到叶子节点
    def __init__(self, root):
        self.deque = collections.deque()
        self.root = root
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if not node.left or not node.right:
                self.deque.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    
    def insert(self, v):
        node = self.deque[0]
        self.deque.append(TreeNode(v))
        if not node.left:
            node.left = self.deque[-1]
        else:
            node.right = self.deque[-1]
            self.deque.popleft()
        return node.val

    def get_root(self):
        return self.root
    
# 用时太久
# class CBTInserter(object):
#     def __init__(self, root):
#         """
#         :type root: TreeNode
#         """
#         self.root = root
#     def insert(self, v):
#         """
#         :type v: int
#         :rtype: int
#         """
#         q = [self.root]
#         while q:
#             cur = q.pop(0)
#             if cur.left:
#                 q.append(cur.left)
#             if cur.right:
#                 q.append(cur.right)
#             if not cur.left:
#                 cur.left = TreeNode(v)
#                 break
#             if cur.left and not cur.right:
#                 cur.right = TreeNode(v)
#                 break
#         return cur.val
#     def get_root(self):
#         """
#         :rtype: TreeNode
#         """
#         return self.root

# # Your CBTInserter object will be instantiated and called as such:
# # obj = CBTInserter(root)
# # param_1 = obj.insert(v)
# # param_2 = obj.get_root()



