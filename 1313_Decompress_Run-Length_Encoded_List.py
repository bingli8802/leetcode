class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(0, len(nums) - 1, 2):
            # 也可以用extend
            # res.extend(nums[i+1]] * nums[i])
            res += [nums[i+1]] * nums[i]
        return res
