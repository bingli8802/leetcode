class Solution(object):
    # 东哥版本
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        def maxProfit_k_inf(prices):
            n = len(prices)
            dp = [[0] * 2 for _ in range(n)]
            dp[0][0] = 0
            dp[0][1] = -prices[0]
            for i in range(1, n):
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
                dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
            return dp[-1][0]
        
        n = len(prices)
        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(n)]
        
        if k > n / 2:
            return maxProfit_k_inf(prices)
        # 这部分代码可以不写
        # for i in range(n):
        #     dp[i][0][0] = 0
        #     dp[i][0][1] = -float('inf')
        for j in range(1, k+1):
            dp[0][j][0] = 0
            dp[0][j][1] = -prices[0]
        for i in range(1, n):
            for j in range(1, k+1):
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
        return dp[-1][-1][0]
    
    # 这个方法不对 不知道为什么 把判断base case放里面 就不通过了
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        def maxProfit_k_inf(prices):
            n = len(prices)
            dp = [[0] * 2 for _ in range(n)]
            dp[0][0] = 0
            dp[0][1] = -prices[0]
            for i in range(1, n):
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
                dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
            return dp[-1][0]
        
        n = len(prices)
        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(n)]
        
        if k > n / 2:
            return maxProfit_k_inf(prices)
        
        for i in range(1, n):
            for j in range(1, k + 1):
                if i == 0:
                    dp[0][j][0] = 0
                    dp[0][j][1] = -prices[0]
                    continue
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
        return dp[-1][-1][0]
