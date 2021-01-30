class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
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
    
    # 第二种解法更容易理解
    # 每次都要找到包含当前位置在内的最大值和最小值
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """    
        res = nums[0]
        pre_max = nums[0]
        pre_min = nums[0]
        for num in nums[1:]:
            cur_max = max(pre_max * num, pre_min * num, num)
            cur_min = min(pre_max * num, pre_min * num, num)
            res = max(res, cur_max)
            pre_max = cur_max
            pre_min = cur_min
        return res

