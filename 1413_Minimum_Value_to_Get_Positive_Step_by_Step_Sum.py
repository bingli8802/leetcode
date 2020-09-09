class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 计算前缀和
        for i in range(1, len(nums)):
            nums[i] = nums[i-1] + nums[i]
        # 找到最小前缀和
        return 1-min(nums) if min(nums) < 1 else 1
