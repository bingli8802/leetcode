class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix) #row
        n = len(matrix[0]) #col
        maxSide = 0
        
        M = [[0] * n for _ in range(m)]
            
        for i in range(m):
            for j in range(n):
                if int(matrix[i][j]) == 0:
                    M[i][j] = 0
                else:
                    if i == 0 or j == 0:
                        M[i][j] = 1
                    else:
                        M[i][j] = min(M[i-1][j-1], M[i][j-1], M[i-1][j]) + 1
                    maxSide = max(maxSide, M[i][j])
             
        maxSquare = maxSide * maxSide
        return maxSquare
        
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix) #row
        n = len(matrix[0]) #col
        
        # 定义一个最大边长
        maxSide = 0
        
        M = [[0] * n for _ in range(m)]
            
        for i in range(m):
            for j in range(n):
                # 注意细节 matrix里面是字符
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        M[i][j] = 1
                    else:
                        M[i][j] = min(M[i-1][j-1], M[i][j-1], M[i-1][j]) + 1
                    maxSide = max(maxSide, M[i][j])
             
        maxSquare = maxSide * maxSide
        return maxSquare
