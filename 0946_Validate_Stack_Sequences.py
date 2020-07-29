class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        for push in pushed:
            stack.append(push)
            while stack and stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)
        if len(stack) == 0:
            return True
        else:
            return False
