class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        # 数据栈用来存放数据 min栈用来存储当前最小值
        self.data_stack = []
        self.min_stack = []
        
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        # 数据栈元素放进来
        self.data_stack.append(x)
        # 如果min栈为空 或者进入栈的元素<=min栈最后一个元素 则入栈
        if (len(self.min_stack) == 0 or x <= self.min_stack[-1]):
            self.min_stack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        # 数据栈元素pop出来
        # 如果min栈最顶元素和pop出来的元素一样的话 那么min栈也pop
        top = self.data_stack.pop()
        if self.min_stack[-1] == top:
            self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        # 返回数据栈最顶元素
        return self.data_stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        # 返回min栈最顶元素
        return self.min_stack[-1]
    
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
