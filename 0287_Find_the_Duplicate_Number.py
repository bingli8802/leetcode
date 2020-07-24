class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 1
        right = len(nums)
        while left < right:
            cnt = 0
            mid = (left+right)/2
#           计算小于mid的数字
            for i in nums:
                if i <= mid:
                    cnt += 1
#           如果小于mid数字的个数<=它自己 那么重复的数字一定在[mid+1，right]之间
            if cnt <= mid:
                left = mid + 1
#           反之 如果小于mid数字的个数>他自己 那么重复的数字一定在[left,mid]之间
            else:
                right = mid
        return right
                
