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
                # 消除重复
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
    
    # 参考东哥回溯算法框架模板
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        res = []
        def backTrack(li, tmp):
            res.append(tmp)
            for i in range(len(li)):
                if i >=1 and li[i] == li[i-1]:
                    continue
                backTrack(li[i+1:], tmp+[li[i]])
        backTrack(nums, [])
        return res

        # laioffer老师答案
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        def backTrack(sol, li, index):
            if index == len(li):
                res.append(sol)
                return
            backTrack(sol+[li[index]], li, index+1)
            while index < len(li)-1 and li[index+1] == li[index]:
                index += 1
            backTrack(sol, li, index+1)
        backTrack([], nums, 0)
        return res
