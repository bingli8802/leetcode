class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []
        i = 0
        for i in range(len(S)):
            if len(stack) == 0:
                stack.append(S[i])
            elif S[i] != stack[-1]:
                stack.append(S[i])
            elif S[i] == stack[-1]:
                stack.pop()
        return "".join(stack)
