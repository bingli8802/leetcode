class Solution(object):
    # 效率居然是100% 
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        cnt = 0
        n = len(nums)
        if nums[0] == 1:
            start = 1
        else:
            start = 0
        for i in range(start, n):
            if nums[i] == 0:
                cnt += 1
            elif nums[i] == 1:
                if cnt < k:
                    return False
                else:
                    cnt = 0
        return True
        
