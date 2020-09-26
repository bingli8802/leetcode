class Solution(object):
    # 三种解法思路一样
    # 自己解法 每次递归时减去当前值 得到remaining
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if candidates == [] or min(candidates) > target:
            return []
        candidates.sort()
        res = []
        n = len(candidates)
        
        def helper(i, rem, cur):
            if rem == 0:
                res.append(cur)
                # return
            elif rem < 0:
                return
            for j in range(i, n):
                helper(j, rem - candidates[j], cur + [candidates[j]])
        
        helper(0, target, [])
        return res
    
    # 解法2 每次递归加上当前值
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates: #先解决空输入的情况
            return []
        
        candidates.sort()  #排序
        res=[]
        n = len(candidates)
        
        def backtrack(i,temp_sum,temp_list): 
            """
            i：遍历到candidates数组中第几个元素
            temp_sum：目前遍历数组的和
            temp_list：目前遍历的数组
            """
            if temp_sum==target:
                res.append(temp_list)
                return
            if temp_sum>target:
                return
            for j in range(i,n):
                backtrack(j,temp_sum+candidates[j],temp_list+[candidates[j]])
        backtrack(0,0,[])
        return res
    
    # 解法3 把数组当作参数传入递归函数 最快 接近95%
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if candidates == [] or min(candidates) > target:
            return []
        candidates.sort()
        res = []
        
        def helper(candidates, target, temp_list):
            if target == 0:
                res.append(temp_list)
            if target < 0:
                return
            for i in range(len(candidates)):
                if candidates[i] > target:
                    break
                helper(candidates[i:], target - candidates[i], temp_list + [candidates[i]])
        helper(candidates,target,[])
        return res
