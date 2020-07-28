class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        # 初始化一个ans用来存放结果
        ans = [0]*len(T)
        # 临时栈用来存放当前下标
        stack = []
        for i in range(len(T)):
            # 当栈不为空 并且栈尾-1取出的index对应T[index]的数字小于T[i]时：
            while stack and T[stack[-1]] < T[i]:
                # 给ans重新赋值
                ans[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return ans
            
