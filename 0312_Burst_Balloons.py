class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # 新建一个points数组 存放两端虚拟值 “1”
        points = nums
        points.insert(0, 1)
        points.append(1)
        # 状态转移数组
        dp = [[0] * (n+2) for _ in range(n+2)]
        for i in range(n, -1, -1):
            for j in range(i+1, n+2):
                for k in range(i+1, j):
                    # 状态转移方程
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + points[i] * points[k] * points[j])
        # print dp
        return dp[0][n+1]
