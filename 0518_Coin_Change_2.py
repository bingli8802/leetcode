class Solution(object):
    # 优化的一维题解
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0] * (amount+1)
        dp[0] = 1
        for i in coins:
            for j in range(1, amount+1):
                if j >= i:
                    dp[j] = dp[j] + dp[j-i]
        return dp[-1]
    
    # 二维题解
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        n = len(coins)
        dp = [[0] * (amount+1) for _ in range(n+1)]
        for k in range(n+1):
            dp[k][0] = 1
        for i in range(1, n+1):
            for j in range(1, amount+1):
                if j >= coins[i-1]:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
            # print dp
        return dp[-1][-1]
