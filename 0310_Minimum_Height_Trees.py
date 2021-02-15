class Solution(object):
    # BFS 超时
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        dic = defaultdict(list)
        res = []
        for x, y in edges:
            dic[x].append(y)
            dic[y].append(x)
        # print dic
        cur_min = float('inf')
        for node in range(n):
            q = deque([(node, 0)])
            visited = []
            while q:
                root, height = q.popleft()
                visited.append(root)
                for nei in dic[root]:
                    if nei in visited:
                        continue
                    else:
                        q.append((nei, height+1))
            if height < cur_min:
                cur_min = height
                res = [node]
            elif height == cur_min:
                res.append(node)        
        return res
    
    # 下面两种解法思路一样
    # 先找出叶子节点 即degree=1 的节点并入队
    # 每次读一个叶子节点，把dic里相连边的degree-1，如果当点节点degree=1 就再入队
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]
        # g = [[] for _ in range(n)]
        g = defaultdict(list)
        degrees = [0] * n
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
            degrees[u] += 1
            degrees[v] += 1
        # g = {0: [3], 1: [3], 2: [3], 3: [0, 1, 2, 4], 4: [3, 5], 5: [4]}) 
        # degrees = [1, 1, 1, 4, 2, 1]
        layer = deque()
        for i,v in enumerate(degrees):
            if v == 1:
                layer.append(i)
        while layer:
            next_layer = []
            for i in range(len(layer)):
                u = layer.popleft()
                next_layer.append(u)
                for v in g[u]:
                    degrees[v] -= 1
                    if degrees[v] == 1:
                        layer.append(v)
        return next_layer

    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # 从最外层遍历,最后一层即为结果.
        if n == 1:
            return [0]
        # 构造邻接表和度
        adjs = defaultdict(list)
        degrees = [0 for _ in range(n)]
        for (f, t) in edges:
            adjs[f].append(t)
            adjs[t].append(f)
            degrees[f] += 1
            degrees[t] += 1   
        # 第一层(最外层)
        layer = []
        for ind, val in enumerate(degrees):
            if val == 1:
                layer.append(ind)
        # 层层缩进:遍历当前层,确定下一层节点.
        while layer:
            next_layer = []
            for node in layer:
                for neighbor in adjs[node]:
                    degrees[neighbor] -= 1
                    if degrees[neighbor] == 1:
                        next_layer.append(neighbor)
            if not next_layer:  # 下一层没东西了,说明当前遍历的最后一层,也就是我们需要的
                return layer
            layer = next_layer




