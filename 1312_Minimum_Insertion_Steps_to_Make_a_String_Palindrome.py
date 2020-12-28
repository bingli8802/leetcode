class Solution(object):
    # 东哥二维dp
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1
        return dp[0][n-1]
    # 东哥一维  
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [0] * n
        tmp = 0
        for i in range(n-1, -1, -1):
            # pre is dp[i+1][j-1] 
            pre = 0
            for j in range(i+1, n):
                tmp = dp[j]
                if s[i] == s[j]:
                    dp[j] = pre
                else:
                    dp[j] = min(dp[j], dp[j-1]) + 1
                pre = tmp
            print dp
        return dp[n-1]
