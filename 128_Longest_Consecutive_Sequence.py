class Solution(object):
    # 先消重再排序
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums = list(set(nums))
        nums.sort()
        n = len(nums)
        dp = [1] * n
        res = 1
        # print nums
        for i in range(1, n):
            if nums[i] == nums[i-1] + 1:
                dp[i] = dp[i-1] + 1
                res = max(res, dp[i])
        return res
