class Solution(object):
    # reverse the order and insert items from the end to head
    # 先反转数组 找到中点 从中点开始插入到头
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nums.sort(reverse = True)
        mid = len(nums)//2
        i = 0
        j = mid
        while i < n and j < n:
            tmp = nums[j]
            del nums[j]
            nums.insert(i, tmp)
            i += 2
            j += 1
            

