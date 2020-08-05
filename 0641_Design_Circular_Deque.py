class MyCircularDeque(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.queue = [0] * k
        self.front = 0
        self.rear = 0
        self.count = 0
        self.capacity = k

    # deque
    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.count == self.capacity:
            return False
        self.front = (self.front - 1) % self.capacity
        self.queue[self.front] = value
        self.count += 1
        return True
        
    # 和queue的操作一样
    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.count == self.capacity:
            return False
        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.count += 1
        return True

    # 和queue的操作一样
    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.count == 0:
            return False
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        return True

    # deque
    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.count == 0:
            return False
        self.rear = (self.rear - 1) % self.capacity
        self.count -= 1
        return True

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if self.count == 0:
            return -1
        return self.queue[self.front]

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if self.count == 0:
            return -1
        return self.queue[self.rear - 1]

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return self.count == 0

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return self.count == self.capacity


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
