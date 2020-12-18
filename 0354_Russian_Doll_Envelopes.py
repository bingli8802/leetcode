class Solution(object):
    # dp二分法
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        # sort increasing in first dimension and decreasing on second
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        # print envelopes

        def LIS(nums):
            dp = []
            for i in range(len(nums)):
                idx = bisect_left(dp, nums[i])
                if idx == len(dp):
                    dp.append(nums[i])
                else:
                    dp[idx] = nums[i]
            return len(dp)
        # extract the second dimension and run the LIS
        return LIS([i[1] for i in envelopes])
    
    # 常规lis没考虑二分法 效率很低
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        # sort increasing in first dimension and decreasing on second
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        # print envelopes
        
        def LIS(nums):
            if not nums:
                return 0
            dp = [1] * len(nums)
            for i in range(len(nums)):
                for j in range(i):
                    if nums[i] > nums[j]:
                        dp[i] = max(dp[i], dp[j] + 1)
            return max(dp)
        return LIS([i[1] for i in envelopes])
