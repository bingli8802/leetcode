class Solution(object):
    # 自己解法超时
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        largest = -float('inf')
        for i in range(len(nums) - k + 1):
            largest = max(sum(nums[i:i+k]), largest)
        return float(largest)/k
    
    # 滑动窗口        
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        numSum = sum(nums[:k])
        res = numSum
        for i in range(k, len(nums)):
            numSum += nums[i] - nums[i-k]
            res = max(res, numSum)
        return float(res)/k
    
    # 累计求和 最快
    # def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        li = [0] * n
        li[0] = nums[0]
        for i in range(1, n):
            li[i] = li[i-1] + li[i]
        res = li[k-1]
        for j in range(k, n):
            res = max(res, nums[i] - nums[i-k])
        return float(res)/4
            
