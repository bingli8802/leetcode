class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 找最大值和次大值
        first=second=1
        for i in nums:
            if first < i:
                second = first
                first = i
            elif second <= i <= first :
                second = i
        return (second - 1) * (first - 1)
    # 第一版 很慢
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi = (nums[0] - 1) * (nums[1] - 1)
        for i in range(len(nums)-1):
            for j in range(i + 1, len(nums)):
                maxi = max(maxi, (nums[i] - 1) * (nums[j] - 1))
        return maxi

