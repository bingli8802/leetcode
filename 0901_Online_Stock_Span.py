class StockSpanner(object):

    def __init__(self):
        # 全局变量用来储存(股票价格，跨度)
        self.stack = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        cnt = 1
        # 如果当天股票价格大于前一天 就把跨度加一 前一天pair删掉
        while self.stack and self.stack[-1][0] <= price:
            cnt += self.stack[-1][1]
            self.stack.pop()
        self.stack.append([price, cnt])
        return cnt


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
