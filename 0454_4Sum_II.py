class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        res = 0
        dic = {}
        for a in A:
            for b in B:
                sum1 = a + b
                dic[sum1] = dic.get(sum1, 0) + 1
        print dic
        for c in C:
            for d in D:
                sum2 = c + d
                if -sum2 in dic:
                    res += dic[-sum2]
        return res

