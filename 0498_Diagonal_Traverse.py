class Solution(object):
    # 思路是想把矩阵分成两部分 分别计算
    # 上半部分输出没问题 下半部分没写完
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        n = len(matrix[0])
        if m == 0 or n == 0:
            return matrix
        res = []
        for i in range(m):
            tmp = []
            for j in range(i+1):
                tmp.append(matrix[i-j][j])
            if i % 2 == 0:
                res += tmp
            else:
                res += tmp[::-1]
                
    # Diagonal index sum are equal to same value           
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        res = []
        dic = defaultdict(list)
        
        # 同一个对角线上的坐标 x+y 是一样的 因此可以用dic
        for i in range(m):
            for j in range(n):
                dic[i+j].append(matrix[i][j])
        for d in range(m+n):
            if d % 2 == 1:
                res += dic[d]
            else:
                res += dic[d][::-1]        
        return res

    # 模拟遍历
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        res = []
        i = j = 0
        for _ in range(m * n):
            res.append(matrix[i][j])
            if (i + j) % 2: #奇数行
                if i == m - 1:
                    j += 1
                else:
                    i += 1
                    if j > 0:
                        j -= 1
            else: #偶数行
                if j == n - 1:
                    i += 1
                else:
                    j += 1
                    if i > 0:
                        i -= 1
        return res 
        
        
        
