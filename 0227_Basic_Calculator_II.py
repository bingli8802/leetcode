class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        return eval(s)
    
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """                        
        stack = []
        #用num来记录目前累积的数字
        num = 0
        #记录数字前的sign，初始化为+
        sign = '+'
        for i in range(len(s)):
            #如果遇到数字 更新num
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            #如果遇到符号 或者最后一个数字
            if ((not s[i].isdigit()) and s[i] != ' ') or (i == len(s) - 1):
                #一定注意需要把之前计算的数字和符号都存入栈中
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    #注意python的//是向下取整，如果-5//2 = -3这显然不是我们想要的结果，除法向0取整应该使用下面的方法
                    stack.append(int(float(stack.pop()) / num))
                #更新符号 数字清零
                sign = s[i]
                num = 0
        return sum(stack)


