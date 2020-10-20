class Solution(object):
    # 从前往后分割 慢 65%
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1, n+1):
            for j in range(i):
                if dp[j] == 1 and s[j:i] in wordDict:
                    dp[i] = 1
                    break
        return dp[-1]
    
    # 优化从前往后分割 88%
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        dp = [0] * (n+1)
        dp[0] == 1
        for i in range(1, n+1):
            if s[:i] in wordDict:
                dp[i] = 1
            else:
                for j in range(i):
                    if dp[j] == 1 and s[j:i] in wordDict:
                        dp[i] = 1
                        break
        return dp[-1]
    
    # 参考他人解法 99%快
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        # if not wordDict: return not s
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i - 1, -1, -1):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]


