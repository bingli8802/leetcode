class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        res = []
        
        def helper(i, tmp):
            res.append(tmp)
            for j in range(i, n):
                if j > i and nums[j] == nums[j-1]:
                    continue
                helper(j+1, tmp+[nums[j]])
        helper(0, [])
        return res
    
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        res = []
        
        def helper(i, tmp):
            if tmp not in res:
                res.append(tmp)
            for j in range(i, n):
                helper(j+1, tmp+[nums[j]])
        helper(0, [])
        return res 
