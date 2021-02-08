class Solution(object):
    # 自己解法
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) / 2
            # print left, mid, right
            if left != mid and nums[left] == nums[mid]:
                left += 1
                continue
            if right != mid and nums[right] == nums[mid]:
                right -= 1
                continue
            if nums[mid] >= nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid    
        return nums[right]
    
    # compare nums[mid] and nums[right]
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right-left)/2
            if nums[mid] == nums[right]:
                right -= 1
            elif nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
        return nums[left]

