class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        def getMax(subArr):
            n = len(subArr)
            dp = [0] * (n+1)
            dp[0] = 0
            dp[1] = subArr[0]
            for i in range(2, n+1):
                dp[i] = max(dp[i-1], dp[i-2] + subArr[i-1])
            return dp[-1]
        
        firstPart = nums[:-1]
        secondPart = nums[1:]
        # print firstPart, secondPart
        
        firstSum = getMax(firstPart)
        secondSum = getMax(secondPart)
        # print firstSum, secondSum
        
        return max(firstSum, secondSum)
    
    # 空间优化后接近100%
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def my_rob(nums):
            prev = 0
            curr = 0
            for num in nums:
                prev, curr = curr, max(curr, prev+num)
            return curr
        return max(my_rob(nums[:-1]), my_rob(nums[1:])) if len(nums) != 1 else nums[0]
        
        
        
        
