class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # (str, int) 记录之前的字符串和括号外的上一个数字
        stack = []
        # 实时记录当前可以提取出来的字符串
        res = ""
        num = 0
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == "[":
                stack.append((res, num))
                res, num = "", 0
            elif c == "]":
                top = stack.pop()
                res = top[0] + top[1] * res
            else:
                res += c
        return res
