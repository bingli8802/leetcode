class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return(0)
        n = len(nums)
        
        # lengths = [0] * N #lengths[i] = longest ending in nums[i]
        # counts = [1] * N #count[i] = number of longest ending in nums[i]

        length = [1] * n
        counter = [1] * n

        for i in range(1,n):
            for j in range(i):
                if nums[j] < nums[i]: 
                    if length[j] + 1 > length[i]:# 代表第一次遇到最长子序列
                        length[i] = 1 + length[j]
                        counter[i] = counter[j]
                    elif length[j] + 1 == length[i]:# 代表已经遇到过最长子序列
                        counter[i] = counter[i] + counter[j]
        tmp = max(length)
        res = sum([counter[i] for i in range(n) if length[i] == tmp])
        return(res)

