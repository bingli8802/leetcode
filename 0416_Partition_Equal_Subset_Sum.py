class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        # 如果长度小于2 直接返回
        if n < 2:
            return False
        total = sum(nums)
        # 如果sum不能被2整除 直接返回
        if total % 2 == 1:
            return False
        m = total / 2
        maxNumber = max(nums)
        # 如果数组中最大的数大于一半 并且和半数的和大于total 直接返回
        if maxNumber > m and maxNumber + m > total:
            return False
        # 创建dp
        dp = [[0] * (m+1) for _ in range(n)]
        
        # 先填表格第0行，第1个数只能让容积为它自己的背包恰好装满
        if nums[0] <= m:
            dp[0][nums[0]] = 1
            
        # 从第一行开始遍历
        for i in range(1, n):
            for j in range(m+1):
                dp[i][j] = dp[i-1][j]
                if nums[i] <= j:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
        return dp[-1][-1]
    
    # 优化1 如果第i行的最后一个dp[-1] == 1,可以提前退出循环并返回true
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        # 如果长度小于2 直接返回
        if n < 2:
            return False
        total = sum(nums)
        # 如果sum不能被2整除 直接返回
        if total % 2 == 1:
            return False
        m = total / 2
        maxNumber = max(nums)
        # 如果数组中最大的数大于一半 并且和半数的和大于total 直接返回
        if maxNumber > m and maxNumber + m > total:
            return False
        # 创建dp
        dp = [[0] * (m+1) for _ in range(n)]
        
        # 先填表格第0行，第1个数只能让容积为它自己的背包恰好装满
        if nums[0] <= m:
            dp[0][nums[0]] = 1
            
        # 从第一行开始遍历
        for i in range(1, n):
            for j in range(m+1):
                dp[i][j] = dp[i-1][j]
                if nums[i] <= j:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
            if dp[i][-1] == 1:
                return True
        return dp[-1][-1]
    
    # 优化2 空间优化 速度快了一倍
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        # 如果长度小于2 直接返回
        if n < 2:
            return False
        total = sum(nums)
        # 如果sum不能被2整除 直接返回
        if total % 2 == 1:
            return False
        m = total / 2
        maxNumber = max(nums)
        # 如果数组中最大的数大于一半 并且和半数的和大于total 直接返回
        if maxNumber > m and maxNumber + m > total:
            return False
        dp = [0] * (m+1)
        dp[0] = 1
        for i in range(1, n):
            for j in range(m, -1, -1):
                if nums[i] <= j:
                    dp[j] = dp[j] or dp[j-nums[i]]
            if dp[-1] == 1:
                return True
        return dp[-1]
    
                
