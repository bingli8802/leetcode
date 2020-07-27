class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        stack1 = []
        stack2 = []
        ss = ""
        tt = ""
        for s in S:
            if stack1 and s == "#":
                stack1.pop()
            elif s != "#":
                stack1.append(s)

        for t in T:
            if stack2 and t == "#":
                stack2.pop()
            elif t != "#":
                stack2.append(t)
        
        ss = "".join(stack1)
        tt = "".join(stack2)
        return True if ss == tt else False
