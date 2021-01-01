class Solution(object):
    # 效率可以达到91% 自己的解法
    # 根据之前做过 39， 40
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        li = [i for i in range(1,10)]
        res = []
        def helper(i, cnt, tmp):
            if sum(tmp) == n and cnt == k:
                res.append(tmp)
                return
            if sum(tmp) == n:
                return
            for j in range(i, 9):
                if cnt == k and li[j] + sum(tmp) < n or li[j] + sum(tmp) > n:
                    break
                helper(j+1, cnt+1, tmp+[li[j]])
        helper(0, 0, [])
        return res
    
    # 回溯算法 套用东哥模板
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        li = [i for i in range(1, 10)]
        res = []
        def backTrack(arr, tmp, rem):
            if rem == 0 and len(tmp) == k:
                res.append(tmp)
                return
            elif rem != 0 and len(tmp) == k:
                return
            for i in range(len(arr)):
                if li[i] > rem:
                    break
                backTrack(arr[i+1:], tmp + [arr[i]], rem - arr[i])
        backTrack(li, [], n)
        return res
        
        
        
        
        
        
        
        
        
