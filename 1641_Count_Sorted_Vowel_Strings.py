class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0] * 5 for i in range(n)]
        for i in range(5):
            dp[0][i] = 1
        for j in range(n):
            dp[j][0] = 1
        for m in range(1, n):
            for k in range(1, 5):
                dp[m][k] = sum(dp[m-1][:k+1])
        return sum(dp[n-1][:])
    
    # 从二维dp优化到一维dp 时间复杂度差不多
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """        
        dp=[1 for _ in range(5)]
        for i in range(1,n):
            # 从后往前更新数据 很巧妙
            for j in range(4,-1,-1):
                dp[j]=sum(dp[:j+1])
        return sum(dp)
