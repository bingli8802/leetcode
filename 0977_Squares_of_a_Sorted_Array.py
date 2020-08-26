class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return sorted([i*i for i in A])
    
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = []
        p = 0
        i = 0
        j = 0
        # 先把负数部分找到
        negative = []
        while p < len(A) and A[p] < 0:
            negative.insert(0, A[p])
            p += 1
        positive = A[len(negative):]
        # 再进行比较
        while i < len(negative) and j < len(positive):
            if negative[i] * negative[i] > positive[j] * positive[j]:
                res.append(positive[j] * positive[j])
                j += 1
            else:
                res.append(negative[i] * negative[i])
                i += 1
        res.extend([m * m for m in negative[i:]])
        res.extend([n * n for n in positive[j:]])
        return res
