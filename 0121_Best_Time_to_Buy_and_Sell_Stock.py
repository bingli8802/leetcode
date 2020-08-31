class Solution(object):
    # 动态规划
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
        minprice = prices[0] 
        for i in range(1, n):
            minprice = min(minprice, prices[i])
            dp[i] = max(dp[i-1], prices[i] - minprice)
        return dp[-1]
    
    # 改进的动态规划
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

    # 改进的动态规划
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
    
#     # 特别特别慢 O(n^2)
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         maxi = 0
#         for i in range(len(prices) - 1):
#             buy = prices[i]
#             sell = max(prices[i:])
#             maxi = max(maxi, sell - buy)
#         return maxi
