class Solution(object):
    # 排序 双指针同时走
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = sorted(nums)
        start = 0
        end = len(nums)

        for i in range(len(nums)):
            if n[i] != nums[i]:
                start = max(start, i)
                end = min(end, i)
        return start-end+1 if start-end >=0 else 0
    
    # 排序 双指针单独走
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = sorted(nums) 
        low = 0
        while low <= len(nums)-1:
            if nums[low] != n[low]:
                break
            low += 1
        high = len(nums)-1
        while high >= 0:
            if nums[high] != n[high]:
                break
            high -= 1
        return max(high-low+1, 0)
    
    # 四次循环
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_n = max(nums)
        max_n = min(nums)
        '''找到顺序数组第一次降序之后的最小值'''
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                min_n = min(nums[i], min_n)
        '''找到逆序数组第一次升序之后的最大值'''
        for i in range(len(nums)-2, -1, -1):
            if nums[i] > nums[i+1]:
                max_n = max(nums[i], max_n)
        low = 0
        high = len(nums)-1
        '''顺序找到第一个比min_n大的数，代表从这里开始乱序需要排序'''
        while low <= len(nums) - 1:
            if nums[low] > min_n:
                break
            low += 1
        '''逆序找到第一个比max_n小的数，代表从这里开始乱序需要排序'''
        while high >= 0:
            if nums[high] < max_n:
                break
            high -= 1
        # 有可能是一个不需要排序的数组
        return max(high - low + 1, 0)

