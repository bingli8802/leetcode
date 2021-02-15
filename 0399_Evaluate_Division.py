class Solution(object):
    # BFS
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        ret = []
        dic = dict()
        for i in range(len(equations)):
            v1 = equations[i][0]
            v2 = equations[i][1]

            if v1 not in dic:
                dic[v1] = dict()
            if v2 not in dic:
                dic[v2] = dict()
            dic[v1][v2] = values[i]
            dic[v2][v1] = 1 / values[i]

        for node in dic.keys():
            scaned = set()
            queue = [(node,1)]
            while queue:
                p, w = queue.pop()
                scaned.add(p)
                for k, v in dic[p].items():
                    if k not in scaned:
                        queue.append((k, w*v))
                        dic[node][k] = w*v
        ret = [-1] * len(queries)
        for i, query in enumerate(queries):
            if query[0] in dic and query[0] == query[1]:
                ret[i] = 1.0
            elif query[0] in dic and query[1] in dic[query[0]]:
                ret[i] = dic[query[0]][query[1]]
        return ret

    # Floyd
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = defaultdict(int)
        set1 = set()
        for i in range(len(equations)):
            a, b = equations[i]
            graph[(a, b)] = values[i]
            graph[(b, a)] = 1/values[i]
            set1.add(a)
            set1.add(b)
        print graph

        # Floyd算法 求图中任意2点距离
        arr = list(set1)
        for k in arr:
            for i in arr:
                for j in arr:
                    if graph[(i, k)] and graph[(k, j)]:
                        graph[(i, j)] = graph[(i, k)] * graph[(k, j)]
        
        res = []
        for x, y in queries:
            if graph[(x, y)]:
                res.append(graph[(x, y)])
            else:
                res.append(-1)
        return res


