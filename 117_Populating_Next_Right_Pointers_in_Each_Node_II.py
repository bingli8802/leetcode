"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
BFS
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root == None:
            return None
        q = [root]
        while q:
            nxt = []
            for i in range(len(q)):
                if i == len(q) - 1:
                    q[i].next = None
                else:
                    q[i].next = q[i + 1]
                if q[i].left:
                    nxt.append(q[i].left)
                if q[i].right:
                    nxt.append(q[i].right)
            q = nxt
        return root
# DFS
# 怎么得到每次的开头的节点呢？我们用一个dummy指针，当连接第一个节点的时候，就将dummy指针指向
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        cur = root
        while cur != None:
            dummy = Node()
            tail = dummy
        # 遍历 cur 的当前层
            while cur != None:
                if cur.left != None:
                    tail.next = cur.left
                    tail = tail.next
                if cur.right != None:
                    tail.next = cur.right
                    tail = tail.next
                cur = cur.next
            # 更新 cur 到下一层
            cur = dummy.next
        return root
