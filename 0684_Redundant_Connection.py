class Solution(object):
    # 迭代 最初代码
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        l = len(edges)
        nums = [i for i in range(l + 1)]
        for item in edges:
            p1 = nums[item[0]]
            while p1 != nums[p1]:
                p1 = nums[p1]
            p2 = nums[item[1]]
            while p2 != nums[p2]:
                p2 = nums[p2]
            if p1 != p2:
                nums[p1] = item[1]
                print nums
            else:
                return item
    
    # 并查集算法
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # 用并查集，进来一对边，就查找两个节点的根节点，如果是一样的，那就不能要这对边，否则就增加这对边
        self.parent = {} 
        # 初始化所有的节点为单独的根节点
        for u, v in edges: 
            if u not in self.parent:
                self.parent[u] = u
            if v not in self.parent:
                self.parent[v] = v

            # 找到pu pv的父节点
            pu = self.find(u)
            pv = self.find(v)
            
            # 如果不相等就更新其中一个是另一个父节点
            if pu != pv:
                self.parent[pu] = self.parent[pv]
            else:
                return [u, v]

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x



