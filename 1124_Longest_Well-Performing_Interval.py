做法1-错误 题目理解错误
class Solution(object):
    def longestWPI(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        stack = []
        for h in hours:
            if h > 8:
                if len(stack) == 0 or stack[-1][1] > 0:
                    stack.append([1, 0])
                elif stack[-1][1] == 0:
                    stack[-1][0] += 1
            elif h <= 8:
                if len(stack) != 0:
                    stack[-1][1] += 1
        for s in range(len(stack)):
            if stack[s][1] == 0:
                stack[s] = stack[s][0] + 1
            elif stack[s][0] > stack[s][1]:
                stack[s] = stack[s][0] + stack[s][1]
            elif stack[s][0] == stack[s][1]:
                stack[s] = stack[s][0]
            elif stack[s][0] < stack[s][1]:
                stack[s] = stack[s][0] + 1
        if len(stack) == 0:
            return 0
        else:
            return max(stack)
             
