class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stack = []
        cnt = 1
        res = ""
        for i in s:
            # 如果栈不为空并且当前元素和栈顶元素一样 更新栈顶元素个数
            if stack and i == stack[-1][0]:
                stack[-1][1] += 1
                # 如果栈顶元素个数等于k 就把栈顶元素pair都pop出来
                if stack[-1][1] == k:
                    stack.pop()
            # 如果栈空或者当前元素和栈顶元素不一样 直接把(元素，个数)pair 放入栈
            else:
                stack.append([i,cnt])
        for j in stack:
            res += j[0] * j[1]
        return res
