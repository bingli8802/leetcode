class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """            
        count = 0
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                count += 1
                if i+1 < len(nums) and i-2 >= 0:
                    if nums[i+1] < nums[i-1] and nums[i-2] > nums[i]:
                        return False
            if count > 1:
                return False
        return True

    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cnt = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                if cnt == 1:
                    return False 
                if i < len(nums) - 1 and i >= 2:
                    if nums[i+1] < nums[i-1] and nums[i] < nums[i-2]:
                        return False
                cnt += 1
        return True
    
    # 修改原数组 更慢些
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cnt = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1] and cnt == 0:
                if i >= 2 and nums[i] < nums[i-2]:
                    nums[i] = nums[i-1]
                cnt += 1
            elif nums[i] < nums[i-1] and cnt == 1:
                return False
        return True
                
