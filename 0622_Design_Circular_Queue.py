class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.queue = [0]*k
        # 队首的索引
        self.headIndex = 0
        # 循环队列当前的长度
        self.count = 0
        # 循环队列的容量
        self.capacity = k

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        # 如果数组满了 则不能再插入新的元素 返回false
        if self.count == self.capacity:
            return False
        # 找到下一个空位 并赋值
        self.queue[(self.headIndex + self.count) % self.capacity] = value
        self.count += 1
        return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        # 如果数组为空 返回false
        if self.count == 0:
            return False
        # 找到头 并把头的index加1
        self.headIndex = (self.headIndex + 1) % self.capacity
        self.count -= 1
        return True


    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.count == 0:
            return -1
        return self.queue[self.headIndex]

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.count == 0:
            return -1
        # 找到队尾 注意减1
        return self.queue[(self.headIndex + self.count - 1) % self.capacity]
        

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.count == 0

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.count == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
