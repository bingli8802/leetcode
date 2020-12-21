class Solution(object):
    # labuladong 做法超时
    # 找状态 做选择 清晰易懂 可流程化
    # 二分法的优化可以研究
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        # 备忘录
        memo = dict()
        def dp(K, N):
            # base case
            if K == 1:
                return N
            if N == 0:
                return 0
            # 查找字典 避免重复计算
            if (K, N) in memo:
                return memo[(K, N)]
            
            res = float('INF')
            # 穷举所有可能的选择
            for i in range(1, N+1):
                res = min(res, max(dp(K, N-i), dp(K-1, i-1)) + 1)
            # 计入备忘录
            memo[(K, N)] = res
            # print res, memo
            return res
        return dp(K, N)
