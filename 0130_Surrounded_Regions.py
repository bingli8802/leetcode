class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        f = {}
        def find(p):
            # 如果p不在dict里 那么p的value设置为p
            f.setdefault(p, p)
            if f[p] != p:
                f[p] = find(f[p])
            return f[p]
        
        def union(p, q):
            f[find(p)] = find(q)       
            
        if not board or not board[0]:
            return
        
        row = len(board)
        col = len(board[0])
        dummy = row * col
        
        # 第一次遍历整个矩阵 进行连接
        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    # 如果四边上出现"O" 把当前位置和dummy连接
                    if i == 0 or i == row - 1 or j == 0 or j == col - 1:
                        # print i * col + j, dummy
                        union(i * col + j, dummy)
                        # print f
                    # 如果"O"不在四边上
                    else:
                        # 检查四个方向的值
                        for p, q in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            # 如果任意一个方向出现"O" 就把当前位置和出现"O"的位置连接
                            if board[i + p][j + q] == "O":
                                # print i * col + j, (i + p) * col + (j + q)
                                union(i * col + j, (i + p) * col + (j + q))
                                # print f
        # 第二次遍历整个矩阵 
        for i in range(row):
            for j in range(col):
                if find(i * col + j) == find(dummy):
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"
        
# [["X","X","X","X"],
#  ["X","O","O","X"],
#  ["X","X","O","X"],
#  ["X","O","X","X"]]        
# 5 6
# {5: 6, 6: 6}
# 6 10
# {10: 10, 5: 6, 6: 10}
# 6 5
# {10: 10, 5: 10, 6: 10}
# 10 6
# {10: 10, 5: 10, 6: 10}
# 13 16
# {16: 16, 10: 10, 5: 10, 6: 10, 13: 16}
