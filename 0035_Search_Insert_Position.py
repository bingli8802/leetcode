class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
#       寻找第一个大于目标值的位置 最后一个元素也可能是 所以right=len(nums)
#       循环退出的条件是当left==right 所以返回left或者right都可以

        left = 0
        right = len(nums)
        
        while left < right:
            middle = (left+right)/2
            
            if nums[middle] == target:
                return middle
            # 严格小于 target 的元素一定不是解
            elif nums[middle] < target:
                # 下一轮搜索区间是 [mid + 1, right]
                left = middle+1
            elif nums[middle] > target:
                # 下一轮搜索区间是 [left, mid]
                right = middle 
        return left
    
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left = 0
        right = len(nums)-1
        

        while left <= right:
            mid = (left + right)/2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return left
        
