class Solution(object):
    # time complexity: O(n)
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # res = float("-inf")
        res = nums[0] 
        curSum = 0
        for num in nums:
            curSum = max(curSum + num, num)
            res = max(res, curSum)
        return res
    
