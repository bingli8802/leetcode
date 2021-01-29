class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for s in range(m):
                        if matrix[s][j] != 0:
                            matrix[s][j] = 'x'
                    for t in range(n):
                        if matrix[i][t] != 0:
                            matrix[i][t] = 'x'
                    matrix[i][j] = 'x'
        # print matrix
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 'x':
                    matrix[i][j] = 0
