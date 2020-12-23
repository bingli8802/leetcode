class Solution(object):
    # 东哥动态规划 二维
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        dp = [[0, -prices[0]]] + [[0, 0] for _ in range(n - 1)]
        # dp = [[0]*2 for _ in range(n)]
        # dp[0][0] = 0
        # dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i] - fee)
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        # print dp
        return dp[-1][0]
    
    # 优化成常数级
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if not prices:
            return 0
        n = len(prices)
        dp0 = 0
        dp1 = -prices[0]
        for i in range(1, n):
            temp = dp0
            dp0 = max(dp1 + prices[i] - fee, dp0)
            dp1 = max(temp - prices[i], dp1)
        return dp0
