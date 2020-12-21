class Solution(object):
    # labuladong
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        def dp(s, i, p, j):
            m = len(s)
            n = len(p)
            if j == n:
                return i == m
            if i == m:
                if (n - j) % 2 == 1:
                    return False
                for j in range(0, n-1, 2):
                    if p[j+1] != "*":
                        return False
                return True
            
            if s[i] == p[j] or p[j] == ".":
                if j < len(p) - 1 and p[j+1] == "*":
                    return dp(s, i, p, j+2) or dp(s, i+1, p, j)
                else:
                    return dp(s, i+1, p, j+1)
            else:
                if j < len(p) - 1 and p[j+1] == "*":
                    return dp(s, i, p, j+2)
                else:
                    return False

        return dp(s, 0, p, 0)
    # 官方解法 
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)

        def matches(i, j):
            if i == 0:
                return False
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]

        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    f[i][j] = f[i][j] | f[i][j - 2]
                    if matches(i, j - 1):
                        f[i][j] = f[i][j] | f[i - 1][j]
                else:
                    if matches(i, j):
                        f[i][j] = f[i][j] | f[i - 1][j - 1]
        return f[m][n]

    # 这个解法容易理解
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s)
        n = len(p)

        # dp[i][j] 表示 s[:i] 与 p[:j] 是否匹配，各自前 i、j 个是否匹配
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        # s 为空串
        for j in range(1, n + 1):
            # 若 p 的第 j 个字符 p[j - 1] 是 '*'
            # 说明第 j - 1、j 位可有可无
            # 那么如果前 j - 2 个已经匹配上，前 j 个也可以匹配上
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] in {s[i - 1], '.'}:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    if p[j - 2] in {s[i - 1], '.'}:
                        dp[i][j] = dp[i][j - 2] or dp[i - 1][j - 2] or dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i][j - 2]
        return dp[m][n]
    
    
    
