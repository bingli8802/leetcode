class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        s = sum(i for i in A if i % 2 == 0)
        res = []
        for val, index in queries:
            if A[index] % 2 == 0:
                s -= A[index]
            A[index] += val
            if A[index] % 2 == 0:
                s += A[index]
            res.append(s)
        return res
    
    # 位运算
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        nsum = sum(i for i in A if i & 1 == 0)
        res = []
        for value, key in queries:   
            if A[key] & 1 == 0:     # 如果要修改的数原本是偶数，先从偶数和中减去（通过 & 1 判断会更快一些）
                nsum -= A[key]
            A[key] += value
            if A[key] & 1 == 0:    # 如果修改完后为偶数，加到偶数和中
                nsum += A[key]
            res.append(nsum)
        return res
    
    # 位运算改进
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        nsum = sum(i for i in A if i & 1 == 0)
        res = []
        for value, key in queries:
            if A[key] & 1 == 0:         # 原来为偶数
                if value & 1 == 0:      # 增加的值为偶数，和为偶数
                    nsum += value
                else:                   # 增加的值为奇数，和为奇数
                    nsum -= A[key]
            else:                       # 原来为奇数
                if value & 1:           # 增加的值为奇数，和为偶数
                    nsum += A[key] + value
            res.append(nsum)
            A[key] += value
        return res

    # 暴力解法 超时
    # def sumEvenAfterQueries(self, A, queries):
    #     """
    #     :type A: List[int]
    #     :type queries: List[List[int]]
    #     :rtype: List[int]
    #     """
    #     res = []
    #     for query in queries:
    #         A[query[1]] += query[0]
    #         res.append(sum(i for i in A if i % 2 == 0))
    #     return res
