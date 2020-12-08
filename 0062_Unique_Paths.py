class Solution(object):
    # 空间复杂度 O(m*n)
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                # 任何一个点的path都应该是它左边的点和上面的点之和
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
    
    # 优化空间复杂度 O(n)
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j-1] + dp[j]
        return dp[-1]
                
