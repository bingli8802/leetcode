class Solution(object):
    # 不改变原数组
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [nums[0]] 
        for i in range(1, len(nums)):
            num = nums[i] + res[i-1]
            res.append(num)
        return res
    
    # 在原数组上直接修改 
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(1, len(nums)):
            nums[i] = nums[i-1] + nums[i]
        return nums
