class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1
#       如果中间数大于最右边数 那么最小值一定在右半边
        while left < right:
            mid = (left+right)/2
            if nums[mid] > nums[right]:
                    left = mid+1
            else:
                right = mid
        return nums[left]
