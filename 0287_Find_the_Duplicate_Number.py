class Solution(object):
    # 二分法
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
            # 计算小于mid的数字
            for i in nums:
                if i <= mid:
                    cnt += 1
            # mid = 3, cnt = 2, 如果小于3个数 小于3: 那么重复的数字一定在4，5之间，left右移 缩小范围
            if cnt <= mid:
                left = mid + 1
            # mid = 3, cnt = 4, 如果小于3个数 大于3: 那么重复的数字一定在1，3之间 right左移 缩小范围
            else:
                right = mid
        return right
    
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = dict(collections.Counter(nums))
        for i, v in dic.items():
            if v > 1:
                return i
        
        
