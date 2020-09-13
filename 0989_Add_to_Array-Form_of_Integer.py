class Solution(object):
    # 逐位相加
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        A[-1] += K
        for i in xrange(len(A) - 1, -1, -1):
            carry, A[i] = divmod(A[i], 10)
            if i: A[i-1] += carry
        if carry:
            # 此处map返回一个list -> [1]
            A = map(int, str(carry)) + A
        return A
    
    # 把list转换成string再转换成int 和 k相加 再把结果转换成list
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        s = ''.join([str(i) for i in A])
        n = int(s) + K
        li = list(str(n))
        return [int(i) for i in li]
    
    # reduce用法
    # map()是将传入的函数依次作用到序列的每个元素，每个元素都是独自被函数“作用”一次
    # reduce()是将传人的函数作用在序列的第一个元素得到结果后，把这个结果继续与下一个元素作用（累积计算）
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        return map(int, str(K + reduce(lambda a, b: a*10+b, A)))


