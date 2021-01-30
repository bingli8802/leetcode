"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """  
        if not head:
            return None
        cur = head
        # 创建一个哈希表，key是原节点，value是新节点 
        dic = {}
        # 将原节点和新节点放入哈希表中
        while cur:
            node = Node(cur.val)
            dic[cur] = node
            print dic
            cur = cur.next
        cur = head
        # 遍历原链表，设置新节点的next和random
        while cur:
            # cur是原节点，d[cur]是对应的新节点，cur.next是原节点的下一个
            # d[cur.next]是原节点下一个对应的新节点
            if cur.next:
                dic[cur].next = dic[cur.next]
            # cur.random是原节点随机指向
            # d[cur.random]是原节点随机指向  对应的新节点
            if cur.random:
                dic[cur].random = dic[cur.random]
            cur = cur.next
            # 返回头结点，即原节点对应的value(新节点)
        return dic[head]

