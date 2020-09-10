class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        for i in range(n):
            if i != nums[i]:
                return i
        return n
    
    # 二分查找
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right)/2
            if nums[mid] > mid:
                right = mid
            else:
                left = mid + 1
        return left
