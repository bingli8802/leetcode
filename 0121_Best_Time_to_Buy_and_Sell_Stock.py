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
