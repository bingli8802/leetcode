class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        M0 = [[1] * N for _ in range(N)]
        M1 = [[0] * N for _ in range(N)]
        M2 = [[0] * N for _ in range(N)]
        M3 = [[0] * N for _ in range(N)]
        M4 = [[0] * N for _ in range(N)]
        M = [[0] * N for _ in range(N)]
        res = 0
        
        # 把题目转换成一个矩阵
        for mine in mines:
            M0[mine[0]][mine[1]] = 0
        
        # 从左往右
        for a1 in range(N):
            for b1 in range(N):
                if M0[a1][b1] == 1:
                    if b1 == 0:
                        M1[a1][b1] = 1
                    else:
                        M1[a1][b1] = M1[a1][b1-1] + 1
        # 从右往左               
        for a2 in range(N):
            for b2 in range(N-1,-1, -1):
                if M0[a2][b2] == 1:
                    if b2 == N-1:
                        M2[a2][b2] = 1
                    else:
                        M2[a2][b2] = M2[a2][b2+1] + 1
        # 从上往下
        for a3 in range(N):
            for b3 in range(N):
                if M0[a3][b3] == 1:
                    if a3 == 0:
                        M3[a3][b3] = 1
                    else:
                        M3[a3][b3] = M3[a3-1][b3] + 1
        # 从底向上
        for a4 in range(N-1, -1, -1):
            for b4 in range(N):
                if M0[a4][b4] == 1:
                    if a4 == N-1:
                        M4[a4][b4] = 1
                    else:
                        M4[a4][b4] = M4[a4+1][b4] + 1
                        
        # 从每个点出发遍历一次矩阵
        for i in range(N):
            for j in range(N):
                M[i][j] = min(M1[i][j], M2[i][j], M3[i][j], M4[i][j])
                res = max(res, M[i][j])
        print M
        return res
5
[[4,2]]    
M0 = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 0, 1, 1]]
M1 = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 0, 1, 2]]
M2 = [[5, 4, 3, 2, 1], [5, 4, 3, 2, 1], [5, 4, 3, 2, 1], [5, 4, 3, 2, 1], [2, 1, 0, 2, 1]]
M3 = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4], [5, 5, 0, 5, 5]]
M4 = [[5, 5, 4, 5, 5], [4, 4, 3, 4, 4], [3, 3, 2, 3, 3], [2, 2, 1, 2, 2], [1, 1, 0, 1, 1]]
M = [[1, 1, 1, 1, 1], [1, 2, 2, 2, 1], [1, 2, 2, 2, 1], [1, 2, 1, 2, 1], [1, 1, 0, 1, 1]]
