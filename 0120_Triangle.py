class Solution(object):
    # 空间复杂度O(n^2)
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        dp = [[0] * n for _ in range(n)]
        dp[0][0] = triangle[0][0]
        for i in range(1, n):
            dp[i][0] = dp[i-1][0] + triangle[i][0]
            for j in range(1, i):
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
            dp[i][i] = dp[i-1][i-1] + triangle[i][i]
        print dp
        return min(dp[-1])
    
    # 优化空间
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        dp = [0] * n
        dp[0] = triangle[0][0]
        for i in range(1, n):
            # 最后一个元素赋值
            dp[i] = dp[i-1] + triangle[i][i]
            # 从后往前赋值
            for j in range(i-1, 0, -1):
                dp[j] = min(dp[j-1], dp[j]) + triangle[i][j]
            # 第一个元素赋值
            dp[0] = dp[0] + triangle[i][0]
        return min(dp)
