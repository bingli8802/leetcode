class Solution(object):
    # time complexity: O(n) 
    # space: O(1)
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0] 
        curSum = 0
        for num in nums:
            curSum = max(curSum + num, num)
            res = max(res, curSum)
            print curSum, res
        return res
    
#     # 举一反三 返回左右边界
#     def maxSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         n = len(nums)
#         res = nums[0]
#         curSum = 0
#         leftBound = 0
#         rightBound = 0
#         tmpBound = 0
        
#         for i in range(n):
#             if curSum < 0:
#                 tmpBound = i
#                 curSum = nums[i]
#             else:
#                 curSum += nums[i]
            
#             if curSum > res:
#                 res = curSum
#                 leftBound = tmpBound
#                 rightBound = i
                
#         print leftBound, rightBound
#         tmp = sum(nums[leftBound:rightBound+1])
#         # tmp 和 res 相等
#         return res
            
#     # time complexity: O(n)
#     def maxSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         n = len(nums)
#         dp = [0] * n
#         dp[0] = nums[0]
#         for i in range(1, n):
#             dp[i] = max(nums[i], dp[i-1] + nums[i])
#         return max(dp)
            
