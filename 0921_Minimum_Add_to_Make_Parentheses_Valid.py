class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        num = 0
        for i in S:
            if i == "(":
                stack.append(i)
                num += 1
            elif i == ")" and len(stack) == 0:
                num += 1
            elif i == ")" and len(stack) != 0:
                stack.pop()
                num -= 1
        return num
