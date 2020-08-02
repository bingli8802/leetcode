# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        # 栈中存放未找到更大值的节点，以及该节点的下标
        curr = head
        res = []
        stack = []
        i = 0
        while curr:
            res.append(0)
            # 如果栈不空 栈顶元素小于当前curr.val 就把栈顶元素相应的res里面值换成curr.val
            # 并pop栈顶元素
            while stack and stack[-1][0] < curr.val:
                res[stack[-1][1]] = curr.val
                stack.pop()
            stack.append((curr.val, i))
            i += 1
            curr = curr.next
        return res

