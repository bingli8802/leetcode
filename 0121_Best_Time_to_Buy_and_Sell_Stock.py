class Solution(object):
    # 东哥二维dp
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], - prices[i])
        # print dp
        return dp[n-1][0]
    
    # 东哥二维dp 改进的动态规划 
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        n = len(prices)
        # 初始化第一天的值
        dp0 = 0 #卖出
        dp1 = -prices[0] #买进
        for i in xrange(1,n):
            # dp0表示第i天卖出的最大收益
            dp0 = max(dp0,dp1+prices[i])
            # dp1表示第i天买入的最大收益
            dp1 = max(dp1,-prices[i])
        # return max(dp0,dp1)
        return dp0
    
    # 压缩成一维动态规划 快多了 解法中最快的
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0: 
            return 0 # 边界条件
        # 收益 初始化都是0
        dp = [0] * n
        minPrice = prices[0] 
        for i in range(1, n):
            minPrice = min(minPrice, prices[i])
            dp[i] = max(dp[i-1], prices[i] - minPrice)
        # print dp
        return dp[-1]

    # 一维dp 改进的动态规划
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice = float("inf")
        maxProfit = 0
        for price in prices:
            minPrice = min(minPrice, price)
            maxProfit = max(maxProfit, price - minPrice)
        return maxProfit


    

