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
    
    # 举一反三 返回左右边界
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res = nums[0]
        curSum = 0
        leftBound = 0
        rightBound = 0
        tmpBound = 0
        
        for i in range(n):
            if curSum < 0:
                tmpBound = i
                curSum = nums[i]
            else:
                curSum += nums[i]
            
            if curSum > res:
                res = curSum
                leftBound = tmpBound
                rightBound = i
                
        print leftBound, rightBound
        tmp = sum(nums[leftBound:rightBound+1])
        # tmp 和 res 相等
        return res
            
