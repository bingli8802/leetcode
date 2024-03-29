class Solution(object):
    # 官网答案
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        
        # 有一个字符串为空串
        if n * m == 0:
            return n + m
        
        # DP 数组
        D = [ [0] * (n + 1) for _ in range(m + 1)]
        
        # 边界状态初始化
        for i in range(m + 1):
            D[i][0] = i
        for j in range(n + 1):
            D[0][j] = j
        
        # 计算所有 DP 值
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                left = D[i - 1][j] + 1
                down = D[i][j - 1] + 1
                left_down = D[i - 1][j - 1] 
                if word1[i - 1] != word2[j - 1]:
                    left_down += 1
                D[i][j] = min(left, down, left_down)
        
        return D[m][n]

    # time: n times m O(n*m)
    # space: n times m O(n*m)
    # each of the cell is a subproblem
    '''
    relplace | insert
    -----------------
    delete   |  cur
    '''
    # 自己解法 参考老师讲义 效率比官网解法高
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(word1)
        m = len(word2)
        
        # 有一个字符串为空串
        if n * m == 0:
            return n + m
        
        # DP 数组
        M = [ [0] * (m + 1) for _ in range(n + 1)]
        
        # 边界状态初始化
        for i in range(n + 1):
            M[i][0] = i
        for j in range(m + 1):
            M[0][j] = j

        for i in range(1, n+1):
            for j in range(1, m+1):
                if word1[i-1] == word2[j-1]:
                    M[i][j] = M[i-1][j-1]
                else:
                    M[i][j] = min(M[i-1][j-1], M[i][j-1], M[i-1][j]) + 1
                    
        return M[n][m]
