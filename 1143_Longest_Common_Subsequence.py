class Solution(object):
    # 二维动态规划
    # 画dp table很重要
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m = len(text1)
        n = len(text2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                # 如果当前字符是一样的 那么只要知道i-1和j-1的值就可以了
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:   
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
    
    # 优化成一维
    # 注意两个变量的使用 tmp和last
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m = len(text1)
        n = len(text2)
        dp = [0] * (n+1)
        tmp = 0
        for i in range(1, m+1):
            last = 0
            for j in range(1, n+1):
                tmp = dp[j]
                if text1[i-1] == text2[j-1]:
                    dp[j] = last + 1
                else:   
                    dp[j] = max(tmp, dp[j-1])
                last = tmp
        return dp[-1]
    
    
