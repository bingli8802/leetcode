class Solution(object):
    # 典型的回溯算法 东哥模版
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        if not k or not n:
            return
        def backTrack(m, tmp):
            if len(tmp) == k:
                res.append(tmp)
                return
            for i in range(m+1, n+1):
                backTrack(i, tmp + [i])
        backTrack(0, [])
        return res
