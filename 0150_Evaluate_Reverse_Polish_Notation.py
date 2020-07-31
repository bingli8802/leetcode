class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        stack = []
        res = 0
        for i in tokens:
            # 判断负数
            if i.lstrip("-").isdigit():
                stack.append(i)
            elif i in operators:
                top1 = stack.pop()
                top2 = stack.pop()
                res = str(int(eval(top2 + i + top1)))
                stack.append(res)
        return stack[0]
        
# 解法2 不去判断数字       
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        stack = []
        res = 0
        for i in tokens:
            if i in operators:
                top1 = stack.pop()
                top2 = stack.pop()
                res = str(int(eval(top2 + i + top1)))
                stack.append(res)
            else:
                stack.append(i)
        return stack[0]
