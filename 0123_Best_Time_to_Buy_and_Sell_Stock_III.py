class Solution(object):
    # 东哥模版 判断i==0写在函数里面
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        dp=[[[0 for state in range(2)]for k in range(3)] for i in range(len(prices))]

        for i in range(1, len(prices)):
            for k in range(1,3):
                if i==0:
                    dp[0][k][0]=0
                    dp[0][k][1]=-prices[0]
                    continue # continue不要忘啊
                dp[i][k][0]=max(dp[i-1][k][0],dp[i-1][k][1]+prices[i])
                dp[i][k][1]=max(dp[i-1][k][1],dp[i-1][k-1][0]-prices[i])
        return dp[-1][-1][0]
    
    # 东哥模版 初始化写在外面
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        max_k = 2
        dp = [[[0] * 2 for _ in range(max_k+1)] for _ in range(n)]
        for k in range(1, max_k + 1):
            dp[0][k][1] = -prices[0]
            
        for i in range(1, n):
            for k in range(1, max_k + 1):
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
        # print dp
        return dp[-1][-1][0]

