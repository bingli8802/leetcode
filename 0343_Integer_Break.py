class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        M = [0] * (n+1)
        for i in range(2, n+1):
            curMax = 0
            for j in range(1, i/2+1):
                curMax = max(curMax, max(j, M[j])*max(i-j, M[i-j]))
            M[i] = curMax
        return M[n]
    
    # 效率
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]*(n+1)
        # dp[1] = 1
        for i in range(2,n+1):
            for j in range(1,i//2+1):
                dp[i] = max(dp[i],max(j,dp[j])*max(i-j,dp[i-j]))
        return dp[-1]

    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1)
        for i in range(2, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], max(j, dp[j]) * (i-j))
        return dp[-1]
