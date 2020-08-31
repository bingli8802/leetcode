class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                res += prices[i+1] - prices[i]
        return res
    
    # 动态规划 二维
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        dp = [[0]*2 for _ in xrange(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][1] + prices[i], dp[i-1][0])
            dp[i][1] = max(dp[i-1][0] - prices[i], dp[i-1][1])
        return dp[-1][0]
    
    # 动态规划 一维
    def maxProfit(self, prices):
        n = len(prices)
        # 初始化第一天
        dp0 = 0
        dp1 = -prices[0]
        for i in xrange(1,n):
            # 这里的dp0相当于二维数组的dp[i][0]
            # dp1相当于dp[i][1]
            tmp = dp0
            dp0 = max(dp0,dp1+prices[i])
            dp1 = max(dp1,tmp-prices[i])
        # return max(dp0,0)
        return dp0
