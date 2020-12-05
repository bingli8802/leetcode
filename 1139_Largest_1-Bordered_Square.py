class Solution(object):
    # 根据讲义自己写的答案 效率95%
    def largest1BorderedSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        maxSide = grid[0][0]
        
        # step1 初始化两个矩阵 记录从右往左 从下往上 每个顶点上1的个数
        M1 = [[0] * n for _ in range(m)]
        M2 = [[0] * n for _ in range(m)]
        
        for a1 in range(m):
            for b1 in range(n-1, -1, -1):
                if grid[a1][b1] == 1:
                    if b1 == n-1:
                        M1[a1][b1] = 1
                    else:
                        M1[a1][b1] = M1[a1][b1+1] + 1
        
        for a2 in range(m-1, -1, -1):
            for b2 in range(n):
                if grid[a2][b2] == 1:
                    if a2 == m-1:
                        M2[a2][b2] = 1
                    else:
                        M2[a2][b2] = M2[a2+1][b2] + 1
                        
        # step2 从第一个顶点开始遍历
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                # 当点节点上右边的边长 和下面的边长 进行比较 取较短那个    
                side = min(M1[i][j], M2[i][j])
                # 如果这个节点的边长已经小于当前最大边长 此次循环不进行 
                if side < maxSide:
                    continue
                # 站在当前节点下 check右上顶点 还有左下顶点 是否具有相同的边长  
                for k in range(side, 0, -1):
                    # check top right 右上角顶点从下往上数的边长
                    top_right = M2[i][j+k-1]
                    if top_right < k:
                        continue
                    else:
                        # check bottom left 左下角顶点往右数的边长
                        bottom_left = M1[i+k-1][j]
                        if bottom_left < k:
                            continue
                        else:
                            maxSide = max(maxSide, k) 
                            break             
        # print M1
        # print M2
        res = maxSide * maxSide
        # print res
        return res
