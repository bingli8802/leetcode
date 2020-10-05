class Solution(object):
    # 滑动窗口
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, 0
        res = 0
        cnt = 0
        n = len(nums)
        
        for i in range(n):
            cnt = cnt + 1 if nums[i] == 0 else cnt
            while j < i and cnt > 1:
                if nums[j] == 0:
                    cnt -= 1
                j += 1
            res = max(res, i - j)
        return res

