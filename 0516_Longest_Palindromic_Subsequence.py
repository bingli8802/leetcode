class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        dp=[[0] * n for _ in range(n)]
        # 初始化条件，一个字符是回文字符，长度为1
        for i in range(n):
            dp[i][i]=1
        # i>j，最长回文子序列为0，因此逆序遍历
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                # 两种情况，两端相等，dp[i+1][j-1]代表s[i+1..j-1] 中最长回文子序列的长度加上2
                if s[i]==s[j]:
                    dp[i][j]=dp[i+1][j-1]+2
                # 不相等，分别加入 s[i+1..j-1] 中，看看哪个子串产生的回文子序列更长
                else:
                    dp[i][j]=max(dp[i+1][j],dp[i][j-1])
        # print dp
        return dp[0][-1]#返回整个字符串的最长回文子序列长度

# "bbbab"   
# [[1, 2, 3, 3, 4], 
#  [0, 1, 2, 2, 3], 
#  [0, 0, 1, 1, 3], 
#  [0, 0, 0, 1, 1], 
#  [0, 0, 0, 0, 1]]
