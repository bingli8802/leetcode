class RecentCounter(object):

    def __init__(self):
        self.q = collections.deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        # 入队
        self.q.append(t)
        # 如果当前值减去3000大于队列第一个元素，证明从第一个元素到当前值的时间大于3000，应给把第一个元素出队
        # 直到队列第一个元素到当前值的时间距离小于或等于3000
        while self.q[0] < t-3000:
            self.q.popleft()
        return len(self.q)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
