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
        
            
# 第一次复习写的答案
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return[-1,-1]
        # 第一次二分查找，找最左边target
        left = 0
        right = len(nums)-1
        ret = []
        while left < right:
            mid = (left+right)/2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        # 如果没找到直接返回，如果找到的话继续第二次二分查找，找最右边的target
        if nums[right] != target:
            return [-1,-1]
        else:
            # 这次的查找范围应该是在[left,right]之间，而不是[0,right],可以缩小范围
            ret.append(left)
            right = len(nums)-1
            while left < right:
                mid = (left+right+1)/2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                elif nums[mid] == target:
                        left = mid
            ret.append(right)
        return ret
                
              
            
            
            
