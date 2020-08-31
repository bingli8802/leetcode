class Solution(object):
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
