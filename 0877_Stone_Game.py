class Solution(object):
    # 从下往上 从左往右 遍历 三维dp
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        n = len(piles)
        dp = [[[0,0] for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i][0] = piles[i]
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                # 选择左边石头
                left = piles[i] + dp[i+1][j][1]
                # 选择右边石头
                right = piles[j] + dp[i][j-1][1]
                # 如果左边大于右边
                if left > right:
                    # 先手选择左边
                    dp[i][j][0] = left
                    # 后手只能从[i+1...j]区间选择 并成为这个区间的先手
                    dp[i][j][1] = dp[i+1][j][0]
                else:
                    # 先手选择右边
                    dp[i][j][0] = right
                    # 后手只能从[i...j-1]区间选择 并成为这个区间的先手
                    dp[i][j][1] = dp[i][j-1][0]
        # print dp
        return dp[0][n-1][0] > dp[0][n-1][1]
    # 从下往上 从左往右 二维dp
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        length = len(piles)
        dp = [[0] * length for _ in range(length)]
        for i, pile in enumerate(piles):
            dp[i][i] = pile
        for i in range(length - 2, -1, -1):
            for j in range(i + 1, length):
                dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
        # print dp
        return dp[0][length - 1] > 0

