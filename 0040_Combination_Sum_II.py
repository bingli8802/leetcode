class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if candidates == []:
            return []
        res = []
        n = len(candidates)
        candidates.sort()
        
        def helper(i, rem, li):
            if rem == 0:
                res.append(li)
            if rem < 0 or i == n:
                return
            for j in range(i, n):
                if candidates[j] > rem:
                    break
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                helper(j+1, rem - candidates[j], li + [candidates[j]])
        helper(0, target, [])
        return res
    
    # 回溯算法 东哥套路模版
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if candidates == []:
            return []
        res = []
        candidates.sort()
        
        def backTrack(li, tmp, rem):
            if rem == 0:
                res.append(tmp)
            if rem < 0 or li == []:
                return
            for i in range(len(li)):
                if li[i] > rem:
                    break
                if i >= 1 and li[i] == li[i-1]:
                    continue
                backTrack(li[i+1:], tmp + [li[i]], rem - li[i])
        backTrack(candidates, [], target)
        return res        
        
# 这个避免重复当思想是在是太重要了。
# 这个方法最重要的作用是，可以让同一层级，不出现相同的元素。即
#                   1
#                  / \
#                 2   2  这种情况不会发生 但是却允许了不同层级之间的重复即：
#                /     \
#               5       5
#                 例2
#                   1
#                  /
#                 2      这种情况确是允许的
#                /
#               2  
                
# 为何会有这种神奇的效果呢？
# 首先 cur-1 == cur 是用于判定当前元素是否和之前元素相同的语句。这个语句就能砍掉例1。
# 可是问题来了，如果把所有当前与之前一个元素相同的都砍掉，那么例二的情况也会消失。 
# 因为当第二个2出现的时候，他就和前一个2相同了。
                
# 那么如何保留例2呢？
# 那么就用cur > begin 来避免这种情况，你发现例1中的两个2是处在同一个层级上的，
# 例2的两个2是处在不同层级上的。
# 在一个for循环中，所有被遍历到的数都是属于一个层级的。我们要让一个层级中，
# 必须出现且只出现一个2，那么就放过第一个出现重复的2，但不放过后面出现的2。
# 第一个出现的2的特点就是 cur == begin. 第二个出现的2 特点是cur > begin.
