class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # stack1用来存储
        # stack2用来颠倒stack1里元素 操作结束后 再把stack2所有剩余元素返回到stack1
        self.stack1 = []
        self.stack2 = []
        
    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """       
        self.stack1.append(x)
        return self.stack1
            
    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        while len(self.stack1) != 0:
            s1 = self.stack1.pop()
            self.stack2.append(s1)
            
        res = self.stack2.pop()
        
        while len(self.stack2) != 0:
            s2 = self.stack2.pop()
            self.stack1.append(s2)
            
        return res
    
    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        while len(self.stack1) != 0:
            s1 = self.stack1.pop()
            self.stack2.append(s1)
            
        res = self.stack2.pop()
        self.stack2.append(res)
        
        while len(self.stack2) != 0:
            s2 = self.stack2.pop()
            self.stack1.append(s2)
            
        return res

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.stack1) > 0:
            return False
        else:
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
