class Solution(object):
    def maxProbability(self, n, edges, succProb, start, end):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start: int
        :type end: int
        :rtype: float
        """
        d = defaultdict(list)
        for (x, y), p in zip(edges, succProb):
            d[x].append((y, p))
            d[y].append((x, p))
            
        queue = deque([(start, 1)])
        record = defaultdict(int)
        res = 0
        
        while queue:
            node, prob = queue.popleft()
            if node == end:
                res = max(res, prob)
                continue

            for neighbor, neighbor_prob in d[node]:
                new_prob = neighbor_prob * prob
                if new_prob > record[neighbor]:
                    record[neighbor] = new_prob
                    queue.append((neighbor, new_prob))
        return res
