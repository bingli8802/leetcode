class Solution(object):
    # 解法太巧妙了 和自己思路一样
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
    
    # 回溯法 递归 更快
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
    
    # 东哥思路 套模板
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def backTrack(li, tmp):
            res.append(tmp)
            for i in range(len(li)):
                backTrack(li[i+1:], tmp + [li[i]])
        backTrack(nums, [])
        return res
                   
    # laioffer老师解法
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """  
        res = []
        def backTrack(li, index, tmp):
            if index == len(li):
                res.append(tmp)
                return
            backTrack(li, index+1, tmp+[li[index]])
            backTrack(li, index+1, tmp)
        backTrack(nums, 0, [])
        return res
        
        
        

