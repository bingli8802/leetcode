class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
#       start，end 两个指针右移
#       如果start：end之和小于target，end右移
#       如果start：end之和大于target，start右移
#       每次比较ret的长度
        start = 0
        end = 0
        total = 0
        ret = len(nums)+1
        
        while end < len(nums):
            total += nums[end]
            while total >= s:
                ret = min(ret, end-start+1)
                total -= nums[start]
                start += 1
            end += 1
        return 0 if ret == len(nums)+1 else ret
