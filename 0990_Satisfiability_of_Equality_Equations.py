class UnionFind: #定义并查集
    def __init__(self,equations):
        self.parent = defaultdict(str) #初始化父亲列表 用到了字典储存
        for s in equations: #初始化父亲列表，所有变量指向自己
            self.parent[s[0]] = s[0]
            self.parent[s[3]] = s[3]
            
    def find(self,x): #查找函数
        # 这部分代码是完全压缩路径
        # if self.parent[x] != x:
        #     self.parent[x] = self.find(self.parent[x])
        # return self.parent[x]
        
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self,x,y): #合并函数
        # 这部分代码是完全压缩路径
        # if self.find(x) != self.find(y):
        #     self.parent[self.find(x)] = self.parent[self.find(y)]
        
        if self.find(x) != self.find(y):
            self.parent[self.find(x)] = self.find(y)

class Solution:
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        uf = UnionFind(equations)
        for s in equations:
            if s[1] == "=": #等号的时候合并
                uf.union(s[0],s[3])
        for s in equations: #检查不等号是否有矛盾
            if s[1] == "!" and uf.find(s[0]) == uf.find(s[3]):
                return False
        return True
    
# liweiwei解法 
class UnionFind:
    def __init__(self, n):
        # 初始化父亲列表 用list储存
        self.parent = [i for i in range(n)]
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def union(self, p, q):
        if self.connected(p, q): return
        self.parent[self.find(p)] = self.find(q)
    def connected(self, p, q):
        return self.find(p) == self.find(q) 
    
class Solution:
    def equationsPossible(self, equations):       
        uf = UnionFind(26)
        for e in equations:
            if e[1] == "=":
                index1 = ord(e[0])-ord("a")
                index2 = ord(e[3])-ord("a")
                uf.union(index1, index2)
        
        for e in equations:
            if e[1] == "!":
                index1 = ord(e[0])-ord("a")
                index2 = ord(e[3])-ord("a")
                if uf.connected(index1, index2):
                    return False
        return True
