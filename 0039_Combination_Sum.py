class Solution(object):
    # 回溯套路
    # 自己解法 每次递归时减去当前值 得到remaining
    # 注意 在for循环里加上一个判断语句 提升速度到97%
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
                return
            elif rem < 0:
                return
            for j in range(i, n):
                # 加一个判断语句
                if candidates[j] > rem:
                    break
                helper(j, rem - candidates[j], cur + [candidates[j]])
        helper(0, target, [])
        return res
    
    # 解法2 把数组当作参数传入递归函数 最快 接近95%
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
        
        def helper(li, rem, tmp):
            if rem == 0:
                res.append(tmp)
                # return
            if rem < 0:
                return
            for i in range(len(li)):
                if li[i] > rem:
                    break
                helper(li[i:], rem - li[i], tmp + [li[i]])
        helper(candidates,target,[])
        return res
                
