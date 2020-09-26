class Solution(object):
    # 解法太巧妙了 和自己思路一样 但没做出来
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for i in nums:
            res = res + [[i] + num for num in res]
            print res
        return res
    
    # 回溯法 递归 更快 好难理解啊
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)
        
        def helper(i, tmp):
            res.append(tmp)
            for j in range(i, n):
                helper(j + 1,tmp + [nums[j]] )
                print res
        helper(0, [])
        return res  


