class Solution(object):
    # 二维
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        n = len(nums)
        # 先判断如果全是正号或者全是负号的情况下 如果比s小 直接返回
        nums_sum = sum(nums)
        if abs(nums_sum) < abs(S): 
            return 0
        # 整个数组长度应该是算上全是负号那边
        length = 2 * nums_sum + 1
        dp = [[0] * length for _ in range(n)]
        # 注意初始化
        # 如果nums[0]， 那么dp[0][0] = 2 而不是 1
        dp[0][nums_sum + nums[0]] = 1
        dp[0][nums_sum - nums[0]] = dp[0][nums_sum - nums[0]] + 1
        
        for i in range(1, n):
            for j in range(length):
                # 分别计算左右两边
                l = dp[i - 1][j - nums[i]] if 0 <= j - nums[i] < length else 0
                r = dp[i - 1][j + nums[i]] if 0 <= j + nums[i] < length else 0
                dp[i][j] = l + r
            # print dp
        return dp[n-1][nums_sum+S]
    
    # 二维
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        n = len(nums)
        # 先判断如果全是正号或者全是负号的情况下 如果比s小 直接返回
        nums_sum = sum(nums)
        if abs(nums_sum) < abs(S): 
            return 0
        # 整个数组长度应该是算上全是负号那边
        length = 2 * nums_sum + 1
        dp = [[0] * length for _ in range(n)]
        # 注意初始化
        dp[0][nums_sum + nums[0]] = 1
        dp[0][nums_sum - nums[0]] = dp[0][nums_sum - nums[0]] + 1  
        for i in range(1, n):
            for j in range(length):
                # 分别计算左右两边
                if 0 <= j - nums[i] < length:
                    dp[i][j] += dp[i - 1][j - nums[i]] 
                if 0 <= j + nums[i] < length:
                    dp[i][j] += dp[i - 1][j + nums[i]] 
            # print dp
        return dp[n-1][nums_sum+S]
    
    # 优化成一维
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        n = len(nums)
        nums_sum = sum(nums)
        if abs(nums_sum) < abs(S):
            return 0
        length = 2 * nums_sum + 1
        dp = [0] * length
        dp[nums_sum + nums[0]] = 1
        dp[nums_sum - nums[0]] += 1
        for i in range(1, n):
            # 因为dp[i]的取值可能需要左右两边的值相加 所以建立一个临时数组last 用来存储结果
            last = [0] * length
            for j in range(length-1, -1, -1):
                if 0 <= j - nums[i] < length:
                    last[j] += dp[j-nums[i]] 
                if 0 <= j + nums[i] < length:
                    last[j] += dp[j+nums[i]]
            dp = last
            # print last, dp
        return dp[nums_sum+S]
    
# 二维            
# [[0, 2, 0], [0, 4, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
# [[0, 2, 0], [0, 4, 0], [0, 8, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
# [[0, 2, 0], [0, 4, 0], [0, 8, 0], [0, 16, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
# [[0, 2, 0], [0, 4, 0], [0, 8, 0], [0, 16, 0], [0, 32, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
# [[0, 2, 0], [0, 4, 0], [0, 8, 0], [0, 16, 0], [0, 32, 0], [0, 64, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
# [[0, 2, 0], [0, 4, 0], [0, 8, 0], [0, 16, 0], [0, 32, 0], [0, 64, 0], [0, 128, 0], [0, 0, 0], [0, 0, 0]]
# [[0, 2, 0], [0, 4, 0], [0, 8, 0], [0, 16, 0], [0, 32, 0], [0, 64, 0], [0, 128, 0], [0, 256, 0], [0, 0, 0]]
# [[0, 2, 0], [0, 4, 0], [0, 8, 0], [0, 16, 0], [0, 32, 0], [0, 64, 0], [0, 128, 0], [0, 256, 0], [256, 0, 256]]

# 一维
# [0, 2, 0]
# [0, 4, 0]
# [0, 8, 0]
# [0, 16, 0]
# [0, 32, 0]
# [0, 64, 0]
# [0, 128, 0]
# [0, 256, 0]
# [256, 256, 256]
            
            
