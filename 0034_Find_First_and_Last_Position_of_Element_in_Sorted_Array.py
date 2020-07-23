class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums == []:
            return [-1,-1]
        
#       第一次二分查找需要找到最左边的target
        left = 0
        right = len(nums)-1
        
        while left < right:
            middle = (left+right)/2
            if nums[middle] >= target:
                right = middle
            else:
                left = middle+1
        if nums[right] != target:
            return[-1,-1]
        
        start = right
        
#       第二次二分查找需要找到最右边的target
        left = 0
        right = len(nums)-1
        while left < right:
#           向右取中位数！
            middle = (left+right+1)/2
            if nums[middle] > target:
                right = middle-1
            else:
                left = middle
        if nums[right] != target:
            return[-1,-1]
        
        end = right
        return [start,end]
        
            
