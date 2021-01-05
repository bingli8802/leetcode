class UnionFind:
    def __init__(self, isConnected):
        self.parent = defaultdict(int)
        for i in range(len(isConnected)):
            self.parent[i] = i
    
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    # def find(self, x):
    #     if self.parent[x] != x:
    #         self.parent[x] = self.find(self.parent[x])
    #     return self.parent[x]
    
    def union(self, x, y):
        if self.find(x) != self.find(y):
            self.parent[self.find(x)] = self.find(y)

class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        res = set()
        uf = UnionFind(isConnected)
        n = len(isConnected)
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    uf.union(i, j)
            # print uf.parent
            
        for i in uf.parent:
            res.add(uf.find(i))
        return len(res)
    
    
    
