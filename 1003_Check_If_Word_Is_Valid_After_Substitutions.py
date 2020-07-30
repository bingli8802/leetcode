# 第一种做法 替换字符串的"abc"->""
class Solution:
    def isValid(self, S: str) -> bool:
        while 'abc' in S:
            S = S.replace('abc', '')
        if len(S) == 0:
            return True
        else:
            return False
        
# 用栈的思想 runtime很长
class Solution(object):
    def isValid(self, S):
        """
        :type S: str
        :rtype: bool
        """
        stack = []
        for i in S:
            if i == "a":
                stack.append(i)
            elif i == "b":
                if stack and stack[-1][-1] == "a":
                    stack[-1] += i
                else:
                    stack.append(i)
            elif i == "c":
                if stack and stack[-1][-1] == "b":
                    stack[-1] += i
                else:
                    stack.append(i)
            if stack[-1] == "abc":
                stack.pop()
        if len(stack) == 0:
            return True
        else:
            return False

