class Solution(object):
    # 网上答案
    # 如果都是正数 或者有偶数个负数
    # 如果有奇数个负数
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        maxProd = nums[0]
        curMax, curMin = 1, 1
        for i in range(n):
            if nums[i] < 0:
                curMax, curMin = curMin, curMax
            curMax = max(curMax * nums[i], nums[i])
            curMin = min(curMin * nums[i], nums[i])
            maxProd = max(maxProd, curMax)
        return maxProd
        
