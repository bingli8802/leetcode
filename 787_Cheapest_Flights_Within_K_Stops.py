class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        # costs = {0: [(1, 100), (2, 500)], 1: [(2, 100)]}
        costs = defaultdict(list)
        for (x, y, z) in flights:
            costs[x].append((y, z))
        
        q = deque([(src, 0, 0)])
        res = float('inf')
        
        # record = {0: 0, 1: inf, 2: inf} record cost for each node
        record = defaultdict(float)
        for i in range(n):
            record[i] = float('inf')
        record[src] = 0
        
        while q:
            node, cost, cnt = q.popleft()
            if node == dst:
                if cnt > K+1:  # if count is more than K+1 need to return
                    if res != float('inf'):
                        return res
                    else:
                        return -1
                elif cnt <= K+1:  # if count is less than K+1 continue to pop the queue
                    res = min(res, cost)
                    continue
            for nei, nei_cost in costs[node]:  # check each neighbor and update the costs
                new_cost = cost + nei_cost
                if new_cost < record[nei]:
                    record[nei] = new_cost
                    q.append((nei, new_cost, cnt+1))
                    
        if res == float('inf'):
            return -1
        else:
            return res

