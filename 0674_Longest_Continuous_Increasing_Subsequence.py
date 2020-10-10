class Solution(object):
    # 效率高些
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        ans = 1
        cnt = 1
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                cnt += 1
            else:
                ans = max(ans, cnt)
                cnt = 1
        return max(ans, cnt)
    
    # 效率低些
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        ans = 1
        cnt = 1
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                cnt += 1
            else:
                cnt = 1
            ans = max(ans, cnt)
        return ans
    
    # 效率最高 接近100%
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        # if n == 1:
        #     return 1
        res = 1
        cnt = 1
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                cnt += 1
            else:
                res = max(res, cnt)
                cnt = 1
        return max(res, cnt)
