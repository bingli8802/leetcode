class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.queue1.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))
        top = self.queue1.pop(0)
        tem = self.queue1 
        self.queue1 = self.queue2
        self.queue2 = tem        
        return top
            
    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        while len(self.queue1) > 1:
            top = self.queue1.pop(0)
            self.queue2.append(top)
        print "ok"    
        top = self.queue1.pop(0)
        self.queue2.append(top)
        tem = self.queue1 
        self.queue1 = self.queue2
        self.queue2 = tem
        return top

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return True if len(self.queue1) == 0 else False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
