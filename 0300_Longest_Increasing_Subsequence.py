class Solution(object):
    # 时间复杂度 O(n^2) 效率25%
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 创建一个函数下面调用 用于查找在i之前 所有比i小的数里面 最大的连续子序列的长度
        # 边界就是range(i)
        def maxLengthBeforeI(num):
            lstBeforeI = [dp[j] for j in range(num) if nums[j] < nums[i]]
            return max(lstBeforeI) if lstBeforeI else 0
        
        n = len(nums)
        dp = [0] * n
        dp[0] = 1
        # 遍历整个数组 每次查找在i之前 所有比i小的数里面 最大的连续子序列的长度
        for i in range(1, n):
            dp[i] = 1 + maxLengthBeforeI(i)
        return max(dp)
    
    # 效率10%
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = []
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
    
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    # 二分法
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        tails = [0] * len(nums)
        res = 0
        for num in nums:
            i = 0
            j = res
            while i < j:
                m = (i + j) // 2
                # 左边界右移
                if tails[m] < num: 
                    i = m + 1
                # 右边界左移
                else: 
                    j = m
            tails[i] = num
            if j == res: 
                res += 1
        return res

