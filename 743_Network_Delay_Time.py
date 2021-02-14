class Solution(object):
    # 参考liweiwei
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
        
    # 网友答案 差不多
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        dic = collections.defaultdict(list)
        for u,v,w in times:
            dic[u].append((v,w))
        visited = {k:0}
        queue = collections.deque([[k,0]])
        while queue:
            curNode,curTime = queue.popleft()
            for node,time in dic[curNode]:
                t = curTime + time
                if node not in visited or t < visited[node]:
                    visited[node] = t
                    queue.append([node,t])
        if len(visited) == n:
            return max(visited.values())
        return -1



                
