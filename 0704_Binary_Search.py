class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """        
#         left = 0
#         right = len(nums)-1
        
#         while (left <= right):
#             middle = (left + right)/2
#             if nums[middle] == target:
#                 return middle
#             elif nums[middle] < target:
#                 left = middle + 1
#             elif nums[middle] > target:
#                 right = right - 1
#         return -1

        left = 0
        right = len(nums)
        
        while (left < right):
            middle = (left+right)/2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = right - 1
        return -1
