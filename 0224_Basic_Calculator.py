class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = deque(s)  
        def helper(s):
            stack = []
            sign = '+'
            num = 0
            while len(s) > 0:
                c = s.popleft()
                if c.isdigit():
                    num = 10 * num + int(c)
                # 遇到左括号开始递归计算 num
                if c == '(':
                    num = helper(s)

                if (not c.isdigit() and c != ' ') or len(s) == 0:
                    if sign == '+': 
                        stack.append(num)
                    elif sign == '-': 
                        stack.append(-num)
                    elif sign == '*': 
                        stack.append(stack.pop() * num)
                    elif sign == '/': 
                        stack.append(int(stack.pop() / num))
                    num = 0
                    sign = c
                # 遇到右括号返回递归结果
                if c == ')': break
            return sum(stack)

        return helper(s)



