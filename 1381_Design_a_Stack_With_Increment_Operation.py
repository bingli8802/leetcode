class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.length = 0
        self.stack = []
        self.stack2 = []
        self.maxSize = maxSize

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        # 如果长度没达到上限 继续push
        if self.length != self.maxSize:
            self.stack.append(x)
            self.length += 1

    def pop(self):
        """
        :rtype: int
        """
        if self.length != 0:
            self.length -= 1
            return self.stack.pop()
        else:
            return -1

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        min_len = min(k, self.length)

        for i in range(0,self.length):
            s1 = self.stack.pop()
            self.stack2.append(s1)
            
        for j in range(0, min_len):
            s2 = self.stack2.pop()
            sum = int(s2) + val
            self.stack.append(sum)  
        
        while self.stack2:
            self.stack.append(self.stack2.pop())
        
# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
