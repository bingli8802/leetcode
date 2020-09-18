class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        cnt = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
                res = max(res, cnt)
            else:
                cnt = 0
        return res
    
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        cnt = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
            else:
                res = max(res, cnt)
                cnt = 0
        return max(res, cnt)
    
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 用map函数一行
        # return max(map(len, ''.join(map(str, nums)).split('0')))
        
        s = ''.join(str(i) for i in nums)
        li = s.split('0')
        return max(len(i) for i in li)
    
    
