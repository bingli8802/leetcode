class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = ["(", "[", "{"]
        right = [")", "]", "}"]
        stack = []
        
        for i in s:
            if i in left:
                stack.append(i)
            else:
                if len(stack) == 0 or i != right[left.index(stack[-1])]:
                    return False
                stack.pop()
                              
        if len(stack) == 0:
            return True
