class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        '''
                     left
                     point
        [0,  0,   1,   1,   2,   2]
                      right
        []
        '''
        left = point = 0
        right = len(nums) - 1
        while point <= right:
            if nums[point] == 0:
                nums[point], nums[left] = nums[left], nums[point]
                left += 1
                point += 1
            elif nums[point] == 2:
                nums[point], nums[right] = nums[right], nums[point]
                right -= 1
            else:
                point += 1

