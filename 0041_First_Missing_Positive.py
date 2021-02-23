class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        n = len(nums)
        nums_rec = [False] * (n + 1)
        
        for i in nums:
            if 0 < i <= n:
                nums_rec[i] = True
        print nums_rec
        
        for j in range(1, n+1):
            if not nums_rec[j]:
                return j
        if not nums_rec:
            return 1
        else:
            return n+1
