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
