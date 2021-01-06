class Solution(object):
    # 并查集
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        f = {}
        edges = 0
        self.needs = n

        def find(x):
            f.setdefault(x, x)
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]
            
        def union(x, y):
            f[find(x)] = find(y)
            self.needs -= 1
            
        for a, b in connections:
            pa = find(a)
            pb = find(b)
            if pa != pb:
                union(a, b)
            else:
                edges += 1
                
        return self.needs-1 if edges >= self.needs-1 else -1
    
# 解法二 单独建立一个并查集class   
class Solution(object):    
     def makeConnected(self, n, connections):
        # 计算多余的线缆数量是否大于闭包之间的所需的线缆数量
        uf = UnionFind(n)
        edges,needs = 0,0
        for x,y in connections:
            px,py = uf.find(x),uf.find(y)
            if px != py:
                uf.union(x, y)
            else:
                edges += 1    
        # 计算闭包之间的所需的线缆数量
        needs = uf.count() - 1
        print needs, edges, uf.parent
        if edges < needs:
            return -1
        else:
            return needs     
# 并查集
class UnionFind():
    def __init__(self, n):
        self.parent = {}
        self.needs = n
            
    def find(self, x):
        self.parent.setdefault(x, x)
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)
        self.needs -= 1
        
    def count(self):
        return self.needs

    
    
