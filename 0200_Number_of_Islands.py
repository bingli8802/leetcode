class Solution:
    # 方法一 liweiwei
    def numIslands(self, grid):
        class UnionFind:
            def __init__(self, n):
                self.count = n
                self.parent = [i for i in range(n)]

            def get_count(self):
                return self.count

            def find(self, p):
                while p != self.parent[p]:
                    self.parent[p] = self.parent[self.parent[p]]
                    p = self.parent[p]
                return p

            def union(self, p, q):
                p_root = self.find(p)
                q_root = self.find(q)
                if p_root == q_root:
                    return
                self.parent[p_root] = q_root
                self.count -= 1

        row = len(grid)
        if row == 0:
            return 0
        col = len(grid[0])

        def get_index(x, y):
            return x * col + y

        # 陆地的个数
        spaces = 0
        uf = UnionFind(row * col)

        # 1、统计陆地的个数；2、合并水域
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '0':
                    spaces += 1
                else:
                    if i + 1 < row and grid[i + 1][j] == '1':
                        uf.union(get_index(i, j), get_index(i + 1, j))
                    if j + 1 < col and grid[i][j + 1] == '1':
                        uf.union(get_index(i, j), get_index(i, j + 1))

        return uf.get_count() - spaces
    
    # 方法二 powcai
    def numIslands(self, grid):
        f = {}

        def find(x):
            f.setdefault(x, x)
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            f[find(x)] = find(y)

        if not grid: 
            return 0
        row = len(grid)
        col = len(grid[0])

        # 第一次循环 并
        for i in range(row):
            for j in range(col):
                # 如果当前节点是1 检查左边和上边两个节点 如果也是1就连接起来
                if grid[i][j] == "1":
                    for x, y in [[-1, 0], [0, -1]]:
                        tmp_i = i + x
                        tmp_j = j + y
                        if 0 <= tmp_i < row and 0 <= tmp_j < col and grid[tmp_i][tmp_j] == "1":
                            union(tmp_i * col + tmp_j, i * col + j)
                        # print (tmp_i,tmp_j), (tmp_i * col + tmp_j, i * col + j)
                        # print f
        # 第二次循环 查
        res = set()
        for i in range(row):
            for j in range(col):
                # 如果当前节点是1 找出最终根节点
                if grid[i][j] == "1":
                    res.add(find(i * col + j))
        return len(res)

# [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
# (-1, 0) (-5, 0)
# {}
# (0, -1) (-1, 0)
# {}
# (-1, 1) (-4, 1)
# {}
# (0, 0) (0, 1)
# {0: 1, 1: 1}
# (-1, 2) (-3, 2)
# {0: 1, 1: 1}
# (0, 1) (1, 2)
# {0: 1, 1: 2, 2: 2}
# (-1, 3) (-2, 3)
# {0: 1, 1: 2, 2: 2}
# (0, 2) (2, 3)
# {0: 1, 1: 2, 2: 3, 3: 3}
# (0, 0) (0, 5)
# {0: 3, 1: 3, 2: 3, 3: 5, 5: 5}
# (1, -1) (4, 5)
# {0: 3, 1: 3, 2: 3, 3: 5, 5: 5}
# (0, 1) (1, 6)
# {0: 3, 1: 5, 2: 3, 3: 5, 5: 6, 6: 6}
# (1, 0) (5, 6)
# {0: 3, 1: 5, 2: 3, 3: 5, 5: 6, 6: 6}
# (0, 3) (3, 8)
# {0: 3, 1: 5, 2: 3, 3: 6, 5: 6, 6: 8, 8: 8}
# (1, 2) (7, 8)
# {0: 3, 1: 5, 2: 3, 3: 6, 5: 6, 6: 8, 8: 8}
# (1, 0) (5, 10)
# {0: 3, 1: 5, 2: 3, 3: 6, 5: 8, 6: 8, 8: 10, 10: 10}
# (2, -1) (9, 10)
# {0: 3, 1: 5, 2: 3, 3: 6, 5: 8, 6: 8, 8: 10, 10: 10}
# (1, 1) (6, 11)
# {0: 3, 1: 5, 2: 3, 3: 6, 5: 8, 6: 10, 8: 10, 10: 11, 11: 11}
# (2, 0) (10, 11)
# {0: 3, 1: 5, 2: 3, 3: 6, 5: 8, 6: 10, 8: 10, 10: 11, 11: 11}
