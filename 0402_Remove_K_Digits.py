class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        rem = len(num) - k
        for i in num:
            while k and stack and stack[-1] > i:
                k -= 1
                stack.pop()
            stack.append(i)
        res = stack[:rem]
        return "".join(res).lstrip("0") or "0"
