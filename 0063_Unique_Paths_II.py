class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if len(obstacleGrid) == 0:
            return 0
        if obstacleGrid[0][0] == 1:
            return 0
        if obstacleGrid == [[1]]:
            return 0
        if obstacleGrid == [[0]]:
            return 1
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                # 起点坐标是1
                if i == 1 and j == 1:
                    dp[i][j] = 1
                    continue
                # 如果当前节点在obstacle中是障碍物 那么这个点坐标是0
                if obstacleGrid[i-1][j-1] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # print dp
        return dp[-1][-1]
            
