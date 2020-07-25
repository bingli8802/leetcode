class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#       已知条件：nums[-1] = nums[n] = -∞， 意味着总有峰值
#       迭代二分查找,注意right范围，因为比较middle和middle+1，防止越界
        left = 0
        right = len(nums) - 1
        
        while left < right:
            middle = (left + right)/2
            if nums[middle] < nums[middle+1]:
                left = middle + 1
            else:
                right = middle
        return right
