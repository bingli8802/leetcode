class Solution(object):
    # 自己解法很慢很慢
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) in [0, 2]:
            return -1
        if len(nums) == 1:
            return 0
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
        return -1
    # 前缀和
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == s - leftsum - x:
                return i
            leftsum += x
        return -1
