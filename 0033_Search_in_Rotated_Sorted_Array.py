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
            middle = left + (right - left) / 2

            if nums[middle] == target:
                return middle
            
            elif nums[middle] < nums[right]:
                if nums[middle] < target and target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
            else:
                if nums[left] <= target and target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1       
        return -1
                
