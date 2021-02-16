class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        # dic = {2:{1:1, 3:1}, 3:{4:1}}
        dic = defaultdict(dict)
        for x,y,z in times:
            dic[x][y] = z
        record = [float('inf')] * n  
        record[k-1] = 0
        q = deque([(k, 0)])
        # q.append([(k, 0)])
        visited = set()
        while q:
            node, base = q.popleft()
            visited.add(node)
            for nei, tm in dic[node].items():
                if base + tm < record[nei-1]:
                    record[nei-1] = base + tm
                    q.append((nei, base+tm))
                         
        if len(visited) != n:
            return -1
        else:
            return max(record)
    # 参考liweiwei BFS
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        # dic = {2:[(1, 1),(3, 1)], 3:[(4, 1)]}
        dic = defaultdict(list)
        for x, y, z in times:
            dic[x].append((y, z))

        # record = {1:0, 3:0, 4:0}
        record = defaultdict(int)
        for i in range(1, n+1):
            record[i] = float('inf')
        record[k] = 0
        q = deque([(k, 0)])
        visited = set()
        res = 0
        
        while q:
            node, tm = q.popleft() # node = 2, tm = 0
            visited.add(node)
            for nei, nei_tm in dic[node]:
                new_time = tm + nei_tm
                if new_time < record[nei]:
                    record[nei] = new_time # record = {1:1, 3:1, 4:2, 2:0}
                    q.append((nei, record[nei]))
                # q = []
        if len(visited) != n:
            return -1
        else:
            return max(record.values())

    def networkDelayTime(self, times, N, K):
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        pq = [(0, K)]
        dist = {}
        while pq:
            d, node = heapq.heappop(pq)
            if node in dist: 
                continue
            dist[node] = d
            for nei, d2 in graph[node]:
                if nei not in dist:
                    heapq.heappush(pq, (d+d2, nei))

        return max(dist.values()) if len(dist) == N else -1

