"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
# 广度优先bfs O(n) 
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        queue = [root]  # 保存下一层的节点  
        while queue:
            nxt = []
            for i in range(len(queue)):
                '''依次用next指向同层下一个节点'''
                if i == len(queue)-1:
                    queue[i].next = None
                else:
                    queue[i].next = queue[i+1]           
                if queue[i].left:
                    nxt.append(queue[i].left)
                if queue[i].right:
                    nxt.append(queue[i].right)                  
            queue = nxt  # 每次更新queue           
        return root
# DFS O(n)
# Initially, all next pointers are set to NULL 初始化每个节点next都是none
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root == None:
            return None
        if root.left:
            root.left.next = root.right
        if root.right and root.next != None:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root
# iterative O(1)
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root == None:
            return None
        leftmost = root
        # Once we reach the final level, we are done
        # 因为每次都是在parent level把左右子树的next找到 所以如果root没有左子树的话就停止
        while leftmost.left:
            head = leftmost
            # 每次都是在parent level把左右子树的next找到
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            leftmost = leftmost.left
        return root
        
