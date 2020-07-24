class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        
        start = 0
        end = 0
        total = 0
        ret = len(nums) + 1
        
        while end < len(nums):
            total = total + nums[end]
            while total >= s:
                total = total - nums[start]
                ret = min(ret,end-start+1)
                start = start + 1
            end = end + 1
        return 0 if ret == len(nums) + 1 else ret
