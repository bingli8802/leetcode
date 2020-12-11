class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        if not matrix:
            return 
        m = len(matrix)
        n = len(matrix[0])

        self.dp = [[0] * (n+1) for _ in range(m)]
        for i in range(m):
            for j in range(1, n+1):
                self.dp[i][j] = self.dp[i][j-1] + matrix[i][j-1]
        
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        # 自己解法超时 时间复杂度O(m*n) 空间复杂度O(1)
        # res = 0
        # for i in range(row1, row2+1):
        #     res = res + sum(self.matrix[i][col1:col2+1])
        # return res
        # 优化-加入缓存 时间复杂度O(m) 空间复杂度O(m*n)
        res = 0
        for k in range(row1, row2+1):
            res += self.dp[k][col2+1] - self.dp[k][col1]
        return res

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
