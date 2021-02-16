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
        res = 0
        dic = defaultdict(dict)
        for (x, y), p in zip(edges, succProb):
            dic[x][y] = p
            dic[y][x] = p
        
        q = deque([(start, 1)])
        
        # probabilities from start to each node
        record = [0] * n
        record[start] = 1
        
        while q:
            node, prob = q.popleft()      
            if node == end:
                res = max(res, prob)
            for nei, p in dic[node].items():
                if prob * p > record[nei]:
                    q.append((nei, prob * p)) 
                    record[nei] = prob * p
        return res
        
