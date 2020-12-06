class Solution(object):
    # 使用额外空间
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        M = [0] * (n+1)
        if n == 0:
            return 0
        M[0] = 0
        M[1] = nums[0]
        for i in range(2, n+1):
            M[i] = max(nums[i-1]+M[i-2], M[i-1])
        return M[-1]
    
    # 空间优化 从O(n)到O(1)     
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = 0
        curr = 0
    
        # 每次循环，计算“偷到当前房子为止的最大金额”
        for i in nums:
        # 循环开始时，curr 表示 dp[k-1]，prev 表示 dp[k-2]
        # dp[k] = max(dp[k-1], dp[k-2] + i)
            prev, curr = curr, max(curr, prev + i)
        # 循环结束时，curr 表示 dp[k]，prev 表示 dp[k-1]

        return curr
            
            
