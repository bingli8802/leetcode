class Solution(object):
    # 二维dp
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        n = len(coins)
        dp = [[float('inf')] * (amount+1)] * n
        dp[0][0] = 0
        for i in range(n):
            for j in range(amount+1):
                if j >= coins[i]:
                    dp[i][j] = min(dp[i-1][j],dp[i][j-coins[i]]+1)
        return dp[-1][-1] if dp[-1][-1] != float('inf') else -1
    
    # 优化成一维dp
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for i in coins:
            for j in range(i, amount+1):
                dp[j] = min(dp[j], dp[j-i]+1)
        return dp[-1] if dp[-1] != float('inf') else -1
