class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right)/2
            if nums[mid] == target:
                return True
#           判断左边界和右边界是否相等
#           如果相等，左边界右移，直到不相等
            if nums[left] == nums[right]:
                left += 1
                # right -= 1
                continue          
            # 如果中间数小于最左边的数，那么[mid,right]这一区间是单调升的
            if nums[mid] < nums[left]:
                # 如果target在单调升这一区间
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            # 如果中间数大于最左边的数，那么[left,mid]这一区间是单调升的
            elif nums[mid] >= nums[left]:
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return False
    
#  第二种解法
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right)/2
            if nums[mid] == target:
                return True
#           判断左边界和右边界是否相等
#           如果相等，左边界右移，直到不相等
            if nums[left] == nums[right]:
                left += 1
                # right -= 1
                continue          
            # 如果中间数小于或等于最右边的数，那么[mid,right]这一区间是单调升的
            if nums[mid] <= nums[right]:
                # 如果target在单调升这一区间
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            # 如果中间数大于最右边的数，那么[left,mid]这一区间是单调升的
            elif nums[mid] > nums[right]:
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return False
