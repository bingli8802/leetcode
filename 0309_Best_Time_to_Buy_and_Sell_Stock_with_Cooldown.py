class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n < 2: 
            return 0
        dp = [[0]*3 for _ in xrange(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[0][2] = 0
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][1] + prices[i], dp[i-1][0])
            dp[i][1] = max(dp[i-1][2] - prices[i], dp[i-1][1])
            dp[i][2] = dp[i-1][0]
        return dp[-1][0]
    
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n<2:
            return 0
        # 初始化第一天    
        dp0 = 0
        dp1 = -prices[0]
        dp2 = 0
        for i in xrange(1,n):
            # 这里的dp0相当于二维数组的dp[i][0] 卖出收益
            # dp1相当于dp[i][1] 买入收益
            # dp2相当于dp[i][2] 冷冻期内的收益
            tmp = dp0
            dp0 = max(dp0,dp1+prices[i])
            dp1 = max(dp1,dp2-prices[i])
            dp2 = tmp
        # return max(dp0,dp1,dp2)
        return dp0
