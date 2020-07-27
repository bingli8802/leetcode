class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
#       只删掉最外面一层括号
#       左括号入栈：若入栈后栈的长度大于1，即该左括号不是原语首个左括号，结果加入'('
#       右括号出栈：若出栈后栈的长度大于0，即该右括号不是原语末个右括号，结果加入')'
        li = []
        res = ""
        for i in S:
            if i == "(":
                li.append(i)
                if len(li) > 1:
                    res += i
            else:
                li.pop()
                if len(li) != 0:
                    res += i
        return res
